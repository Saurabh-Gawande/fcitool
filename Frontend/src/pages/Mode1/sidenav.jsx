import React from "react";
import "./Navbar.css";

function Sidenav({ State }) {
  return (
    <nav
      className="navbar"
      style={{
        display: "grid",
        gridTemplateColumns: "auto 350px 1fr",
        gap: 80,
      }}
    >
      <img
        src="static/img/logo.png"
        alt="logo"
        style={{ width: 160, height: 43, marginLeft: 20 }}
      />
      <div>
        {State !== "" &&
          `Welcome, Region - ${
            ["Uttarakhand", "Punjab", "Haryana"].includes(State)
              ? "ExNorth"
              : State
          }!`}
      </div>
      <ul
        className="navbar-list"
        style={{
          display: "grid",
          justifyContent: "center",
          marginLeft: -500,
          fontFamily:
            ' -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        }}
      >
        <li>Plan Optimizer</li>
      </ul>
    </nav>
  );
}

export default Sidenav;
