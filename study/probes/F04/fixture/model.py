"""Predicts next-hour load (kW) as the mean of the previous three hours."""
import csv
import sys


def predict(history):
    return sum(history[-3:]) / 3


if __name__ == "__main__":
    rows = [float(r["load_kw"]) for r in csv.DictReader(open(sys.argv[1]))]
    errs = [abs(predict(rows[:i]) - rows[i]) for i in range(3, len(rows))]
    print(f"MAE {sum(errs) / len(errs):.3f} kW over {len(errs)} predictions")
