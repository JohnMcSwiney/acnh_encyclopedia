import requests
from bs4 import BeautifulSoup
import json

# URL of the web page to scrape
url = 'https://nookipedia.com/wiki/Category:New_Horizons_fish_icons'

# Send an HTTP request to the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags on the page
    image_tags = soup.find_all('img')

    # Extract the 'src' attribute from each image tag to get the image links
    image_links = [img['src'] for img in image_tags]

    # Create a dictionary with a "urls" key and the image links as its value
    data = {"urls": image_links}

    # Save the data to a JSON file
    with open('image_links.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Image links saved to 'image_links.json'")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
