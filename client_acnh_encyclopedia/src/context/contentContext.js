// ErrorContext.js
import React, { createContext, useContext, useState, useEffect } from "react";

const ContentContext = createContext();

const ContentContextProvider = ({ children }) => {
  const [contentType, setContentType] = 
    useState(localStorage.getItem("contentValue") || "FISH")
  ;

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

  return (
    <ContentContext.Provider
      value={{
        contentType,
        updateContentVal,
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
