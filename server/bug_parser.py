import csv
import json

csv_file_path = 'insects.csv'
json_file_path = 'bug_data.json'

# Read CSV and convert to JSON
bugs_data = []

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Get the headers and replace the unknown character with '#'
    headers = csv_reader.fieldnames
    headers[0] = '#'

    # Sort critters by their numbers
    sorted_rows = sorted(csv_reader, key=lambda x: int(x['#']))
    
    for row in sorted_rows:
        bugs_data.append(row)

# Write JSON data to a file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(bugs_data, json_file, ensure_ascii=False, indent=2)

print(f'Conversion completed. JSON data written to {json_file_path}')