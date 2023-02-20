#!/bin/bash

# Set the query directory
query_dir="BenchmarkTest"

query_cmd="python2 nlde.py -s http://localhost:5000/dbpedia -r n -t 1800 -f"

# Loop through the query files
for query_file in "$query_dir"/*.rq
do
  # Set the output file name
  extra_string="_noPolicy"
  output_file="${query_file%%.*}${extra_string}.csv"
  #The %%.* parameter expansion is used to remove the extension from the query_file variable

  # Run the command 30 times
  for i in {1..3}
  do
    echo "Running query $query_file (iteration $i)"
    start_time=$(date +%s)
    $query_cmd "$query_file" -r n >> "$output_file"
    if [ $? -ne 0 ]; then
      end_time=$(date +%s)
      elapsed_time=$((end_time - start_time))
      if [ $elapsed_time -lt 1800 ]; then
        echo "Error: Failed to execute query $query_file (iteration $i)"
        echo "Killing all running Python processes"
        killall -9 python
        continue
      else
        echo "Query $query_file (iteration $i) has reached timeout"
        killall -9 python
      fi
    fi
  done
done
