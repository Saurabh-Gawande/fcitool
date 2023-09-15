import React, { useRef, useState, useEffect } from "react";
import Sidenav from "./sidenav_M02";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import config from "../../config";

// Updated_railhead_list
function Monthly_Solution_M02(props) {
  useEffect(() => {
    const inject = document.createElement("script");
    inject.innerHTML = `
    var fd = new FormData();
    var obj = null;

    $("#uploadConfig").click(function(){   
      var fd = new FormData();
      var files = $('#uploadFile')[0].files;
      if(files.length > 0 ){
          fd.append('uploadFile_M02',files[0]);
  
          $.ajax({
              url: projectIp + "/uploadConfigFile_M02",
              xhrFields: { withCredentials: true },
              type: 'post',
              data: fd,
              contentType: false,
              processData: false,
              success: function(response){
                  if(response != 0){
                      console.log(response);
                      var obj = JSON.parse(response);
                      if(obj["status"]==1){
                              alert("File Uploaded");
                          }
                      }
                  }
              });
          }
          else{
              alert("Please Select The File First");
          }
  });`;
    document.body.appendChild(inject);
    return () => {
      document.body.removeChild(inject);
    };
  });

  const [r_s, setr_s] = useState("");
  const [r_d, setr_d] = useState("");
  const [selectedOption, setSelectedOption] = useState("default");
  const [subOptions, setSubOptions] = useState([]);
  const [selectedOption2, setSelectedOption2] = useState("default");
  const [subOptions2, setSubOptions2] = useState([]);
  const buttonRef = useRef(null);

  const handleSolve = async () => {
    alert("This action will take time, click OK to continue.");
    buttonRef.current.innerText = "Solving..";
    const payload = {
      r_s: r_s,
      r_d: r_d,
      selectedOption: selectedOption,
      selectedRailheadOption: document.getElementById("origin_railhead").value,
      selectedOption2: selectedOption2,
      selectedRailheadOption2:
        document.getElementById("deficit_railhead").value,
    };

    try {
      const response = await fetch(
        config.serverUrl + "/Monthly_Solution_M02",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }
      );

      if (response.ok) {
        buttonRef.current.innerText = "Solved";
        alert("Solution Done!, Now you can download results");
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } catch (error) {
      console.error("Error sending inputs:", error);
    }
  };

  const [cost, setCost] = useState(null);
  const [Total_result, set_Total_Result] = useState(null);
  // const [Relevant_result, set_Relevant_Result] = useState(null);

  const fetchReservationId_cost = () => {
    var form = new FormData();
    const projectIp = "http://207.180.218.55:5000/";
    fetch(projectIp + "/readPickle", {
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
    const projectIp = "http://207.180.218.55:5000/";
    fetch(projectIp + "/read_Result_M02", {
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
  // const fetchReservationId_Revelant_result = () => {
  //   var form = new FormData();
  //   const projectIp = "http://207.180.218.55:5000/";
  //   fetch(projectIp + "/read_Relevant_Result", {
  //     method: "POST",
  //     credentials: "include",
  //     body: form,
  //   })
  //     .then((response) => response.json())
  //     .then((data) => {
  //       const fetched_Relevant_Result = data;
  //       set_Relevant_Result(fetched_Relevant_Result);
  //     })
  //     .catch((error) => {
  //       console.error("Error:", error);
  //     });
  // };

  const exportToExcel1 = () => {
    fetchReservationId_Total_result();
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

  // const exportToExcel2 = () => {
  //   fetchReservationId_Revelant_result();
  //   if (Relevant_result == null) {
  //     window.alert("Fetching Result, Please Wait");
  //   } else {
  //     const workbook = XLSX.utils.book_new();
  //     Object.entries(Relevant_result).forEach(([column, data]) => {
  //       const parsedData = JSON.parse(data);
  //       const worksheet = XLSX.utils.json_to_sheet(parsedData);
  //       XLSX.utils.book_append_sheet(workbook, worksheet, column);
  //     });
  //     const excelBuffer = XLSX.write(workbook, {
  //       type: "array",
  //       bookType: "xlsx",
  //     });
  //     const excelBlob = new Blob([excelBuffer], {
  //       type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
  //     });
  //     saveAs(excelBlob, "Movement_results.xlsx");
  //   }
  // };

  const handleDropdownChange = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);

    const workbook = XLSX.read(data, { type: "array" });

    // Assuming the Excel file has only one sheet
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];

    // Parse the sheet data into JSON format
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
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

  const handleDropdownChange2 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption2(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);

    const workbook = XLSX.read(data, { type: "array" });

    // Assuming the Excel file has only one sheet
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];

    // Parse the sheet data into JSON format
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    for (let i = 0; i < jsonData.length; i++) {
      if (jsonData[i][1] == selectedValue) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));

    setSubOptions2(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions2(dropdownOptions);
  };

  fetchReservationId_cost();

  return (
    <div className="page-container" style={{ backgroundColor: "#00BFBF" }}>
      <Sidenav />
      <div className="page-content">
        <ul className="x-navigation x-navigation-horizontal x-navigation-panel">
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
            <span style={{ color: "white", fontSize: "32px" }}>
              MONTHLY PLAN
            </span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>

        <ul className="breadcrumb">
          <li>
            <a href="/home">Home</a>
          </li>
          <li className="active">Upload File</li>
        </ul>

        <div className="page-content-wrap">
          <div className="row">
            <div className="col-md-12">
              <br />
            
              <div className="row" style={{ marginLeft: "15px" }}>
                <form
                  action=""
                  encType="multipart/form-data"
                  id="uploadForm"
                  className="form-horizontal"
                >
                  <div className="col-md-6">
                    <div className="form-group">
                      <div className="col-md-9">
                        <div className="input-group">
                          <span className="input-group-addon">
                            <span className="fa fa-info" />
                          </span>
                          <input
                            type="file"
                            className="form-control"
                            id="uploadFile"
                            name="uploadFile"
                            defaultValue=""
                            required=""
                          />
                        </div>
                        <span className="help-block" style={{ color: "white" }}>
                          Choose Data Template
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <input
                      style={{ marginLeft: "60px" }}
                      type="button"
                      className="btn btn-primary"
                      defaultValue="Upload Data Template"
                      id="uploadConfig"
                    />
                  </div>
                </form>
              </div>
              <br />
              <div>
                <form>
                  <p style={{ margin: 0, padding: 0 }}>
                    <strong
                      style={{
                        color: "blue",
                        fontSize: "20px",
                        marginLeft: "15px",
                      }}
                    >
                      For Maximum Number of Rakes:
                    </strong>
                  </p>
                  <label>
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Max number of rakes per railhead to be allowed from
                      surplus states (Default Value is 25):
                    </strong>
                    <input
                      type="text"
                      value={r_s}
                      onChange={(e) => setr_s(e.target.value)}
                      style={{ marginLeft: "40px" }}
                    />
                  </label>
                  <br />

                  <label>
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Max number of rakes per railhead to be allowed into
                      deficit states (Default Value is 25):
                    </strong>
                    <input
                      type="text"
                      value={r_d}
                      onChange={(e) => setr_d(e.target.value)}
                      style={{ marginLeft: "53px" }}
                    />
                  </label>
                  <br />
                  <br />
                  <p style={{ margin: 0, padding: 0 }}>
                    <strong
                      style={{
                        color: "blue",
                        fontSize: "20px",
                        marginLeft: "15px",
                      }}
                    >
                      For Route Blocking:
                    </strong>
                  </p>
                  <label htmlFor="origin_state">
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Select Origin State:
                    </strong>
                    <select
                      style={{ marginLeft: "568px", width: "150px" }}
                      id="origin_state"
                      onChange={handleDropdownChange}
                      value={selectedOption}
                    >
                      <option value="default">Select Origin State</option>
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

                  <label htmlFor="origin_railhead">
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Select Origin Railhead:
                    </strong>
                    <select
                      id="origin_railhead"
                      style={{ marginLeft: "540px", width: "150px" }}
                    >
                      {subOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                          {option.label}
                        </option>
                      ))}
                    </select>
                  </label>
                  <br />

                  <label htmlFor="deficit_state">
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Select Destination State:
                    </strong>
                    <select
                      style={{ marginLeft: "528px", width: "150px" }}
                      id="deficit_state"
                      onChange={handleDropdownChange2}
                      value={selectedOption2}
                    >
                      <option value="default">Select Origin State</option>
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

                  <label htmlFor="deficit_railhead">
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Select Destination Railhead:
                    </strong>
                    <select
                      id="deficit_railhead"
                      style={{ marginLeft: "500px", width: "150px" }}
                    >
                      {subOptions2.map((option) => (
                        <option key={option.value} value={option.value}>
                          {option.label}
                        </option>
                      ))}
                    </select>
                  </label>
                  <br />
                </form>

                <button
                  style={{
                    color: "white",
                    backgroundColor: "blue",
                    fontSize: "20px",
                    width: "8%",
                    marginLeft: "728px",
                  }}
                  onClick={handleSolve}
                  ref={buttonRef}
                >
                  Solve
                </button>
              </div>
            </div>
          </div>
          <br />
          <p style={{ display: "inline", marginLeft: "15px" }}>
            <strong style={{ fontSize: "16px" }}>
              Minimum Cost of Transportation is:{" "}
              <span style={{ color: "#FF0509" }}>{cost}</span> Lakhs
            </strong>
          </p>
          <br />
          <div className="panel-heading">
            <h3 className="panel-title"></h3>
            <div className="btn-group pull-left">
              <button
                style={{ color: "white", marginLeft: "2px" }}
                className="btn btn-danger dropdown-toggle"
                onClick={() => exportToExcel1()}
              >
                <i className="fa fa-bars"></i> Download Results
              </button>
            </div>
          </div>
          <br />
          {/* <div className="panel-heading">
            <h3 className="panel-title"></h3>
            <div className="btn-group pull-left">
              <button
                style={{ color: "white", marginLeft: "15px" }}
                className="btn btn-danger dropdown-toggle"
                onClick={() => exportToExcel2()}
              >
                <i className="fa fa-bars"></i> Download Movement List
              </button>
              <br />
              <br />
              <br />
            </div>
          </div> */}
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
        </div>
      </div>
    </div>
  );
}

export default Monthly_Solution_M02;
