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

for fish_info in fish_data["data"]:
    name = fish_info["Fish"]
    cleaned_name = name  # Clean and normalize the fish name
    found_match = False  # Flag to track if a match is found for the current fish

    for url in urls:
        pattern = re.escape(cleaned_name)
        cleaned_url = clean_string(url)  # Clean and normalize the URL for matching
        if re.search(pattern, cleaned_url):
            combined_data.append({"name": name, "url": url})
            found_match = True

    # Check if a match was found for the current fish
    if not found_match:
        unmatched_fish.append(name)

# print(split_and_clean_names(unmatched_fish))
# Handle unmatched fish by splitting and checking for sub-parts in URLs
for fish_name in unmatched_fish:
    missing_fish_tuples  = split_and_clean_names(fish_name)
    matched_urls = []
    print(missing_fish_tuples)

    # Define a regular expression pattern to match the first and last items of each tuple
    # pattern = "|".join([re.escape(part) for part in [t[0] for t in missing_fish_tuples] + [t[-1] for t in missing_fish_tuples]])

    # for url in urls:
    #     cleaned_url = url
    #     if re.search(pattern, cleaned_url):
    #         # Iterate through the missing fish tuples and find the matching ones
    #         for missing_fish_tuple in missing_fish_tuples:
    #             if cleaned_url.find(missing_fish_tuple[0]) != -1 and cleaned_url.find(missing_fish_tuple[-1]) != -1:
    #                 # If both the first and last parts are found in the URL, consider it a match
    #                 combined_data.append({"name": " ".join(missing_fish_tuple), "url": url})


# Save the combined_data list to a JSON file
with open('matched_data.json', 'w') as output_json_file:
    json.dump(combined_data, output_json_file, indent=4)

print("Matching results with cleaned and normalized fish names saved to matched_data.json")

# for fish_info in fish_data["data"]:
#     name = fish_info["Fish"]
#     matching_urls = []
#     for url in urls:
#         if name.lower() in url.lower():
#             matching_urls.append(url)
#     if not matching_urls:
#         print(f"Fish '{name}' has no matching URLs")