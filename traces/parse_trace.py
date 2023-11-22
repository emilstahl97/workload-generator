import json

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
                flow_source_id, flow_dest_id, flow_size = map(int, flow_info)
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

# Example usage:
file_path = '2000-0.9-FB-UP.txt'
parsed_data = parse_txt_to_json(file_path)
print(parsed_data)
