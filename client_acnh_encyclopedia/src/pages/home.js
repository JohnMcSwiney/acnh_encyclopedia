import React, { useEffect, useState } from "react";
import { useContentContext } from "../context/contentContext";
import { FaFish, FaBug, FaLocationDot } from "react-icons/fa";
import { TbChartBubbleFilled, TbMapNorth, TbMapSouth } from "react-icons/tb";
import { PiCircleHalfFill } from "react-icons/pi";
import { MdLocationOn } from "react-icons/md";
import { BiTimeFive } from "react-icons/bi";

// FaFish
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
        // console.log(data[0]);
      })
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
      });
  }, []);
  return (
    <div className="page__container">
      <header className="selector__box">
        <button
          className={
            contentType === "FISH" ? "fish__btn selected " : "fish__btn"
          }
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
      <main>
        {contentType === "FISH" ? (
          <section>
            <div className="creature__box">
              <div className="creature__box__scrollable">
                {fishData.map((fishItem) => (
                  <FishCard
                    key={fishItem.Fish}
                    fishObject={fishItem}
                    // isSelected={{}}
                  />
                ))}
              </div>
            </div>
            <div>
              {contentContext.creatureObject !== null ? (
                <div className="fish__data__cont">
                  <section className="fish__data__title">
                    <h3>{contentContext.creatureObject.Fish}</h3>
                  </section>
                  <section className="fish__data__img">
                    <div>
                      <img src={contentContext.creatureObject.IconUrl}></img>
                    </div>
                  </section>
                  <section className="fish__data__items">
                    <div className="data__item__1">
                      <p>Available:</p>

                      <span>
                        <p>North </p>{" "}
                        <PiCircleHalfFill className="north icon" /> 
                        <p>[  {contentContext.creatureObject.NorthHem}  ]</p>
                      </span>

                      <span>
                        <p>South </p>{" "}
                        <PiCircleHalfFill className="south icon" /> 
                        <p>[  {contentContext.creatureObject.SouthHem}  ]</p>
                      </span>
                    </div>

                    <div className="data__item">
                      <p>Location:</p>

                      <span>
                        <MdLocationOn className="icon" />[
                        {contentContext.creatureObject.Location}]
                      </span>
                    </div>

                    <div className="data__item">
                      <p>Time:</p>

                      <span>
                        <BiTimeFive className="icon" />[
                        {contentContext.creatureObject.Time}]
                      </span>
                    </div>

                    <div className="data__item">
                      <p>Shadow:</p>

                      <span>
                        <FaFish className="icon" />[
                        {contentContext.creatureObject.Shadow}]
                      </span>
                    </div>
                  </section>
                </div>
              ) : (
                <div className="fish__data__cont">
                  <p>No Fish Data</p>
                </div>
              )}
            </div>
          </section>
        ) : contentType === "BUG" ? (
          <div>big</div>
        ) : contentType === "DIVE" ? (
          <div>dive</div>
        ) : (
          "loading"
        )}
      </main>
    </div>
  );
}

export default Home;
