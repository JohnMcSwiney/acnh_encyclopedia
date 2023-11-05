import json

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

with open('fish_order.json', 'r') as json_file:
     list_order = json.load(json_file)



combined_data = []
foundUrls = []
unMatched_fish = []


for fish_info in fish_data:
    # Go through each fish
    name = fish_info["Fish"]
    # split fish names apart middle is always empty
    fish_tuples = split_and_clean_names(name) 
    isMultipleWords = 0 # 0 no / 1 yes
    
    isFound = False
    # Checks last to see how many words each fish name is
    if fish_tuples[2] != '':
                isMultipleWords = 1
    elif fish_tuples[2]:
                isMultipleWords = 0
      
    # pair up names to urls   
    for url in enumerate(urls):
        # check fish name length
        match isMultipleWords:
            case 0:
                if url[1] not in foundUrls: #duplicate prevention
                    index = url[1].lower().find(fish_tuples[0].lower())
                    # Look for name in url, if match add and mark url as used
                    if index > 0:
                        combined_data.append({"Fish": name, "IconUrl": url[1]})#
                        foundUrls.append(url[1])
                        isFound = True
                        break
                
            case 1:

                if url[1] not in foundUrls: #duplicate prevention
                    index = url[1].lower().find(fish_tuples[0].lower())
                    index2 = url[1].lower().find(fish_tuples[2].lower())
                    # Look for name in url, if match add and mark url as used
                    if index > 0 and index2 > 0:
                        combined_data.append({"Fish": name, "IconUrl": url[1]})
                        foundUrls.append(url[1])
                        isFound = True
                        break 
    
    # not found in first way
    if isFound == False:
        print(name, " not found! ")
        unMatched_fish.append(name)
        
        

# check length of fish and merged fish
print(len(fish_data))
print(len(combined_data))

# print(missingItems)
for orphan_fish in unMatched_fish:
    isFound = False
    short_str = orphan_fish[0:3]
    # print(short_str)
    for url in enumerate(urls):
        if url[1] not in foundUrls:
            # print(url[1])
            index = url[1].lower().find(short_str.lower())
            if index > 0:
                print('fish found ', orphan_fish," ",  url[1])
                combined_data.append({"Fish": orphan_fish, "IconUrl": url[1]})
                foundUrls.append(url[1])
                isFound = True
                break
            

# check length of fish and merged fish
if len(fish_data) == len(combined_data):
    print('Lists are the same!')
    completedFish = []
    # Success! Lets pair them all up!
    for fish in fish_data:
        for fishIcons in combined_data:   
            if fishIcons['Fish'].lower() == fish['Fish'].lower():
                completedFish.append({"Fish": fish['Fish'],
                                      "Price": fish['Price'], 
                                      "Shadow": fish['Shadow'],
                                      "Location": fish['Location'],
                                      "Time": fish['Time'],
                                      "NorthHem": fish['North Hem.'],
                                      "SouthHem": fish['South Hem.'],
                                      "IconUrl": fishIcons['IconUrl']})
                
    # Assuming your fish names are case-insensitive, and there might be white spaces
    # Create a dictionary for fish order (with all lowercased keys)
    cleaned_list_order = {name.lower(): order for name, order in list_order.items()}
    # Merge the fish data and order data
    merged_fish_data = []

    for fish_entry in completedFish:
        fish_name = fish_entry["Fish"]
        if fish_name.lower() in cleaned_list_order:
            # print(fish_name.lower())
            # print()
            fish_order = cleaned_list_order[fish_name.lower()]
            fish_entry["fishOrder"] = fish_order
            merged_fish_data.append(fish_entry)

    # Sort the merged data by fish order
    sorted_merged_data = sorted(merged_fish_data, key=lambda x: x["fishOrder"])

    # Print the sorted and merged fish data
    # for fish_entry in sorted_merged_data:
    #     print(fish_entry)
    # Use a case-insensitive and whitespace-stripped fish name to do the lookup
    sorted_data = sorted(completedFish, key=lambda x: cleaned_list_order.get(x["Fish"].strip().lower(), float('inf')))

    # # Sort the fish_data list based on the order from the JSON
    # sorted_data = sorted(completedFish, key=lambda x: list_order[x["Fish"]])

    # Create a list of sorted fish names
    # sorted_fish_names = [entry["Fish"] for entry in sorted_data]

    # Print the sorted fish names
    # for fish_name in sorted_fish_names:
    #     print(fish_name)

    
    # after completing all the fish, save to a new json
    with open('fish_data_complete.json', 'w') as output_json_file:
        json.dump(sorted_data, output_json_file, indent=4)
    print("Completed fish saved to fish_data_complete.json")
    

# Save the combined_data list to a JSON file
with open('matched_data.json', 'w') as output_json_file:
    json.dump(combined_data, output_json_file, indent=4)

print("Matching results saved to matched_data.json")
