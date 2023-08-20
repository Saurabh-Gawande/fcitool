import React, { useEffect } from "react";
import Sidenav from "./sidenav";

function Home() {
  useEffect(() => {});

  return (
    <div className="page-container" style={{ backgroundColor: "#ebab44b0"}}>
      <Sidenav />
      <div className="page-content" style={{ backgroundImage: "url('static/img/home3.jpg')" , height:'100vh'}}>
        <ul className="x-navigation x-navigation-horizontal x-navigation-panel" style={{ backgroundColor: "#ebab44b0"}}>
          <li className="xn-icon-button">
            <a href="#" className="x-navigation-minimize">
              <span className="fa fa-dedent" />
            </a>
          </li>
          <li
            className="xn-logo"
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              width: "90%",
            }}
          >
            <span style={{ color: "white", fontSize: "32px" }}>HOME PAGE</span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>

        <ul className="breadcrumb">
          <li>
            <a className="active">Home</a>
          </li>
        </ul>

        <div className="page-content-wrap">
          <div className="row">
            <div className="col-md-12">
              <center>
                <h1>
                  <strong>WELCOME TO FOOD CORPORATION OF INDIA</strong>
                </h1>
              </center>
              <br />
              {/* <div className="profile-image">
                <center>
                  <img
                    src="static/img/FCI home.png"
                    className="figure-img img-fluid rounded"
                    alt="A generic square placeholder image with rounded corners in a figure."
                  />
                </center>
              </div> */}
              <br />
              <br />
              <br />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
