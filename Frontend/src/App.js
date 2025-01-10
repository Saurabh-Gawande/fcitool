import "./App.css";
import * as React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import Home from "./pages/home";
import Daily_Planner from "./pages/Mode1/Daily_Planner";
import UserState from "./Context/userState";

function App() {
  return (
    <BrowserRouter>
      <UserState>
        <Routes>
          {/* <Route path="/home" element={<Home />} /> */}
          <Route path="/Movement_Planner" element={<Daily_Planner />} />
        </Routes>
      </UserState>
    </BrowserRouter>
  );
}

export default App;
