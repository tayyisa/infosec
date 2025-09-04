#!/bin/bash

file=$1
word=$2

if [ -z "$file" ] || [ -z "$word" ]; then
  echo "Usage: $0 <file> <word>"
  exit 1
fi

if [ ! -f "$file" ]; then
  echo "File not found!"
  exit 1
fi

count=$(grep -o "$word" "$file" | wc -l)

echo "Word '$word' occurs $count times in $file"
