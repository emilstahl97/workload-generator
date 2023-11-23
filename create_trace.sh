#!/bin/bash

start_time=$(date +%s.%N)

echo "Running create_trace.sh"

echo "Running trace_producer.py"

# Run the trace producer
trace_file_path=$(python3 ~/workload-generator/trace_producer.py 1000 FB-UP 0.9)

echo "Finished trace_producer.py"

echo "Running parse_trace.py"

# Run the parse_trace.py script with the path to the trace file
python3 ~/workload-generator/scripts/parse_trace.py "$trace_file_path"

echo "Finished parse_trace.py"

# Extract the name of the trace file without the path and extension
trace_file_name=$(basename "$trace_file_path")

# Save the name of the json file
json_file_name="${trace_file_name%.*}.json"

# the path to the json file is ~/workload-generator/json_traces/$json_file_name
json_file_path=~/workload-generator/json_traces/$json_file_name

echo "Running create_pcap_file.py"

# Run the create_pcap_file.py script with the name of the json file
python3 ~/workload-generator/scripts/create_pcap_file.py "$json_file_path"

echo "Finished create_pcap_file.py"

echo ""
end_time=$(date +%s.%N)
elapsed_time=$(echo "$end_time - $start_time" | bc)

echo "Script execution completed in $elapsed_time seconds."