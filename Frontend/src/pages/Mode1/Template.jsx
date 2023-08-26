import React, {  useState } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import background1 from "./../../assets/update1.png";

function Template() {
  const ProjectIp = "http://localhost:5000";
  const [Monthly_Template_M1, set_Monthly_Template_M1] = useState(null);
  const [Daily_Template_S1, set_Daily_Template_S1] = useState(null);
  const [Daily_Template_S2, set_Daily_Template_S2] = useState(null);
  const [Add_matrices, set_Add_matrices] = useState(null);
  const [add_state, setAddstate] = useState("");
  const [add_railhead, setAddRailhead] = useState("");
  const [remove_state, setRemovestate] = useState("");
  const [remove_railhead, setRemoveRailhead] = useState("");
  const [subOptions, setSubOptions] = useState([]);
  const [fileSelected, setFileSelected] = useState(false);

  const handleFileChange = (event) => {
    setFileSelected(event.target.files.length > 0);
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

  const fetchReservationId_Monthly_Template_M1 = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Monthly_Template_M1", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Monthly_Template_M1 = data;
        set_Monthly_Template_M1(fetched_Monthly_Template_M1);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const fetchReservationId_Daily_Template_S1 = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Daily_Template_S1", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Daily_Template_S1 = data;
        set_Daily_Template_S1(fetched_Daily_Template_S1);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const fetchReservationId_Daily_Template_S2 = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Daily_Template_S2", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Daily_Template_S2 = data;
        set_Daily_Template_S2(fetched_Daily_Template_S2);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const Add_TO_Matrices = () => {
    var form = new FormData();
    fetch(ProjectIp + "/Download_Template_to_add", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Add_matrices = data;
        set_Add_matrices(fetched_Add_matrices);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const exportToExcel1 = () => {
    fetchReservationId_Monthly_Template_M1();
    if (Monthly_Template_M1 == null) {
      window.alert("Fetching Result, Please Wait");
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Monthly_Template_M1).forEach(([column, data]) => {
        const parsedData = JSON.parse(data);
        const worksheet = XLSX.utils.json_to_sheet(parsedData);
        XLSX.utils.book_append_sheet(workbook, worksheet, column);
      });
      const excelBuffer = XLSX.write(workbook, {
        type: "array",
        bookType: "xlsx",
      });
      const excelBlob = new Blob([excelBuffer], {
        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      });
      saveAs(excelBlob, "Monthly_Template_M1.xlsx");
    }
  };

  const exportToExcel2 = () => {
    fetchReservationId_Daily_Template_S1();
    if (Daily_Template_S1 == null) {
      window.alert("Fetching Result, Please Wait");
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Daily_Template_S1).forEach(([column, data]) => {
        const parsedData = JSON.parse(data);
        const worksheet = XLSX.utils.json_to_sheet(parsedData);
        XLSX.utils.book_append_sheet(workbook, worksheet, column);
      });
      const excelBuffer = XLSX.write(workbook, {
        type: "array",
        bookType: "xlsx",
      });
      const excelBlob = new Blob([excelBuffer], {
        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      });
      saveAs(excelBlob, "Daily_Template_S1.xlsx");
    }
  };

  const exportToExcel3 = () => {
    fetchReservationId_Daily_Template_S2();
    if (Daily_Template_S2 == null) {
      window.alert("Fetching Result, Please Wait");
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Daily_Template_S2).forEach(([column, data]) => {
        const parsedData = JSON.parse(data);
        const worksheet = XLSX.utils.json_to_sheet(parsedData);
        XLSX.utils.book_append_sheet(workbook, worksheet, column);
      });
      const excelBuffer = XLSX.write(workbook, {
        type: "array",
        bookType: "xlsx",
      });
      const excelBlob = new Blob([excelBuffer], {
        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      });
      saveAs(excelBlob, "Daily_Template_s2.xlsx");
    }
  };

  const exportToExcel4 = () => {
    Add_TO_Matrices();
    if (Add_matrices == null) {
      window.alert("Preaparing Sheet, Please Wait");
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Add_matrices).forEach(([column, data]) => {
        const parsedData = JSON.parse(data);
        const worksheet = XLSX.utils.json_to_sheet(parsedData);
        XLSX.utils.book_append_sheet(workbook, worksheet, column);
      });
      const excelBuffer = XLSX.write(workbook, {
        type: "array",
        bookType: "xlsx",
      });
      const excelBlob = new Blob([excelBuffer], {
        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      });
      saveAs(excelBlob, "Matrices.xlsx");
    }
  };

  const handleDropdownChange = async (e) => {
    const selectedValue = e.target.value;
    setRemovestate(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);

    const workbook = XLSX.read(data, { type: "array" });

    // Assuming the Excel file has only one sheet
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];

    // Parse the sheet data into JSON format
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [{ value: "", label: "Please select Railhead" }];
    for (let i = 0; i < jsonData.length; i++) {
      if (jsonData[i][1] == selectedValue) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));

    setSubOptions(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions(dropdownOptions);
  };

  const addRailhead = async () => {
    console.log(add_state, add_railhead);
    const payload = {
      state: add_state,
      railhead: add_railhead,
    };
    try {
      const response = await fetch(ProjectIp + "/Add_Railhead", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      // Handle the response here, such as checking status or processing the result
      if (response.ok) {
        alert("Railhead Added");
        const data = await response.json();
        console.log("Response data:", data);
        // Perform additional actions based on the response data
      } else {
        console.error("Failed to add railhead:", response.statusText);
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  const removeRailhead = async () => {
    console.log(remove_state, remove_railhead);
    const payload = {
      state: remove_state,
      railhead: remove_railhead,
    };
    try {
      const response = await fetch(ProjectIp + "/Remove_Railhead", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      // Handle the response here, such as checking status or processing the result
      if (response.ok) {
        alert("Railhead Removed");
        const data = await response.json();
        console.log("Response data:", data);
        // Perform additional actions based on the response data
      } else {
        console.error("Failed to add railhead:", response.statusText);
      }
    } catch (error) {
      console.error("An error occurred:", error);
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
          <li className="active">Template</li>
        </ul>
        <div className="page-content-wrap">
          <p style={{ marginLeft: "30px", fontWeight: "bold" }}>
            <h3>
              <strong>Download Updated Template</strong>
            </h3>
          </p>
          <div className="row">
            <div className="col-md-12">
              <div className="col-md-4">
                <div style={{ display: "flex" }}>
                  <button
                    style={{ color: "white", marginLeft: "15px" }}
                    className="btn btn-danger dropdown-toggle"
                    onClick={() => exportToExcel1()}
                  >
                    <i className="fa fa-bars"></i>
                    Download Monthly Template
                  </button>
                  {/* <button
                    style={{ color: "white", marginLeft: "100px" }}
                    className="btn btn-danger dropdown-toggle"
                    onClick={() => exportToExcel2()}
                  >
                    <i className="fa fa-bars"></i>
                    Download Daily Template of Scenario 1
                  </button> */}
                  <button
                    style={{ color: "white", marginLeft: "100px" }}
                    className="btn btn-danger dropdown-toggle"
                    onClick={() => exportToExcel3()}
                  >
                    <i className="fa fa-bars"></i>
                    Download Daily Template of Scenario 2
                  </button>
                </div>
              </div>
            </div>
            <br />
            <br />
            <br />

            <div>
              <h3 style={{ marginLeft: "80px" }}>Add a new Railhead</h3>
              <label style={{ width: "100vw", marginLeft: "100px" }}>
                <strong
                  style={{
                    fontSize: "16px",
                    marginLeft: "15px",
                    width: "400px",
                  }}
                >
                  Select the state to which the railhead belong to
                </strong>
                <select
                  style={{
                    width: "200px",
                    padding: "5px",
                    marginLeft: "100px",
                  }}
                  id="deficit_state"
                  value={add_state}
                  onChange={(e) => setAddstate(e.target.value)}
                >
                  <option value="default">Select State</option>
                  <option value="Andhra Pradesh">Andhra Pradesh</option>
                  <option value="Bihar">Bihar</option>
                  <option value="Chattisgarh">Chattisgarh</option>
                  <option value="Goa">Goa</option>
                  <option value="Gujarat">Gujarat</option>
                  <option value="Haryana">Haryana</option>
                  <option value="Jammu & Kashmir">Jammu & Kashmir</option>
                  <option value="Jharkhand">Jharkhand</option>
                  <option value="Karnataka">Karnataka</option>
                  <option value="Kerala">Kerala</option>
                  <option value="MP">Madhya Pradesh</option>
                  <option value="Maharashtra">Maharashtra</option>
                  <option value="NE">North East</option>
                  <option value="Odisha">Odisha</option>
                  <option value="Punjab">Punjab</option>
                  <option value="Rajasthan">Rajasthan</option>
                  <option value="Tamil Nadu">Tamil Nadu</option>
                  <option value="Telangana">Telangana</option>
                  <option value="UP">Uttar Pradesh</option>
                  <option value="Uttarakhand">Uttarakhand</option>
                  <option value="West Bengal">West Bengal</option>
                </select>
              </label>
              <br />
              <label
                style={{
                  width: "100vw",
                  marginTop: "5px",
                  marginLeft: "100px",
                }}
              >
                <strong
                  style={{
                    fontSize: "16px",
                    marginLeft: "15px",
                    width: "400px",
                  }}
                >
                  Enter the railhead you want to add
                </strong>
                <input
                  type="text"
                  value={add_railhead}
                  onChange={(e) => setAddRailhead(e.target.value)}
                  style={{
                    width: "200px",
                    padding: "5px",
                    marginLeft: "195px",
                  }}
                />
              </label>
            </div>

            <div
              style={{
                padding: "3px",
                margin: "2px",
                width: "80px",
                background: "orange",
                textAlign: "center",
                marginLeft: "400px",
                cursor: "pointer",
                borderRadius: "5px",
              }}
              onClick={addRailhead}
            >
              <p style={{ textAlign: "center", marginTop: "10px" }}>Add</p>
            </div>
            <div>
              <h3 style={{ marginLeft: "80px", marginTop: "40px" }}>
                Remove an existing Railhead
              </h3>
              <label style={{ width: "100vw", marginLeft: "100px" }}>
                <strong
                  style={{
                    fontSize: "16px",
                    marginLeft: "15px",
                    width: "400px",
                  }}
                >
                  Select the state to which the railhead belong to
                </strong>
                <select
                  style={{
                    width: "200px",
                    padding: "5px",
                    marginLeft: "100px",
                  }}
                  id="deficit_state"
                  value={remove_state}
                  onChange={handleDropdownChange}
                >
                  <option value="default">Select State</option>
                  <option value="Andhra Pradesh">Andhra Pradesh</option>
                  <option value="Bihar">Bihar</option>
                  <option value="Chattisgarh">Chattisgarh</option>
                  <option value="Goa">Goa</option>
                  <option value="Gujarat">Gujarat</option>
                  <option value="Haryana">Haryana</option>
                  <option value="Jammu & Kashmir">Jammu & Kashmir</option>
                  <option value="Jharkhand">Jharkhand</option>
                  <option value="Karnataka">Karnataka</option>
                  <option value="Kerala">Kerala</option>
                  <option value="MP">Madhya Pradesh</option>
                  <option value="Maharashtra">Maharashtra</option>
                  <option value="NE">North East</option>
                  <option value="Odisha">Odisha</option>
                  <option value="Punjab">Punjab</option>
                  <option value="Rajasthan">Rajasthan</option>
                  <option value="Tamil Nadu">Tamil Nadu</option>
                  <option value="Telangana">Telangana</option>
                  <option value="UP">Uttar Pradesh</option>
                  <option value="Uttarakhand">Uttarakhand</option>
                  <option value="West Bengal">West Bengal</option>
                </select>
              </label>
              <br />
              <label
                style={{
                  width: "100vw",
                  marginTop: "5px",
                  marginLeft: "100px",
                }}
              >
                <strong
                  style={{
                    fontSize: "16px",
                    marginLeft: "15px",
                    width: "400px",
                  }}
                >
                  Select the railhead you want to remove
                </strong>
                <select
                  id="origin_railhead"
                  style={{
                    width: "200px",
                    padding: "5px",
                    marginLeft: "162px",
                  }}
                  onChange={(e) => setRemoveRailhead(e.target.value)}
                  value={remove_railhead}
                >
                  {subOptions.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </label>
            </div>
            <div
              style={{
                padding: "3px",
                margin: "2px",
                width: "80px",
                background: "orange",
                textAlign: "center",
                marginLeft: "400px",
                cursor: "pointer",
                marginTop: "5px",
                borderRadius: "5px",
              }}
              onClick={removeRailhead}
            >
              <p style={{ textAlign: "center", marginTop: "10px" }}>Remove</p>
            </div>
            <br />
            <br />

            <div>
              <p style={{ marginLeft: "30px", fontWeight: "bold" }}>
                <h3>
                  <strong>Update Cost, Distance Matrices</strong>
                </h3>
              </p>
              <button
                style={{ color: "white", marginLeft: "30px" }}
                className="btn btn-danger dropdown-toggle"
                onClick={() => exportToExcel4()}
              >
                <i className="fa fa-bars"></i>
                Download Matrix to update data
              </button>
            </div>

            <form
              action=""
              encType="multipart/form-data"
              id="uploadForm"
              className="form-horizontal"
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
                        required=""
                      />
                    </div>
                    <span className="help-block" style={{ color: "black" }}>
                      Choose updated matrix
                    </span>
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
                  style={{ cursor: "pointer" }}
                />
                <div style={{ marginTop: "0px", marginLeft: "8px" }}>Update</div>
                <br />
                <br />
                <br />
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Template;
