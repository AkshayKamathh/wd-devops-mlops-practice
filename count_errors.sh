#!/usr/bin/env bash
FILE="$1"
grep "ERROR" "$FILE" | wc -l
