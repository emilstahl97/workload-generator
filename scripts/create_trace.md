
# run the trace producer located in the ~/workload-generator/
python3 trace_producer.py 2000 FB-UP 0.9

# the trace_producer.py script outputs a file path to the trace file, save this path to a variable

# run the parse_trace.py script located in the ~/workload-generator/scripts/ directory with the path to the trace file as an argument

# the parse_trace.py script outputs creates a json file in the ~/workload-generator/json_traces. The name of the file is the same as the name of the trace file, but with a .json extension. Save the name of the json file to a variable

# run the create_pcap_file.py script located in the ~/workload-generator/scripts/ directory with the name of the json file as an argument

