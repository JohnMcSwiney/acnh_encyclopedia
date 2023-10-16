import React,{ useState, useEffect } from 'react'


function App() {

  const [data,setData] = useState(null);

  useEffect(()=>{
    fetch('http://localhost:8000/members', {
  method: 'GET',
  credentials: 'include',
})
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the response as JSON
  })
  .then(data => {
    // Handle the JSON data
    setData(data);
    console.log(data);
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

  },[])

  return (
    <div>App</div>
  )
}

export default App
