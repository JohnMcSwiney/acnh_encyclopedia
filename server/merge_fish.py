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
foundUrls = []


for fish_info in fish_data:
    # Go through each fish
    name = fish_info["Fish"]
    # split fish names apart middle is always empty
    fish_tuples = split_and_clean_names(name) 
    
    found_match = False  # Flag to track if a match is found for the current fish
    print()
    print("current fish: ", fish_tuples)
    
    isMultipleWords = 0 # 0 no / 1 yes
    
    if fish_tuples[2] != '':
                print('more than one word fish')
                isMultipleWords = 1
    elif fish_tuples[2]:
                print('one word fish')
                isMultipleWords = 0
         
    for url in enumerate(urls):
        match isMultipleWords:
            case 0:
                # print("yep, one word")
                if url[1] not in foundUrls: #duplicate prevention
                    index = url[1].lower().find(fish_tuples[0].lower())
                    if index > 0:
                        # print( "Found Fish, one word")
                        combined_data.append({"name": name, "url": url})
                        foundUrls.append(url[1])
                        found_match = True
                        break
                
            case 1:
                # print("unhuh, this is more") 
                if url[1] not in foundUrls: #duplicate prevention
                    index = url[1].lower().find(fish_tuples[0].lower())
                    index2 = url[1].lower().find(fish_tuples[2].lower())
                    if index > 0 and index2 > 0:
                        # print( "Found Fish, more than one word")
                        combined_data.append({"name": name, "url": url})
                        foundUrls.append(url[1])
                        found_match = True
                        break
                        
            
            
    # for url in enumerate(urls):
        # check if fish name part 1 is in url
        # index = url[1].find(fish_tuples[0])
        
        # if index != -1:
            # if fish name p1 = true then check fish name p2
            # print('found fish')
            # checks to see if fish name p2 is empty or not
            
            # v more than one word fish 
            # if fish_tuples[2] != '':
            #     print('more than one word fish')
                
                # index2 = url[1].find(fish_tuples[2])
                # # if found then add together and move onto next fish
                # if index2 != -1:
                #     if url[1] not in foundUrls: #duplicate prevention
                #         print( "Found Fish")
                #         combined_data.append({"name": name, "url": url})
                #         found_match = True
                #         break
            
            # v one word fish 
            # if fish_tuples[2] == '':
            #     print('one word fish')
                
                # if url[1] not in foundUrls: #duplicate prevention
                #     print( "Found Fish")
                #     combined_data.append({"name": name, "url": url})
                #     found_match = True
                #     break
                
            
            
            # foundUrls.append(url[1])
            # combined_data.append({"name": name, "url": url})
            # found_match = True
            # break
            
        # pattern = re.escape(name)
        # count =+ 1
        
        # if re.search(pattern, url):
        #     combined_data.append({"name": name, "url": url})
        #     found_match = True
        #     # fishIndex = fish_data.index(name)
        #     # urlIndex = urls.index(url)
            
        #     # print(list(filter(lambda x:x["fish_name"]==name,fish_data)))
            
        #     print("removing: ",  name,  " ",  url)
        #     # print("Printing to check",  fish_data[fishIndex], urls[urlIndex])
            
        #     print(list(filter(lambda x:x["Fish"]==name,fish_data)).index)
        #     print()
        #     fish_data.pop(count-2)
        #     urls.pop(count-2)
    print()     
        
            
    

    # Check if a match was found for the current fish
    if not found_match:
        unmatched_fish.append(name)

# print(fish_data)
# print(urls)
# Handle unmatched fish
# for fish_name in unmatched_fish:
#     missing_fish_tuples = split_and_clean_names(fish_name)
#     matched_urls = []
#     # print(missing_fish_tuples)
#     for url in urls:
#         if all(part in url for part in missing_fish_tuples):
#             matched_urls.append(url)

#     if matched_urls:
#         combined_data.extend([{"name": fish_name, "url": url} for url in matched_urls])

# Save the combined_data list to a JSON file
with open('matched_data.json', 'w') as output_json_file:
    json.dump(combined_data, output_json_file, indent=4)

# with open('output_fish_data.json', 'w') as output_json_file:
#     json.dump(fish_data, output_json_file, indent=4)

# with open('output_url_data.json', 'w') as output_json_file:
#     json.dump(urls, output_json_file, indent=4)

print("Matching results saved to matched_data.json")
