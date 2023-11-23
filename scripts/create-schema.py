import json

def get_json_fields(json_data):
    fields = set()

    def extract_fields(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                fields.add(key)
                extract_fields(value)
        elif isinstance(obj, list):
            for item in obj:
                extract_fields(item)

    extract_fields(json_data)
    return list(fields)

# Load your JSON data from a file
with open('2000-0.9-FB-UP.json', 'r') as file:
    json_data = json.load(file)

# Get the list of field names
field_names = get_json_fields(json_data)

# Print the field names
print(field_names)
