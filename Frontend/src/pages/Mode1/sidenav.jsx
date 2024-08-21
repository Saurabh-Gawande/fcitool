import React from "react";

function Sidenav() {
  return (
    <div className="page-sidebar">
      <ul className="x-navigation" style={{ backgroundColor: "#ebab44b0" }}>
        <li className="xn-logo">
          <a href="#">{localStorage.getItem("region")}</a>
          <a href="#" className="x-navigation-control"></a>
        </li>
        <li className="xn-profile">
          <a href="#" className="profile-mini">
            <img src="" alt="" />
          </a>
          <div className="profile" style={{ backgroundColor: "black" }}>
            <div className="profile-image">
              <img src="static/img/FCI.jpg" alt="" />
            </div>
            <div className="profile-data">
              <div className="profile-data-name">Food Corporation of India</div>
              <div className="profile-data-title"></div>
            </div>
          </div>
        </li>
        {/* <li>
          <a href="/home">
            <span className="fa fa-home"></span>{" "}
            <span className="xn-text">Home</span>
          </a>
        </li> */}
        {localStorage.getItem("region") === "admin" ||
        localStorage.getItem("region") === "H.P." ? (
          <li>
            <a href="/Monthly_Solution">
              <span className="fa fa-calendar"></span>
              <span className="xn-text">Monthly Plan</span>
            </a>
          </li>
        ) : null}
        {localStorage.getItem("region") === "H.P." ? null : (
          <li>
            <a href="/Daily_Planner">
              <span className="fa fa-desktop"></span>{" "}
              <span className="xn-text">Daily Planner</span>
            </a>
          </li>
        )}
        {/* <li>
          <a href="/Alternate_Railhead">
            <span className="fa fa-desktop"></span>{" "}
            <span className="xn-text">Alternate Railhead</span>
          </a>
        </li> */}
        {localStorage.getItem("region") === "admin" ||
        localStorage.getItem("region") === "H.P." ? (
          <li>
            <a href="/Mode2">
              <span className="fa fa-train"></span>{" "}
              <span className="xn-text">Mode2</span>
            </a>
          </li>
        ) : null}
        {/* <li>
          <a href="/Reset_Password">
            <span className="fa fa-train"></span>{" "}
            <span className="xn-text">Change Password</span>
          </a>
        </li> */}
        {/* <li>
          <a href="/logout">
            <span className="fa fa-sign-out"></span>{" "}
            <span className="xn-text">Logout</span>
          </a>
        </li> */}
      </ul>
    </div>
  );
}

export default Sidenav;
