import './App.css';
import * as React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from './pages/login';
import Home from './pages/home';
import Logout from './pages/logout';
import Monthly_Solution from './pages/Mode1/Monthly_Solution';
import Alternate_Railhead from './pages/Mode1/Alternate_Railhead';
import Template from './pages/Mode1/Template';
import Monthly_Solution_M02 from './pages/Mode2/Monthly_Solution_M02';
import Alternate_Railhead_M02 from './pages/Mode2/Alternate_Railhead_M02';
import Daily_Scheduler_M02 from './pages/Mode2/Daily_Scheduler_M02';
import Daily_Planner from './pages/Mode1/Daily_Planner';

function App() {
  return (
  <BrowserRouter>
    <Routes>
		<Route path='/' element={<Login />} />
		<Route path='/login' element={<Login />} />
    <Route path='/home' element={<Home />} />
    <Route path='/logout' element={<Logout />} />
		<Route path='/Monthly_Solution' element={<Monthly_Solution />} />
    <Route path='/Alternate_Railhead' element={<Alternate_Railhead />} />
    <Route path='/Template' element={<Template />} />
    <Route path='/Monthly_Solution_M02' element={<Monthly_Solution_M02 />} />
    <Route path='/Alternate_Railhead_M02' element={<Alternate_Railhead_M02 />} />
    <Route path='/Daily_Scheduler_M02' element={<Daily_Scheduler_M02 />} />
    <Route path='/Daily_Planner' element={<Daily_Planner />} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
