#!/bin/bash

END="18:00" 

NOW_STR=$(date +"%H:%M")
NOW_TS=$(date +%s)
END_TS=$(date -j -f "%Y-%m-%d %H:%M" "$(date +%Y-%m-%d) $END" +%s)

if [ "$NOW_TS" -ge "$END_TS" ]; then
  echo "Current time: $NOW_STR. Work day has ended."
  exit 0
fi

LEFT=$(( END_TS - NOW_TS ))
HOURS=$(( LEFT / 3600 ))
MINS=$(( (LEFT % 3600) / 60 ))

echo "Current time: $NOW_STR. Work day ends after ${HOURS} hours and ${MINS} minutes."

