// ErrorContext.js
import React, { createContext, useContext, useState, useEffect } from "react";

const ContentContext = createContext();

const ContentContextProvider = ({ children }) => {
  const [contentType, setContentType] = 
    useState(localStorage.getItem("contentValue") || "FISH")
  ;
  const [currentCreature, setCurrentCreature] = 
    useState(localStorage.getItem("currentCreature") || "NO_SELECTION")
  ;
  const [creatureObject, setCreatureObject] = useState(
    JSON.parse(localStorage.getItem("creatureObject")) || null
  );

 //   Content Library being used
  useEffect(() => {
    console.log("setting content val: " + contentType);
    localStorage.setItem("contentValue", contentType);
  }, [contentType]);
  
  const updateContentVal = (newContent) => {
    switch (newContent) {
      case "FISH":
        setContentType(newContent);
        break;
      case "BUG":
        setContentType(newContent);
        break;
      case "DIVE":
        setContentType(newContent);
        break;
      default:
        setContentType("FISH");
    }
  };

// Creature
// uses name of creature
  useEffect(() => {
    console.log("setting creature val: " + currentCreature);
    localStorage.setItem("currentCreature", currentCreature);
  }, [currentCreature]);

  const updateCurrentCreature = (newCreature) => {
    if(newCreature === "NO_SELECTION"){
        setCurrentCreature(newCreature);
    }else if(newCreature === '' || newCreature === null){
        setCurrentCreature("NO_SELECTION");
    }else{
        setCurrentCreature(newCreature);
    }
  };

 // Update creatureObject and store it in local storage
 const updateCreatureObject = (creatureObj) => {
    setCreatureObject(creatureObj);
  };

  useEffect(() => {
    // Convert creatureObject to JSON and store it in local storage
    localStorage.setItem('creatureObject', JSON.stringify(creatureObject));
  }, [creatureObject]);

  return (
    <ContentContext.Provider
      value={{
        contentType,
        updateContentVal,
        currentCreature,
        updateCurrentCreature,
        creatureObject,
        updateCreatureObject
      }}
    >
      {children}
    </ContentContext.Provider>
  );
};

const useContentContext = () => {
  return useContext(ContentContext);
};

export { ContentContextProvider, useContentContext };
