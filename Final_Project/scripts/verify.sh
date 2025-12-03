#!/usr/bin/env bash
set -e

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 original_file extracted_file"
    exit 1
fi

ORIG="$1"
EXTR="$2"

if [[ ! -f "$ORIG" ]]; then
  echo "Original file not found: $ORIG"
  exit 1
fi

if [[ ! -f "$EXTR" ]]; then
  echo "Extracted file not found: $EXTR"
  exit 1
fi

hash1=$(shasum -a 256 "$ORIG" | awk '{print $1}')
hash2=$(shasum -a 256 "$EXTR" | awk '{print $1}')

echo "Original:  $hash1"
echo "Extracted: $hash2"

if [[ "$hash1" == "$hash2" ]]; then
    echo "Files match (integrity OK)"
    exit 0
else
    echo "Files do NOT match"
    exit 2
fi

