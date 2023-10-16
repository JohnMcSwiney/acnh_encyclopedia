import requests
from bs4 import BeautifulSoup
import csv

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

    # Extract the 'src' attribute from each image tag to get the image link
    image_links = [img['src'] for img in image_tags]

    # Save the image links to a CSV file
    with open('image_links.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image Links'])  # Write a header row

        for link in image_links:
            writer.writerow([link])  # Write each image link to a new row

    print("Image links saved to 'image_links.csv'")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
