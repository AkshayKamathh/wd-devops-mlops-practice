#!/usr/bin/env python3

from collections import Counter
from pathlib import Path


def analyze_log(path: str = "predictions.log") -> None:
    log_path = Path(path)

    if not log_path.exists():
        raise FileNotFoundError(f"No log file found at {log_path}")

    preds = []

    with log_path.open() as f:
        for line in f:
            line = line.strip()

            if "prediction=" in line:
                part = line.split("prediction=")[1]
                try:
                    preds.append(int(part))
                except ValueError:
                    continue

    total = len(preds)
    print(f"Total predictions: {total}")

    if total == 0:
        print("No predictions found in log.")
        return

    counts = Counter(preds)

    for label, count in counts.items():
        pct = count / total * 100
        print(f"Class {label}: {count} ({pct:.1f}%)")


if __name__ == "__main__":
    analyze_log()
