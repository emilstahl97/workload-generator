import json
import sys

def parse_txt_to_json(file_path):
    data = {}

    with open(file_path, 'r') as file:
        # Read the first line
        num_inp_ports, num_coflows = map(int, file.readline().split())
        data['num_inp_ports'] = num_inp_ports
        data['num_coflows'] = num_coflows
        data['coflows'] = []

        for _ in range(num_coflows):
            coflow_info = file.readline().split()
            coflow_id, arrival_time, num_flows, num_sources, num_destinations = map(int, coflow_info[:5])
            flows = []

            for _ in range(num_flows):
                flow_info = coflow_info[5 + _ * 3: 8 + _ * 3]
                flow_source_id, flow_dest_id, flow_size = map(float, flow_info)
                flows.append({'source_id': flow_source_id, 'dest_id': flow_dest_id, 'size_mb': flow_size})

            coflow_data = {
                'coflow_id': coflow_id,
                'arrival_time': arrival_time,
                'num_flows': num_flows,
                'num_sources': num_sources,
                'num_destinations': num_destinations,
                'flows': flows
            }

            data['coflows'].append(coflow_data)

    return json.dumps(data, indent=2)

if __name__ == "__main__":
    # Check if the file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # Get the file path from the command line argument
    file_path = sys.argv[1]

    # Call the function with the provided file path
    parsed_data = parse_txt_to_json(file_path)

    # Save the parsed data to a json file
    with open(file_path.replace('.txt', '.json'), 'w') as file:
        file.write(parsed_data)

    print(f"Data successfully parsed from {file_path} and saved to {file_path.replace('.txt', '.json')}")
