#!/usr/bin/env bash
set -e

while getopts "c:s:o:p:" opt; do
  case $opt in
    c) COVER="$OPTARG" ;;
    s) SECRET="$OPTARG" ;;
    o) OUTPUT="$OPTARG" ;;
    p) PASS="$OPTARG" ;;
  esac
done

if [[ -z "$COVER" || -z "$SECRET" || -z "$OUTPUT" ]]; then
  echo "Usage: $0 -c cover_file -s secret_file -o output_file [-p passphrase]"
  exit 1
fi

if [ -z "$PASS" ]; then
  read -s -p "Enter passphrase: " PASS; echo
fi

# backup original
cp "$COVER" "$OUTPUT"

echo "Cover: $COVER"
echo "Secret: $SECRET"
echo "Output: $OUTPUT"

steghide embed -cf "$OUTPUT" -ef "$SECRET" -p "$PASS"
echo "Embedded $SECRET into $OUTPUT"

