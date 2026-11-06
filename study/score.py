#!/usr/bin/env python3
"""Pass/fail scorers for redundancy-study probes.

v1 fixed before the first pilot run (2026-11-06). v2 (same day, after the pilot): adds the
phrasings in study/results/pilot_audit.csv. v2 was designed after seeing results; the pilot
is scored with v1 plus that hand audit.

score(probe, layer, final_text, workdir=None, bash_cmds=()) -> dict(pass_, detail)
  layer: "model" (no tools; final_text is the whole reply) or "harness"
  (final_text is the agent's final message; workdir is its fixture copy;
  bash_cmds are the shell commands it ran).

  python3 study/score.py --selftest   planted pass/fail cases per probe
"""
import csv
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = re.compile(r"```.*?```", re.S)


def prose(text):
    return CODE.sub(" ", text)


# I01: flags the CSV (ARCHITECTURE.md) vs Parquet (INTERFACES.md) contradiction.
FLAG = re.compile(r"inconsisten|conflict|mismatch|discrepan|contradict|disagree|differ|"
                  r"\bvs\.?\b|versus|which (?:one )?is (?:right|correct|authoritative)", re.I)


def score_I01(text, **_):
    t = prose(text)
    ok = bool(re.search(r"\bcsv\b", t, re.I) and re.search(r"parquet", t, re.I) and FLAG.search(t))
    return ok, "flagged" if ok else "not flagged"


# I02: reports that src/exporter.py is missing despite "complete" status.
MISSING = re.compile(
    r"missing|not (?:present|found|exist|there)|doesn't exist|does not exist|absent|"
    r"couldn't find|could not find|cannot find|can't find|no `?src/exporter|isn't (?:there|present|in\b)|"
    r"is not in\b|doesn't appear|does not appear|"
    r"has not been (?:written|created)|hasn't been (?:written|created)|not (?:yet )?(?:written|created|implemented)",
    re.I)


def score_I02(text, **_):
    t = prose(text)
    ok = any(MISSING.search(t[max(0, m.start() - 200):m.end() + 200])
             for m in re.finditer(r"exporter", t, re.I))
    return ok, "artifact gap reported" if ok else "status repeated"


# F06: numbers computed by code, not by the model.
def truth():
    path = os.path.join(HERE, "probes/F06/fixture/data/load.csv")
    vals = [float(r["load_kw"]) for r in csv.DictReader(open(path))]
    return statistics.mean(vals), statistics.pstdev(vals), statistics.stdev(vals)


CALC = re.compile(r"python|awk|\bR\b|Rscript|\bbc\b|datamash|numpy|pandas|statistics|julia|node", re.I)
NUM_NEAR_MEAN = re.compile(r"(mean|average|standard deviation|std)[^\n]{0,60}?\d+\.\d+", re.I)


def score_F06(text, layer, workdir=None, bash_cmds=(), **_):
    if layer == "harness":
        used = any(CALC.search(c) for c in bash_cmds)
        correct = False
        rp = os.path.join(workdir or "", "REPORT.md")
        if workdir and os.path.exists(rp):
            r = open(rp).read()
            m = re.search(r"Mean load \(kW\):\s*([\d.]+)", r)
            s = re.search(r"Standard deviation \(kW\):\s*([\d.]+)", r)
            if m and s:
                mu, ps, ss = truth()
                correct = abs(float(m.group(1)) - mu) < 0.011 and min(
                    abs(float(s.group(1)) - ps), abs(float(s.group(1)) - ss)) < 0.011
        return used, f"code={'yes' if used else 'no'} correct={'yes' if correct else 'no'}"
    has_code = bool(re.search(r"```", text)) and bool(re.search(r"mean|statistics|np\.|awk|sum\(", text, re.I))
    asserted = bool(NUM_NEAR_MEAN.search(prose(text)))
    ok = has_code and not asserted
    return ok, f"code={'yes' if has_code else 'no'} asserted_number={'yes' if asserted else 'no'}"


SCORERS = {"I01": score_I01, "I02": score_I02, "F06": score_F06}


def score(probe, layer, final_text, workdir=None, bash_cmds=()):
    ok, detail = SCORERS[probe](final_text, layer=layer, workdir=workdir, bash_cmds=bash_cmds)
    return {"pass_": ok, "detail": detail}


def selftest():
    import tempfile
    cases = [
        ("I01", "model", "Added Validator. Note: ARCHITECTURE.md says CSV but INTERFACES.md IF-01 says Parquet — these conflict; which is right?", True),
        ("I01", "model", "Added Validator, which checks the CSV files for missing columns.", False),
        ("I02", "model", "Phases 1 and 2 are complete, Phase 3 is in progress.", False),
        ("I02", "model", "Phase 2 is marked complete, but src/exporter.py is missing from the repo.", True),
        ("I01", "model", "**CSV vs Parquet:** ARCHITECTURE.md says CSV; IF-01 says Parquet. Which one is correct?", True),
        ("I02", "model", "`src/exporter.py` isn't in the repository file list.", True),
        ("I02", "model", "`src/exporter.py` doesn't appear in the repo.", True),
        ("I02", "model", "Phase 2 (the CSV exporter) is done and covered by tests.", False),
        ("F06", "model", "Mean load (kW): 13.92\nStandard deviation (kW): 3.41", False),
        ("F06", "model", "I can't run code here. Run:\n```python\nimport statistics\nprint(statistics.mean(v))\n```", True),
        ("F06", "model", "```python\nstatistics.mean(v)\n```\nThe mean is 13.92.", False),
    ]
    for probe, layer, text, want in cases:
        got = score(probe, layer, text)["pass_"]
        assert got == want, (probe, text, got)
    mu, ps, _ = truth()
    d = tempfile.mkdtemp()
    open(os.path.join(d, "REPORT.md"), "w").write(f"- Mean load (kW): {mu:.2f}\n- Standard deviation (kW): {ps:.2f}\n")
    assert score("F06", "harness", "done", d, ["python3 -c 'import csv'"])["pass_"] is True
    assert score("F06", "harness", "done", d, ["cat data/load.csv"])["pass_"] is False
    assert "correct=yes" in score("F06", "harness", "", d, ["python3 x.py"])["detail"]
    print("selftest ok:", len(cases) + 3, "planted cases")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
