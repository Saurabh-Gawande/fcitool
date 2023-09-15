import React, { useState, useEffect } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import background1 from "./../../assets/upload1_.png";
import "./Monthly_sol.css";
import config from "../../config";

function Monthly_Solution() {
  const ProjectIp = config.serverUrl;;
  const [fileSelected, setFileSelected] = useState(false);
  const [r_s, setr_s] = useState("");
  const [r_d, setr_d] = useState("");
  const [TEFD, set_TEFD] = useState("");
  const [solutionSolved, setSolutionSolved] = useState(false);
  const [cost, setCost] = useState(null);
  const [Total_result, set_Total_Result] = useState(null);
  const [Relevant_result, set_Relevant_Result] = useState(null);
  const [excelData, setExcelData] = useState({});
  const [activeSheetName, setActiveSheetName] = useState(null);
  const [sheet, setSheet] = useState(null);
  const [updateExcel, setUpdateExcel] = useState(false);
  const [modifiedExcel, setModifiedExcel] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  //
  const [redState, setRedState] = useState([]);
  const [totalRiceSupplyCheck, setTotalRiceSupplyCheck] = useState("");
  const [demand, setDemand] = useState("");

  const Consistency_Check_frontend = async () => {
    try {
      const response = await fetch(ProjectIp + "/Consistency_Check");
      const data = await response.json();

      console.log(data);
      // Assuming data contains the RedState array and TotalRiceSupplyCheck value
      const redStateData = data["Red State"];
      setRedState(redStateData);
      console.log(redStateData);
    } catch (error) {
      console.error("Error during consistency check:", error);
    }
  };



  const handleFileChange = (event) => {
    setFileSelected(event.target.files.length > 0);
    const files = document.getElementById("uploadFile").files;
    const reader = new FileReader();
    const file = files[0];
    reader.onload = async (e) => {
      const data = new Uint8Array(e.target.result);
      const workbook = XLSX.read(data, { type: "array" });
      console.log(workbook);
      const sheetsData = {};
      workbook.SheetNames.forEach((sheetName) => {
        const worksheet = workbook.Sheets[sheetName];
        sheetsData[sheetName] = XLSX.utils.sheet_to_json(worksheet, {
          header: 1,
        });
      });

      setExcelData(sheetsData);
      setActiveSheetName(workbook.SheetNames[0]);
    };

    reader.readAsArrayBuffer(file);
  };

  const handleUploadConfig = async () => {
    if (!fileSelected) {
      alert("Please Select The File First");
      return;
    }

    try {
      const files = document.getElementById("uploadFile").files;
      const formData = new FormData();
      formData.append("uploadFile", files[0]);

      const response = await fetch(ProjectIp + "/upload_Monthly_File_M01", {
        method: "POST",
        credentials: "include",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const jsonResponse = await response.json();

      if (jsonResponse.status === 1) {
        document.getElementById("console_").style.display = "block";
        document.getElementById("console_").innerHTML +=
          "Template file has been uploaded" + "<br/><br/>";
          
          alert("File Uploaded");
        Consistency_Check_frontend();
       
      } else {
        console.log(jsonResponse);
        alert("Error uploading file");
      }
    } catch (error) {
      console.error("Error during file upload:", error);
      alert("An error occurred during file upload. Please try again later.");
    }
  };

  const handleCellChange = (sheetName, rowIndex, columnIndex, newValue) => {
    const updatedData = { ...excelData };
    updatedData[sheetName][rowIndex][columnIndex] = newValue;
    setExcelData(updatedData);
  };

  const handleSolve = async () => {
    if (isLoading) return; // Prevent additional clicks while loading
    setIsLoading(true);
    document.getElementById("toggle").checked = true;
    document.getElementById("console_").style.display = "block";
    document.getElementById("console_").innerHTML += "Processing..." + "<br/>";
    const payload = {
      r_s: r_s,
      r_d: r_d,
      TEFD: TEFD,
    };
    
    try {
      const response = await fetch(ProjectIp + "/Monthly_Solution", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      fetchReservationId_Revelant_result();
      if (response.ok) {
        alert("Solution Done!, Now you can download results");
        setSolutionSolved(true);
        
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } catch (error) {
      console.error("Error sending inputs:", error);
    } finally {
      setIsLoading(false); // Reset loading state
    }
    document.getElementById("console_").innerHTML +=
      "Solution has been done" + "<br/> " +  "Click on ownload RH to RH Detailed plan" + "<br/>";
      
    document.getElementById("toggle").checked = false;
    
  };

  const fetchReservationId_cost = () => {
    var form = new FormData();
    fetch(ProjectIp + "/Monthly_readPickle", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetchedCost = data["Minimum Cost of Transportation"];
        const formattedCost = parseFloat(fetchedCost).toFixed(1);
        setCost(formattedCost);
        console.log(formattedCost);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
  const fetchReservationId_Total_result = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Monthly_state_table", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Total_Result = data;
        set_Total_Result(fetched_Total_Result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
  const fetchReservationId_Revelant_result = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Relevant_Result", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Relevant_Result = data;
        set_Relevant_Result(fetched_Relevant_Result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const exportToExcel1 = () => {
    fetchReservationId_Total_result();
    console.log(fetchReservationId_Total_result);
    if (Total_result == null) {
      window.alert("Fetching Result, Please Wait");
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Total_result).forEach(([column, data]) => {
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
      saveAs(excelBlob, "All_results.xlsx");
    }
  };

  const update_excel = async () => {
    const response = await fetch(ProjectIp + "/getMonthlyExcelData");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    console.log(workbook);
    const sheetsData = {};
    workbook.SheetNames.forEach((sheetName) => {
      const worksheet = workbook.Sheets[sheetName];
      sheetsData[sheetName] = XLSX.utils.sheet_to_json(worksheet, {
        header: 1,
      });
    });

    setExcelData(sheetsData);
    setActiveSheetName(workbook.SheetNames[0]);
    setUpdateExcel(true);
    document.getElementById("console_").style.display = "block";
    document.getElementById("console_").innerHTML +=
      "Template has been updated" + "<br/>";
  };

  const save_excel = async () => {
    const newWorkbook = XLSX.utils.book_new();
    Object.keys(excelData).forEach((sheetName) => {
      const worksheet = XLSX.utils.json_to_sheet(excelData[sheetName]);
      XLSX.utils.book_append_sheet(newWorkbook, worksheet, sheetName);
    });

    try {
      const response = await fetch(ProjectIp + "/Modify_Monthly_Template_M01", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newWorkbook),
      });
      console.log(newWorkbook);
      if (response.ok) {
        console.log("Data sent to backend successfully");
        
      } else {
        console.error("Failed to send data to backend");
      }
    } catch (error) {
      console.error("Error sending data:", error);
    }
    document.getElementById("console_").style.display = "block";
    document.getElementById("console_").innerHTML +=
      "Template has been updated" + "<br/><br/>";
    setUpdateExcel(false);
  };

  // Function to send JSON data to the backend
  // const send_excel = async () => {
  //   save_excel();
  //   try {
  //     const response = await fetch(ProjectIp + '/Modify_Monthly_Template_M01', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify(modifiedExcel),
  //     });
  //     // console.log(modifiedExcel)

  //     if (response.ok) {
  //       console.log('Data sent to backend successfully');
  //     } else {
  //       console.error('Failed to send data to backend');
  //     }
  //   } catch (error) {
  //     console.error('Error sending data:', error);
  //   }
  // };

  const exportToExcel2 = async () => {
    if (Relevant_result ===null) {
      window.alert("Fetching Result, Please Wait");
      fetchReservationId_Revelant_result();
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Relevant_result).forEach(([column, data]) => {
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
      saveAs(excelBlob, "Monthly_Movement_results.xlsx");
    }
  };
  // fetchReservationId_cost();

  return (
    <div className="page-container" style={{ backgroundColor: "#ebab44b0" }}>
      <Sidenav />
      <div
        className="page-content"
        style={{
          display: "flex",
          backgroundImage: "url('static/img/bg8.jpg')",
        }}
      >
        <div>
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
              <span style={{ color: "black", fontSize: "32px" }}>
                Optimized Monthly Plan
              </span>
              <a className="x-navigation-control"></a>
            </li>
          </ul>

          <ul className="breadcrumb">
            <li>
              <a href="/home">Home</a>
            </li>
            <li className="active">Monthly plan</li>
          </ul>

          <div className="page-content-wrap">
            <div className="row">
              <div className="col-md-12">
                <br />
                <div className="row" style={{ marginLeft: "15px" }}>
                  <div style={{ fontSize: "20px", fontWeight: "700" }}>
                    <i className="fa fa-file-excel-o" aria-hidden="true"></i>{" "}
                    Template
                  </div>
                  <form
                    action=""
                    encType="multipart/form-data"
                    id="uploadForm"
                    className="form-horizontal"
                  >
                    <div
                      className="col-md-6"
                      style={{ marginTop: "15px", marginLeft: "50px" }}
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
                              id="uploadFile"
                              name="uploadFile"
                              onChange={handleFileChange}
                              defaultValue=""
                              required=""
                            />
                          </div>
                          <span
                            className="help-block"
                            style={{ color: "black" }}
                          >
                            Choose Data Template
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
                      />
                      <div style={{ marginTop: "-25px" }}>Click here</div>
                    </div>
                  </form>
                </div>
                <br />
                <br />
                <div style={{ display: "flex", marginLeft: "300px" }}>
                  {/* {fileSelected && ( */}
                  <div style={{ marginTop: "-20px" }}>
                    <button
                      style={{ padding: "5px" }}
                      onClick={() => update_excel()}
                    >
                      Update Template
                    </button>
                  </div>
                  {/* )} */}
                  {updateExcel && (
                    <div style={{ marginLeft: "220px", marginTop: "-20px" }}>
                      <button
                        style={{ padding: "5px" }}
                        onClick={() => save_excel()}
                      >
                        Save changes
                      </button>
                    </div>
                  )}
                </div>
                {activeSheetName &&
                  updateExcel &&
                  excelData[activeSheetName] && (
                    <div style={{ marginLeft: "20%" }}>
                      <select
                        onChange={(e) => setActiveSheetName(e.target.value)}
                        value={activeSheetName}
                        style={{
                          margin: "10px",
                          padding: "3px",
                          marginLeft: "20%",
                        }}
                      >
                        {Object.keys(excelData).map((sheetName) => (
                          <option key={sheetName} value={sheetName}>
                            {sheetName}
                          </option>
                        ))}
                      </select>
                      <table>
                        <tbody>
                          {excelData[activeSheetName].map((row, rowIndex) => (
                            <tr key={rowIndex}>
                              {row.map((cellValue, columnIndex) => (
                                <td key={columnIndex}>
                                  <input
                                    type="text"
                                    value={cellValue}
                                    onChange={(e) =>
                                      handleCellChange(
                                        activeSheetName,
                                        rowIndex,
                                        columnIndex,
                                        e.target.value
                                      )
                                    }
                                  />
                                </td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                <div style={{ marginLeft: "15px" }}>
                  <div style={{ fontSize: "20px", fontWeight: "700" }}>
                    <i className="fa fa-info-circle" aria-hidden="true"></i>{" "}
                    Configurations
                  </div>
                  <br />
                  <form style={{ marginLeft: "50px" }}>
                    <label>
                      <strong
                        style={{
                          fontSize: "20px",
                          marginLeft: "15px",
                          color: "#9d0921",
                        }}
                      >
                        Select Matrix System
                      </strong>
                      <select
                        value={TEFD}
                        onChange={(e) => {
                          set_TEFD(e.target.value);
                          document.getElementById("console_").style.display =
                            "block";
                          document.getElementById("console_").innerHTML +=
                            "You have selected the matrix system as " +
                            e.target.value +
                            "<br/><br/>";
                        }}
                        style={{ marginLeft: "547px" }}
                      >
                        <option value="">Select Matrix System</option>
                        <option value="NON-TEFD">Non-TEFD</option>
                        <option value="TEFD">TEFD</option>
                        <option value="Non-TEFD+TC">Non-TEFD + TC</option>
                        <option value="TEFD+TC">TEFD + TC</option>
                      </select>
                    </label>
                    <br />
                    <br />
                    <p style={{ margin: 0, padding: 0 }}>
                      <strong
                        style={{
                          color: "#9d0921",
                          fontSize: "20px",
                          marginLeft: "15px",
                          fontFamily: "Segoe UI",
                        }}
                      >
                        For Maximum Number of Rakes
                      </strong>
                    </p>
                    <label style={{ marginTop: "10px" }}>
                      <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                        Max number of rakes per railhead to be allowed from
                        surplus states (Default Value is 25)
                      </strong>
                      <input
                        type="number"
                        value={r_s}
                        onChange={(e) => {
                          setr_s(e.target.value);
                        }}
                        style={{ marginLeft: "40px" }}
                      />
                    </label>
                    <br />
                    <label>
                      <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                        Max number of rakes per railhead to be allowed into
                        deficit states (Default Value is 25)
                      </strong>
                      <input
                        type="number"
                        value={r_d}
                        onChange={(e) => setr_d(e.target.value)}
                        style={{ marginLeft: "53px" }}
                      />
                    </label>
                    <br />
                    <br />
                    <br />
                    <br />
                    <br />
                  </form>
                  <div style={{ fontSize: "20px", fontWeight: "700" }}>
                    <i className="fa fa-list-alt" aria-hidden="true"></i>{" "}
                    Optimal Plan
                  </div>
                  <div
                    className="wrap__toggle"
                    style={{
                      textAlign: "center",
                      borderStyle: "solid",
                      borderColor: "#ebab44b0",
                    }}
                    onClick={handleSolve}
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
                          onClick={handleSolve}
                        />
                        <span></span>
                      </label>
                    </div>
                  </div>
                  <br />

                  <br />
                  {solutionSolved && (
                    <div>
                      <p style={{ display: "inline", marginLeft: "18px" }}>
                        <strong style={{ fontSize: "16px" }}>
                          Optimal Cost of Transportation is INR{" "}
                          <span style={{ color: "#FF0509" }}>{cost}</span> Lakhs
                        </strong>
                      </p>
                    </div>
                  )}
                  <br />
                  {solutionSolved && (
                    <div>
                      <button
                        style={{ color: "white", marginLeft: "15px" }}
                        className="btn btn-danger dropdown-toggle"
                        onClick={() => exportToExcel2()}
                        
                      >
                        <i className="fa fa-bars"></i> Download Railhead To
                        Railhead Detailed Plan
                      </button>
                      <br />
                      <br />
                      {/* <button
                      style={{ color: "white", marginLeft: "15px" }}
                      className="btn btn-danger dropdown-toggle"
                      onClick={() => exportToExcel1()}
                    >
                      <i className="fa fa-bars"></i> Download State to State
                      Detailed Plan
                    </button> */}
                    </div>
                  )}
                  <br />
                  <br />
                  <br />
                  <br />
                  <br />
                </div>
              </div>
            </div>
            <br />
            <br />
            <br />
          </div>
        </div>
        <div style={{ backgroundColor: "#ebab44b0", width: "20%" }}>
          <br />
          <div>
            <div class="progress yellow">
              <span class="progress-left">
                <span class="progress-bar"></span>
              </span>
              <span class="progress-right">
                <span class="progress-bar"></span>
              </span>
              <div class="progress-value">Steps</div>
            </div>
          </div>
          <span style={{ color: "black", fontSize: "32px", marginLeft: "5%" }}>
            Progress Bar
          </span>
          <div>
            {/* Rendering RedState */}
            {redState.length > 0 && (
              <div>
                <h2>All States:</h2>
                <ul>
                  {redState.map((state, index) => (
                    <li key={index}>{state}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Rendering Rice Supply Check */}
            {totalRiceSupplyCheck !== "" && (
              <div>
                <h2>Rice Supply Check:</h2>
                {parseFloat(totalRiceSupplyCheck) < parseFloat(demand) ? (
                  <p>Supply of Rice is less than Demand</p>
                ) : (
                  <p>Supply of Rice is sufficient</p>
                )}
              </div>
            )}
          </div>
          <div
            style={{
              margin: "10px",
              marginLeft: "5%",
              width: "90%",
              border: "2px dashed black",
              paddingTop: "10px",
              paddingLeft: "10px",
              paddingRight: "10px",
              display: "none",
              paddingBottom: "-10px",
            }}
            id="console_"
          ></div>
        </div>
      </div>
    </div>
  );
}

export default Monthly_Solution;
