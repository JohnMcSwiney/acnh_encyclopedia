import React, { useEffect, useState } from "react";
import { useContentContext } from "../context/contentContext";
import { FaFish, FaBug } from "react-icons/fa";
import { TbChartBubbleFilled } from "react-icons/tb";
import "./PageStyles.css";

import FishCard from "../components/fishCard";
function Home() {
  const contentContext = useContentContext();
  const contentType = contentContext.contentType;
  // console.log(contentType)
  // const [tempState,setTempState] =
  // useEffect(() => {

  // },[])
  const [data, setData] = useState([{}]);
  const [fishData, setFishData] = useState([{}]);
  useEffect(() => {
      fetch("http://localhost:8000/fish", {
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
          setFishData(data);
          console.log(data[0]);
        })
        .catch((error) => {
          console.error("There was a problem with the fetch operation:", error);
        });
  }, []);
  return (
    <div className="page__container">
      <header className="selector__box">
        <button
          className={contentType === "FISH" ? "fish__btn selected " : "fish__btn"}
          onClick={() => contentContext.updateContentVal("FISH")}
        >
          <p>Fish</p> <FaFish />
        </button>

        <button
          className={contentType === "BUG" ? "bug__btn selected " : "bug__btn"}
          onClick={() => contentContext.updateContentVal("BUG")}
        >
          <p>Bugs</p> <FaBug />
        </button>
        <button
          className={
            contentType === "DIVE" ? "dive__btn selected " : "dive__btn"
          }
          onClick={() => contentContext.updateContentVal("DIVE")}
        >
          <p>Dive</p> <TbChartBubbleFilled />
        </button>
        <button
          className="hidden__btn"
          onClick={() => contentContext.updateContentVal("FISH")}
        >
          <p>default val</p>
        </button>
      </header>
      <main className="creature__box">
          {contentType === 'FISH' ? 
          <div  className="creature__box__scrollable"
          >
            {fishData.map((fishItem) => (
              <FishCard
              key={fishItem.Fish}
              fishIcon={fishItem.IconUrl}
              // isSelected={{}}
              />
              
            ))}
          </div>
          :contentType ==='BUG' ? <div>big</div>
          :contentType === 'DIVE' ? <div>dive</div>
          :"loading"

          }
          


      </main>
    </div>
  );
}

export default Home;
