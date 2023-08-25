import React, { useRef, useState } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";

function Alternate_Railhead() {
  const ProjectIp = "http://localhost:5000";
  const [rhSource, setRhSource] = useState("");
  const [rhDest, setRhDest] = useState("");
  const [zone, setZone] = useState("");
  // const [n, setN] = useState(0);
  const buttonRef = useRef(null);
  const [data, setData] = useState([]);
  const [selectedOption, setSelectedOption] = useState("default");
  const [subOptions, setSubOptions] = useState([]);
  const [selectedOption2, setSelectedOption2] = useState("default");
  const [subOptions2, setSubOptions2] = useState([]);

  const fetchData = () => {
    fetch(ProjectIp + "/Alternate_Railhead_readPickle")
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error(error));
  };

  const handleSolve = async () => {
    buttonRef.current.innerText = "Solving..";
    const payload = {
      rh_source: rhSource,
      rh_dest: rhDest,
      zone: zone,
      // n: n,
    };
    try {
      const response = await fetch(ProjectIp + "/Alternate_Railhead_Solve", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        buttonRef.current.innerText = "Solve";
        fetchData();
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } catch (error) {
      console.error("Error sending inputs:", error);
    }
  };

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
  const handleSubDropdownChange1 = (e) => {
    setRhDest(e.target.value);
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
    let dropdownOptions = [{ value: "", label: "Please select Railhead" }];
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
  const handleSubDropdownChange2 = (e) => {
    setRhSource(e.target.value);
  };

  return (
    <div className="page-container" style={{ backgroundColor: "#ebab44b0" }}>
      <Sidenav />
      <div
        className="page-content"
        style={{
          backgroundImage: "url('static/img/bg8.jpg')",
          height: "100vh",
        }}
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
            <span style={{ color: "black", fontSize: "32px" }}>
              CHOOSE ALTERNATE RAILHEAD
            </span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>

        <ul className="breadcrumb">
          <li>
            <a href="/home">Home</a>
          </li>
          <li className="active">Input</li>
        </ul>

        <div className="page-content-wrap">
          <div className="row">
            <div className="col-md-12">
              <div>
                <br />
                <br />
                <form>
                  <br />
                  <br />
                  {/* <div style={{ display: "flex", marginLeft: "20px" }}> */}
                    {/* <label htmlFor="origin_state"> */}
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Origin State:
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px", marginLeft: "200px" }}
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
                    </div>
<br/>
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Origin Railhead:
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px", marginLeft: "172px" }}
                        onChange={handleSubDropdownChange2}
                        value={rhSource}
                      >
                        {subOptions2.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    </div>
                    {/* </label> */}
                    <div>
                      
                    </div>
                    <br/>

                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Dsetination State:
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px", marginLeft: "161px" }}
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
                    </div>
                    <br/>
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Destination Railhead:
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px", marginLeft: "136px" }}
                        onChange={handleSubDropdownChange1}
                        value={rhDest}
                      >
                        {subOptions.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    </div>
                    {/* </label> */}
                    <div>
                      <br />
                      <br />
                    </div>

                  {/* </div> */}
                </form>
                <button
                  style={{
                    color: "white",
                    backgroundColor: "blue",
                    fontSize: "20px",
                    width: "8%",
                    marginLeft: "440px",
                  }}
                  onClick={handleSolve}
                  ref={buttonRef}
                >
                  Solve
                </button>
                <div style={{ marginLeft: "15px" }}>
                  <h1>Data Table</h1>
                  <br />
                  {data.length > 0 ? (
                    <table>
                      <thead>
                        <tr>
                          <th>Alternate Railhead</th>
                        </tr>
                      </thead>
                      <tbody>
                        {data.map((item, index) => (
                          <tr key={index}>
                            <td>
                              <strong>{item}</strong>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  ) : (
                    <p>
                      <strong>No data available</strong>
                    </p>
                  )}
                </div>
              </div>
              <br />
              <br />
            </div>
          </div>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
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

export default Alternate_Railhead;
