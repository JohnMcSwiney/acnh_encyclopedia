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

# bug_name_1 > removing the "_NH_Icon.png"
# bug_name_2 > removing the "120px-"
# bug_name_3 > replace "_" with " "
for url in urls:
        # Parse the URL and get the filename
        filename = urlparse(url).path.split('/')[-1]
        
        # Extract name from the filename
        bug_name_1 = unquote(filename.split('_NH_Icon.png')[0])
        print(bug_name_1)
        
        try:
            bug_name_2 = unquote(bug_name_1.split('120px-')[1])
            print(bug_name_2)
        except:
            print("|!| - Unable strip: " + bug_name_1 + " any further")
            bug_name_2 = bug_name_1

        #Replace the underscores in the bug-names with spaces 
        #Attempt and handle errors from text without _
        try:
            bug_name_3 = bug_name_2.replace("_", " ", 3)
        except:
            bug_name_3 = bug_name_2

        # Create a dictionary with name and URL,
        # Catch potential errors
        try:
            bug_entry = {"name": bug_name_3, "url": url}
        
        except:
             print("|!| - Unable to combine Entry and URL")

        bugs_info.append(bug_entry)


# Create a new JSON file with the extracted information
output_json_file_path = 'bug_images_may2025-test.json'
with open(output_json_file_path, 'w', encoding='utf-8') as json_output_file:
    json.dump(bugs_info, json_output_file, ensure_ascii=False, indent=2)

print(f'Extraction completed. JSON data written to {output_json_file_path}')
