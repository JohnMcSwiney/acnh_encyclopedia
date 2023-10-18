import json
import re

# Function to clean and normalize a string (remove spaces and other characters)
def clean_string(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text

# Function to split and clean fish names by underscores
def split_and_clean_names(name):
    split_names = name.partition(" ")
    # print(split_names)
    return [split_name for split_name in split_names]

# Read the JSON file containing fish data
with open('fish_data.json', 'r') as json_file:
    fish_data = json.load(json_file)

# Read the JSON file containing URLs
with open('image_links.json', 'r') as json_file:
    data = json.load(json_file)
    urls = data["urls"]

combined_data = []
unmatched_fish = []  # List to store fish without matching URLs

for fish_info in fish_data:
    name = fish_info["Fish"]
    found_match = False  # Flag to track if a match is found for the current fish

    for url in urls:
        pattern = re.escape(name)
        if re.search(pattern, url):
            combined_data.append({"name": name, "url": url})
            found_match = True

    # Check if a match was found for the current fish
    if not found_match:
        unmatched_fish.append(name)

# Handle unmatched fish
for fish_name in unmatched_fish:
    missing_fish_tuples = split_and_clean_names(fish_name)
    matched_urls = []
    print(missing_fish_tuples)
    for url in urls:
        if all(part in url for part in missing_fish_tuples):
            matched_urls.append(url)

    if matched_urls:
        combined_data.extend([{"name": fish_name, "url": url} for url in matched_urls])

# Save the combined_data list to a JSON file
with open('matched_data.json', 'w') as output_json_file:
    json.dump(combined_data, output_json_file, indent=4)

print("Matching results saved to matched_data.json")
