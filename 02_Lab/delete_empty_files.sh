#!/bin/bash

dir=$1

if [ -z "$dir" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

if [ ! -d "$dir" ]; then
  echo "Directory not found!"
  exit 1
fi

for f in $(find "$dir" -type f -empty); do
  echo "Deleting empty file: $f"
  rm "$f"
done
