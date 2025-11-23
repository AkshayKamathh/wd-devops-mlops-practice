#!/usr/bin/env python3
import argparse
from pathlib import Path


def filter_logs(path: str, keyword: str) -> None:
    log_path = Path(path)
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    matches = 0
    with log_path.open() as f:
        for line in f:
            if keyword in line:
                print(line, end="")
                matches += 1

    print(f"\n--- Found {matches} lines containing '{keyword}' ---")


def main():
    parser = argparse.ArgumentParser(
        description="Filter log lines by keyword."
    )
    parser.add_argument(
        "--file", "-f", required=True, help="Path to log file"
    )
    parser.add_argument(
        "--keyword", "-k", required=True, help="Keyword to search for"
    )

    args = parser.parse_args()
    filter_logs(args.file, args.keyword)


if __name__ == "__main__":
    main()
