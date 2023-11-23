#!/bin/bash

# Run the trace producer
trace_file_path=$(python3 ~/workload-generator/trace_producer.py 10 FB-UP 0.9)

echo "Trace file path: $trace_file_path"

# Run the parse_trace.py script with the path to the trace file
python3 ~/workload-generator/scripts/parse_trace.py "$trace_file_path"

# Extract the name of the trace file without the path and extension
trace_file_name=$(basename "$trace_file_path")

echo "Trace file name: $trace_file_name"

# Save the name of the json file
json_file_name="${trace_file_name%.*}.json"

echo "Json file name: $json_file_name"

# the path to the json file is ~/workload-generator/json_traces/$json_file_name
json_file_path=~/workload-generator/json_traces/$json_file_name

echo "Json file path: $json_file_path"

# Run the create_pcap_file.py script with the name of the json file
python3 ~/workload-generator/scripts/create_pcap_file.py "$json_file_path"
