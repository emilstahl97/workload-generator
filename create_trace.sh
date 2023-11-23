#!/bin/bash

# Run the trace producer
trace_file_path=$(python3 ~/workload-generator/trace_producer.py 2000 FB-UP 0.9)

echo "Trace file path: $trace_file_path"

# Run the parse_trace.py script with the path to the trace file
python3 ~/workload-generator/scripts/parse_trace.py "$trace_file_path"

# Extract the name of the trace file without the path and extension
trace_file_name=$(basename "$trace_file_path")

# Save the name of the json file
json_file_name="${trace_file_name%.*}.json"

# Run the create_pcap_file.py script with the name of the json file
python3 ~/workload-generator/scripts/create_pcap_file.py "$json_file_name"
