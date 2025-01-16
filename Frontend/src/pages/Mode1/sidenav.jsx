import React from "react";
import "./Navbar.css";

function Sidenav() {
  return (
    <nav
      className="navbar"
      style={{ display: "grid", gridTemplateColumns: "auto 1fr", gap: 10 }}
    >
      <img
        src="static/img/logo.png"
        alt="logo"
        style={{ width: 160, height: 43, marginLeft: 20 }}
      />
      <ul
        className="navbar-list"
        style={{
          display: "grid",
          justifyContent: "center",
          gap: 10,
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
