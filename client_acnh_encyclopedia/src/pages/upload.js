import React,{ useState, useEffect } from 'react'
import Papa from 'papaparse';

function Upload() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://localhost:8000/members", {
      method: "GET",
      credentials: "include",
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json(); // Parse the response as JSON
      })
      .then((data) => {
        // Handle the JSON data
        setData(data);
        console.log(data);
      })
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
      });
  }, []);
  function handleFileUpload(event) {
    const file = event.target.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const data = e.target.result;

        // Parse the CSV data
        Papa.parse(data, {
          complete: (result) => {
            // Process the parsed data
            processCSVData(result.data);
          },
          header: true, // Set this to true if the first row contains headers
        });
      };

      reader.readAsText(file);
    }
  }
  function processCSVData(data) {
    fetch("http://localhost:8000/upload-json", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include", // Add this line to include credentials
      body: JSON.stringify(data), // Convert the parsed data to JSON
    })
      .then((response) => {
        if (response.ok) {
          // Data was successfully sent to the server
          console.log("Data sent successfully.");
        } else {
          // Handle errors if the server returns an error status
          console.error("Error sending data to the server.");

          // Log the server's response
          response.text().then((data) => {
            console.error("Server Response:", data);
          });
        }
      })
      .catch((error) => {
        // Handle network errors or other issues
        console.error("Network error:", error);
      });
  }

  return (
    <div>
      <input type="file" onChange={handleFileUpload} />
      <img src="https://dodo.ac/np/images/thumb/d/de/Suckerfish_NH_Icon.png/120px-Suckerfish_NH_Icon.png" />
    </div>
  );
}

export default Upload;
