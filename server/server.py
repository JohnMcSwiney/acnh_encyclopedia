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
        r"/upload-csv": {
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


# Upload CSV route with improved error handling
@app.route("/upload-csv", methods=["POST"])
def upload_csv():
    try:
        data = request.get_json()  # Get the JSON data from the request

        # Process the data and save it to a CSV file
        save_to_csv(data)

        # Log a message to denote the creation of objects
        print("Objects created:", len(data))

        return jsonify({"message": "Data received and saved successfully"}), 200
    except Exception as e:
        # Handle errors and provide an error response
        print(f"Error processing data: {str(e)}")
        return jsonify({"error": "An error occurred while processing the data"}), 500


# Function to save data to a CSV file
import csv

def save_to_csv(data):
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
    
    # print(filtered_data[2])

    # Sort the filtered data by the "Fish" column (ascending order)
    sorted_data = sorted(filtered_data[1:], key=lambda x: x.get('Fish', ''))

    with open('data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_headers)
        writer.writeheader()

        for row in sorted_data:
            writer.writerow(row)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
