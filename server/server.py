from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)

# Configure CORS for specific routes
CORS(
    app,
    resources={
        r"/members/*": {
            "origins": "http://localhost:3000",
            "allow_headers": ["Content-Type"],
            "supports_credentials": True,
        }
    },
)
CORS(
    app,
    resources={
        r"/upload-json": {
            "origins": "http://localhost:3000",
            "allow_headers": ["Content-Type"],
            "supports_credentials": True,
        }
    },
)


# Members API route with a docstring
@app.route("/members")
def members():
    """Get a list of members."""
    return {"members": ["member1", "member2", "member3"]}


# Upload JSON route with improved error handling
@app.route("/upload-json", methods=["POST"])
def upload_json():
    try:
        data = request.get_json()  # Get the JSON data from the request

        # Process the data and save it to a JSON file
        save_to_json(data)

        # Log a message to denote the creation of objects
        print("Objects created:", len(data))

        return jsonify({"message": "Data received and saved successfully"}), 200
    except Exception as e:
        # Handle errors and provide an error response
        print(f"Error processing data: {str(e)}")
        return jsonify({"error": "An error occurred while processing the data"}), 500


# Function to save data to a JSON file
import json

def save_to_json(data):
    # Define the new header names without the "caught" column
    new_headers = ['Fish', 'Price', 'Shadow', 'Location', 'Time', 'North Hem.', 'South Hem.']

    # Ensure the "caught" column is removed from the first row (header)
    if 'caught' in data[0]:
        data[0].pop('caught')

    # Filter out rows with an empty "Fish" column
    filtered_data = [row for row in data if row.get('Fish', '')]

    # Remove the "caught" column from each data row
    for row in filtered_data:
        if 'caught' in row:
            row.pop('caught')
    for row in filtered_data:
        if '' in row:
            row.pop('')
    
    # Sort the filtered data by the "Fish" column (ascending order)
    sorted_data = sorted(filtered_data[1:], key=lambda x: x.get('Fish', ''))

    with open('fish_data.json', 'w') as file:
        json.dump(sorted_data, file)



import json

def save_to_json(data):
    # Define the new header names without the "caught" column
    new_headers = ['Fish', 'Price', 'Shadow', 'Location', 'Time', 'North Hem.', 'South Hem.']

    # Ensure the "caught" column is removed from the first row (header)
    if 'caught' in data[0]:
        data[0].pop('caught')

    # Filter out rows with an empty "Fish" column
    filtered_data = [row for row in data if row.get('Fish', '')]

    # Remove the "caught" column from each data row
    for row in filtered_data:
        if 'caught' in row:
            row.pop('caught')
    for row in filtered_data:
        if '' in row:
            row.pop('')

    # Sort the filtered data by the "Fish" column (ascending order)
    sorted_data = sorted(filtered_data[1:], key=lambda x: x.get('Fish', ''))

    # Create a dictionary to hold the sorted data
    json_data = {
        "headers": new_headers,
        "data": sorted_data
    }

    # Specify the filename for the JSON file
    json_filename = 'fish_data.json'

    # Write the data to the JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
