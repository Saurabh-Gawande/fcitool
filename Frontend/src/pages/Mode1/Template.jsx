import React, { useState } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import background1 from "./../../assets/update1.png";
import config from "../../config";

function Template() {
  const ProjectIp = config.serverUrl;
  const [fileSelected, setFileSelected] = useState(false);

  const handleFileChange = (event) => {
    setFileSelected(event.target.files.length > 0);
  };

  const handleSolveRoutePlan = async () => {
    try {
      const response = await fetch(ProjectIp + "/road_plan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // body: JSON.stringify(payload),
      });
      if (response.ok) {
        console.log("Solved route plan");
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } finally {
      console.log("error");
    }
  };

  const handleUploadConfig = async () => {
    if (!fileSelected) {
      alert("Please Select The File First");
      return;
    }

    try {
      alert("Please Wait While we update matrices");
      const files = document.getElementById("uploadFile").files;
      const formData = new FormData();
      formData.append("uploadFile", files[0]);

      const response = await fetch(ProjectIp + "/Update_matrices", {
        method: "POST",
        credentials: "include",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const jsonResponse = await response.json();

      if (jsonResponse.status === 1) {
        alert("Matrices Updated");
      } else {
        console.log(jsonResponse);
        alert("Error uploading file");
      }
    } catch (error) {
      console.error("Error during file upload:", error);
      alert("An error occurred during file upload. Please try again later.");
    }
  };

  return (
    <div className="page-container" style={{ backgroundColor: "#ebab44b0" }}>
      <Sidenav />
      <div
        className="page-content"
        style={{ backgroundImage: "url('static/img/bg8.jpg')" }}
      >
        <ul
          className="x-navigation x-navigation-horizontal x-navigation-panel"
          style={{ backgroundColor: "rgba(235, 171, 68, 0.69)" }}
        >
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
            <span style={{ color: "black", fontSize: "32px" }}>Templates</span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>
        <ul className="breadcrumb">
          <li>
            <a href="/home">Home</a>
          </li>
          <li className="active">Mode2</li>
        </ul>
        <div className="page-content-wrap" style={{ height: "90vh" }}>
          <div className="row">
            <div
              style={{ fontSize: "20px", fontWeight: "700", marginTop: "5vh" }}
            >
              <i className="fa fa-info-circle" aria-hidden="true"></i>{" "}
              Configurations
            </div>

            <div
              style={{
                marginTop: "4vh",
                display: "flex",
                justifyContent: "end",
                width: "50vw",
              }}
            >
              {/* <p style={{ marginLeft: "30px", fontWeight: "bold" }}>
                <h3>
                  <strong>Update Cost, Distance Matrices</strong>
                </h3>
              </p> */}
              <button
                style={{ color: "white", marginLeft: "30px" }}
                className="btn btn-danger dropdown-toggle"
                // onClick={() => exportToExcel4()}
              >
                <i className="fa fa-bars"></i>
                Import Data
              </button>
            </div>

            <form
              action=""
              encType="multipart/form-data"
              id="uploadForm"
              className="form-horizontal"
              style={{ marginTop: "5vh" }}
            >
              <div
                className="col-md-6"
                style={{ marginTop: "15px", marginLeft: "30px" }}
              >
                <div className="form-group">
                  <div className="col-md-9">
                    <div className="input-group">
                      <span
                        className="input-group-addon"
                        style={{
                          backgroundColor: "rgba(235, 171, 68, 0.69)",
                        }}
                      >
                        <span className="fa fa-info" />
                      </span>

                      <input
                        type="file"
                        className="form-control"
                        onChange={handleFileChange}
                        id="uploadFile"
                        name="uploadFile"
                        defaultValue=""
                        required
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-md-3">
                <img
                  className="upload_class"
                  src={background1}
                  id="uploadConfig"
                  onClick={handleUploadConfig}
                  disabled={!fileSelected}
                  style={{ cursor: "pointer", width: "12%" }}
                />
                <div style={{ marginTop: "0px", marginLeft: "2px" }}>
                  Update
                </div>
                <br />
                <br />
                <br />
              </div>
            </form>
          </div>
          <div
            className="wrap__toggle"
            style={{
              textAlign: "center",
              borderStyle: "solid",
              borderColor: "#ebab44b0",
              marginTop: "10vh",
            }}
          >
            <div className="wrap__toggle--bluetooth">
              <span style={{ textAlign: "center", fontWeight: "bold" }}>
                Generate Optimized Plan
              </span>
            </div>
            <div className="wrap__toggle--toggler">
              <label htmlFor="toggle">
                <input
                  type="checkbox"
                  className="checkBox"
                  id="toggle"
                  // onChange={handleSolveRoutePlan}
                />
                <span></span>
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Template;
