import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import { ContentContextProvider } from "./context/contentContext";
import { Home, Upload } from "./pages";

import Header from "./components/header";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <div className="app__container">
        <ContentContextProvider>
          <Header />
          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/upload" element={<Upload />}></Route>
          </Routes>
        </ContentContextProvider>
      </div>
    </BrowserRouter>
  );
}

export default App;
