import "./App.css";
import * as React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import Home from "./pages/home";
import Daily_Planner from "./pages/Mode1/Daily_Planner";

function App() {
  return (
    <BrowserRouter>
      <>
        <Routes>
          {/* <Route path="/home" element={<Home />} /> */}
          <Route path="/Movement_Planner" element={<Daily_Planner />} />
        </Routes>
      </>
    </BrowserRouter>
  );
}

export default App;
