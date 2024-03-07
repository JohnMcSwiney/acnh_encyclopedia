import json
from urllib.parse import urlparse, unquote

# Read JSON data from a file
json_file_path = 'bug_image_links.json'  # Replace with the actual path to your JSON file

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data_list = json.load(json_file)
    urls = data_list["urls"]
    print(urls)
# Extract names from URLs
bugs_info = []

# for entry in data_list:
    # Access the "urls" key from each dictionary
    # print(data_list.urls)
for url in urls:
        # Parse the URL and get the filename
        filename = urlparse(url).path.split('/')[-1]

        # Extract name from the filename
        name = unquote(filename.split('_NH_Icon.png')[0])

        # Create a dictionary with name and URL
        bug_entry = {"name": name, "url": url}
        # print(bug_entry)
        bugs_info.append(bug_entry)
        # print(bug_entry)

# Create a new JSON file with the extracted information
output_json_file_path = 'bug_images.json'
with open(output_json_file_path, 'w', encoding='utf-8') as json_output_file:
    json.dump(bugs_info, json_output_file, ensure_ascii=False, indent=2)

print(f'Extraction completed. JSON data written to {output_json_file_path}')
