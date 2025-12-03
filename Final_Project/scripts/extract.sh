#!/usr/bin/env bash
set -e

OUT=""
PASS=""
FILE=""

while getopts "f:p:o:" opt; do
  case $opt in
    f) FILE="$OPTARG" ;;
    p) PASS="$OPTARG" ;;
    o) OUT="$OPTARG" ;;
  esac
done

if [[ -z "$FILE" ]]; then
  echo "Usage: $0 -f stego_file [-p passphrase] [-o output_file]"
  exit 1
fi

if [ -z "$PASS" ]; then
  read -s -p "Enter passphrase: " PASS; echo
fi

# Получаем абсолютный путь к stego-файлу
FILE_DIR="$(cd "$(dirname "$FILE")" 2>/dev/null && pwd || echo "$(pwd)")"
FILE_BASENAME="$(basename "$FILE")"
ABS_FILE="$FILE_DIR/$FILE_BASENAME"

# проверяем что файл существует
if [[ ! -f "$ABS_FILE" ]]; then
  echo "✘ File not found: $ABS_FILE"
  exit 1
fi

# создаём временную директорию
TMPDIR=$(mktemp -d)
pushd "$TMPDIR" >/dev/null

# steghide получает абсолютный путь → теперь всегда работает
steghide extract -sf "$ABS_FILE" -p "$PASS" >/dev/null

EXTRACTED=$(ls -1 2>/dev/null || true)
popd >/dev/null

if [[ -z "$EXTRACTED" ]]; then
  echo "✘ Extraction failed or no file extracted"
  rm -rf "$TMPDIR"
  exit 1
fi

if [[ -n "$OUT" ]]; then
  mv "$TMPDIR/$EXTRACTED" "$OUT"
  echo "wrote extracted data to \"$OUT\"."
else
  mv "$TMPDIR/$EXTRACTED" .
  echo "wrote extracted data to \"$EXTRACTED\"."
fi

rm -rf "$TMPDIR"
