#!/usr/bin/env python3
"""Count directive-inventory rows and derive the test sequence for
reports/schema_redundancy_ablation.md.

Row: | ID | Source | Directive | Class | Prior | Impact | Overlap |
Class B = behavioral, C = convention, M = merged into another row.
Test order: Impact H, then M (L not tested); within impact, prior unsure, likely, unlikely;
ties keep table order.

Usage:
  inventory_counts.py <report.md>     print counts and test order as markdown
  inventory_counts.py --selftest      check against a known-answer table
"""
import re
import sys
from collections import Counter

ROW = re.compile(r"^\| ([A-Z]\d{2}) \| (.+?) \| (.+?) \| ([BCM]) \| (.+?) \| (.+?) \| (.+?) \|$")
IMPACT_RANK = {"H": 0, "M": 1}
PRIOR_RANK = {"unsure": 0, "likely": 1, "unlikely": 2}


def parse(text):
    return [m.groups() for m in map(ROW.match, text.splitlines()) if m]


def counts(rows):
    cls = Counter(r[3] for r in rows)
    b = [r for r in rows if r[3] == "B"]
    cp = [r for r in b if r[1].startswith("CODING_PRACTICES")]
    return {
        "total": len(rows), "C": cls["C"], "B": cls["B"], "M": cls["M"],
        "B_likely": sum(r[4] == "likely" for r in b),
        "B_unsure": sum(r[4] == "unsure" for r in b),
        "B_unlikely": sum(r[4] == "unlikely" for r in b),
        "H": sum(r[5] == "H" for r in b), "Mi": sum(r[5] == "M" for r in b),
        "L": sum(r[5] == "L" for r in b),
        "CC": sum("CC" in r[6] for r in b),
        "CP_B": len(cp), "CP_likely": sum(r[4] == "likely" for r in cp),
        "CP_L": sum(r[5] == "L" for r in cp),
    }


def order(rows):
    b = [(i, r) for i, r in enumerate(rows) if r[3] == "B" and r[5] in IMPACT_RANK]
    b.sort(key=lambda x: (IMPACT_RANK[x[1][5]], PRIOR_RANK[x[1][4]], x[0]))
    return [r for _, r in b]


def render(rows):
    c = counts(rows)
    lines = [
        f"- Rows: {c['total']} ({c['B']} B, {c['C']} C, {c['M']} merged).",
        f"- B priors: {c['B_likely']} likely, {c['B_unsure']} unsure, {c['B_unlikely']} unlikely.",
        f"- B impact: {c['H']} H, {c['Mi']} M, {c['L']} L (L not tested).",
        f"- B rows with CC overlap: {c['CC']}.",
        f"- CODING_PRACTICES.md: {c['CP_B']} B directives, {c['CP_likely']} likely, {c['CP_L']} impact L.",
        "",
        "Test order:",
        "",
    ]
    lines += [f"{n}. {r[0]} ({r[5]}, {r[4]}) — {r[2]}" for n, r in enumerate(order(rows), 1)]
    return "\n".join(lines)


def selftest():
    sample = "\n".join([
        "| Z01 | X | a | C | — | — | — |",
        "| Z02 | X | b | B | likely | H | CC |",
        "| Z03 | CODING_PRACTICES §1 | c | B | likely | L | CC |",
        "| Z04 | CODING_PRACTICES §2 | d | B | unsure | M | — |",
        "| ID | Source | Directive | Class | Prior | Impact | Overlap |",
        "| Z05 | X | e | B | unlikely | H | — |",
        "| Z06 | X | f | M | — | — | →Z02 |",
        "| Z07 | X | g | B | unsure | H | — |",
    ])
    rows = parse(sample)
    got = counts(rows)
    want = {"total": 7, "C": 1, "B": 5, "M": 1, "B_likely": 2, "B_unsure": 2, "B_unlikely": 1,
            "H": 3, "Mi": 1, "L": 1, "CC": 2, "CP_B": 2, "CP_likely": 1, "CP_L": 1}
    assert got == want, (got, want)
    assert [r[0] for r in order(rows)] == ["Z07", "Z02", "Z05", "Z04"], [r[0] for r in order(rows)]
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        print(render(parse(open(sys.argv[1]).read())))
