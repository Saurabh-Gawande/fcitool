import "./App.css";
import * as React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import Home from "./pages/home";
import Logout from "./pages/logout";
import Monthly_Solution from "./pages/Mode1/Monthly_Solution";
import Template from "./pages/Mode1/Template";
import Daily_Planner from "./pages/Mode1/Daily_Planner";
import UserState from "./Context/userState";
import Reset_Password from "./pages/Mode1/Reset_Password";

function App() {
  return (
    <BrowserRouter>
      <UserState>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<Home />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/Monthly_Solution" element={<Monthly_Solution />} />
          <Route path="/Mode2" element={<Template />} />
          <Route path="/Daily_Planner" element={<Daily_Planner />} />
          <Route path="/Reset_Password" element={<Reset_Password />} />
        </Routes>
      </UserState>
    </BrowserRouter>
  );
}

export default App;
