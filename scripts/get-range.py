import json

# Specify the path to your JSON file
json_file_path = '2000-0.9-FB-UP.json'

# Read JSON data from the file
try:
    with open(json_file_path, 'r') as file:
        json_data = file.read()
        print("JSON data read successfully:")
except Exception as e:
    print("Error reading JSON file:", e)
    exit()

# Load JSON data
try:
    data = json.loads(json_data)
    print("JSON data loaded successfully:")
except json.JSONDecodeError as e:
    print("Error decoding JSON data:", e)
    exit()

# Extracting source_ids and dest_ids
source_ids = [flow["source_id"] for coflow in data["coflows"] for flow in coflow["flows"]]
dest_ids = [flow["dest_id"] for coflow in data["coflows"] for flow in coflow["flows"]]

# Finding the range
source_id_range = (min(source_ids), max(source_ids))
dest_id_range = (min(dest_ids), max(dest_ids))

# Printing the range
print(f'source_id_range: {source_id_range}')
print(f'dest_id_range: {dest_id_range}')

# removing duplicates from source_ids and dest_ids
source_ids = list(set(source_ids))
dest_ids = list(set(dest_ids))

# Printing the length of source_ids and dest_ids
print(f'len(source_ids): {len(source_ids)}')
print(f'len(dest_ids): {len(dest_ids)}')
