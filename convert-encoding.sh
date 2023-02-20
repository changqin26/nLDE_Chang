#!/bin/bash

# Specify the directory containing the files to convert
dir="Benchmark2Separate"

# Loop through each file in the directory
for file in "$dir"/*.rq; do
  # Convert the file from Windows(CRLF) to Unix(LF)
  dos2unix "$file"
done