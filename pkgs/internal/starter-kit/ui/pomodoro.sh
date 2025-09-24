#!/bin/bash
WORK=25
BREAK=5
while true; do
  echo "Focus for $WORK minutes..."
  sleep ${WORK}m
  echo "Break for $BREAK minutes..."
  sleep ${BREAK}m
done
