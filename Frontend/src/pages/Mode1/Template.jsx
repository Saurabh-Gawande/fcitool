import React, { useState, useEffect } from "react";
import Sidenav from "./sidenav";
import config from "../../config";

function Template() {
  const ProjectIp = config.serverUrl;
  const [fileSelected, setFileSelected] = useState(false);
  const [importedFile1, setImportedFile1] = useState(null);
  const [importedFile2, setImportedFile2] = useState(null);
  const [result, setResult] = useState([]);
  const [senerio, setSenerio] = useState("senerio1");
  const [commodiyCountData, setCommodityCountData] = useState([]);
  const [monthlyDataCollection, setMonthlyDataCollection] = useState([]);
  const [showMessage, setShowMessage] = useState(false);

  const getRowColor = (inward, outward) => {
    if (outward > inward) {
      return "table-success";
    } else if (inward > outward) {
      return "table-danger";
    } else {
      return "";
    }
  };

  const [result1, setResult1] = useState({
    WH_RH_Tag: [
      {
        WarehouseId: "FCI37",
        ConnectedRhcode: "FCP",
        State: "Haryana",
        Commodity: "Wheat(Total)",
        Values: "0.952",
        Type: "WH_RH",
      },
      {
        WarehouseId: "FCI38",
        ConnectedRhcode: "ABC",
        State: "Haryana",
        Commodity: "Wheat(Total)",
        Values: "0.993",
        Type: "WH_RH",
      },
    ],
    RH_WH_Tag: [
      {
        WarehouseId: "FCI37",
        ConnectedRhcode: "PQR",
        State: "Haryana",
        Commodity: "Wheat(Total)",
        Values: "0.952",
        Type: "RH_WH",
      },
      {
        WarehouseId: "FCI31",
        ConnectedRhcode: "XYZ",
        State: "Haryana",
        Commodity: "Wheat(Total)",
        Values: "0.952",
        Type: "RH_WH",
      },
    ],
    RH_RH_Tag: [
      {
        From: "FCP",
        FromState: "Haryana",
        To: "RXL",
        ToState: "Bihar",
        Commodity: "Wheat(Total)",
        Values: "0.952",
        Type: "RH_RH",
      },
    ],
    WH_Wh_Tag: [
      {
        From: "FCI38",
        FromState: "Haryana",
        To: "FCI45",
        ToState: "Bihar",
        Commodity: "Wheat(Total)",
        Values: "0.952",
        Type: "WH_WH",
      },
    ],
  });

  const ExportData = () => {
    fetch(
      "https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/PostMode2MonthlyPlanner",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(result1),
      }
    )
      .then((response) => {
        if (response.ok) {
          window.alert("File uploaded successfully!");
          // setProgress((prev) => [
          //   ...prev,
          //   "Successfully exported the plan to portal",
          // ]);
        } else {
          window.alert("File upload failed. Please try again.");
        }
      })
      .catch((error) => {
        console.error("An error occurred during file upload:", error);
      });
  };

  const ImportData = () => {
    try {
      fetch(
        "https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/Mode2MonthlyPlanforTool?status=Inward"
      )
        .then((res) => res.blob())
        .then(async (blob) => {
          const excelFile = new File([blob], "MonthlyPlanforTool.xlsx", {
            type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          });
          setShowMessage(true);
          setImportedFile1(excelFile);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });

      fetch(
        "https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/Mode2MonthlyPlanforTool?status=Outward"
      )
        .then((res) => res.blob())
        .then(async (blob) => {
          const excelFile = new File([blob], "MonthlyPlanforTool.xlsx", {
            type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          });
          setImportedFile2(excelFile);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });

      fetch(
        "https://test.rakeplanner.callippus.co.uk/api/MonthlyDataCollectionWebApi/GetCommodityCountData/Road"
      )
        .then((res) => res.json())
        .then((data) => setCommodityCountData(data));

      fetch(
        "https://test.rakeplanner.callippus.co.uk/api/MonthlyDataCollectionWebApi/GetAllRegionData/excel/Road"
      )
        .then((res) => res.json())
        .then((data) => setMonthlyDataCollection(data));
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const FetchResultData = () => {
    fetch(ProjectIp + "/daily_planner_data", {
      method: "GET",
      credentials: "include",
      // body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setResult(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  useEffect(() => {
    if (importedFile1) {
      const uploadFile = async () => {
        try {
          const formData1 = new FormData();
          formData1.append("uploadFile1", importedFile1);

          const response1 = await fetch(ProjectIp + "/Import_Mode2_Invard", {
            method: "POST",
            credentials: "include",
            body: formData1,
          });

          if (!response1.ok) {
            throw new Error("Network response was not ok");
          }
        } catch (error) {
          console.error("Error during file upload:", error);
          alert(
            "An error occurred during file upload. Please try again later."
          );
        }
      };
      uploadFile();
    }
  }, [importedFile1]);

  useEffect(() => {
    if (importedFile2) {
      const uploadFile = async () => {
        try {
          const formData2 = new FormData();
          formData2.append("uploadFile2", importedFile2);

          const response2 = await fetch(ProjectIp + "/Import_Mode2_Outward", {
            method: "POST",
            credentials: "include",
            body: formData2,
          });

          if (!response2.ok) {
            throw new Error("Network response was not ok");
          }

          const jsonResponse2 = await response2.json();

          if (jsonResponse2.status === 1) {
            document.getElementById("console_").style.display = "block";
            document.getElementById("console_").innerHTML +=
              "Data imported successfully" + "<br/><br/>";

            alert("Data imported successfully");
          } else {
            alert("Error uploading file");
          }
        } catch (error) {
          console.error("Error during file upload:", error);
          alert(
            "An error occurred during file upload. Please try again later."
          );
        }
      };
      uploadFile();
    }
  }, [importedFile2]);

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
        body: JSON.stringify({
          senerio: senerio,
        }),
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

  return (
    <div
      className="page-container"
      style={{ backgroundColor: "#ebab44b0", minHeight: "100vh" }}
    >
      <Sidenav />
      <div
        className="page-content"
        style={{
          display: "flex",
          backgroundImage: "url('static/img/bg8.jpg')",
          minHeight: "100vh",
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
                Optimized Road Plan
              </span>
              <a className="x-navigation-control"></a>
            </li>
          </ul>

          <ul className="breadcrumb">
            <li>
              <a href="/home">Home</a>
            </li>
            <li className="active">Road plan</li>
          </ul>

          <div className="page-content-wrap">
            <div className="row">
              <br />
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  width: "45vw",
                }}
              ></div>
              <div className="col-md-12">
                <br />
                <div
                  style={{
                    color: "white",
                    display: "flex",
                    width: "62vw",
                    justifyContent: "end",
                    marginBottom: 15,
                  }}
                >
                  <div className="row ml-3">
                    <div className="col-auto">
                      <select
                        className="form-select"
                        id="senerio"
                        onChange={(e) => setSenerio(e.target.value)}
                      >
                        <option value="senerio1">Scenario 1</option>
                        <option value="senerio2">Scenario 2</option>
                        <option value="senerio3">Scenario 3</option>
                        <option value="senerio4">Scenario 4</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div>
                  <div
                    style={{
                      color: "white",
                      display: "flex",
                      width: "62vw",
                      justifyContent: "end",
                    }}
                  >
                    <button
                      className="btn btn-danger dropdown-toggle"
                      onClick={ImportData}
                    >
                      Import data
                    </button>
                  </div>
                </div>
                <br />
                <div style={{ marginLeft: "15px" }}>
                  {showMessage && (
                    <div className="container mt-5">
                      <div className="row">
                        <div className="table-responsive">
                          <table className="table table-sm table-bordered">
                            <thead>
                              <tr>
                                <th>Commodity</th>
                                <th>State</th>
                                <th>Inward</th>
                                <th>Outward</th>
                                <th>Surplus</th>
                              </tr>
                            </thead>
                            <tbody>
                              {commodiyCountData.map((item, index) => (
                                <tr
                                  key={index}
                                  className={getRowColor(
                                    item.inward,
                                    item.outward
                                  )}
                                >
                                  <td>{item.commodity}</td>
                                  <td>{item.state}</td>
                                  <td>{item.inward}</td>
                                  <td>{item.outward}</td>
                                  <td>{item.surplus}</td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                  )}

                  {showMessage && (
                    <div className="container mt-5">
                      <h2>Region Data</h2>
                      <div className="table-responsive">
                        <table className="table table-sm table-bordered">
                          <thead>
                            <tr>
                              <th>State</th>
                              {/* <th>Max Run ID</th> */}
                              <th>Inward Wheat URS</th>
                              <th>Inward Wheat FAQ</th>
                              <th>Inward Wheat Total</th>
                              <th>Inward Rice FRKBR</th>
                              <th>Inward Rice RRA</th>
                              <th>Inward Rice FRKRRA</th>
                              <th>Inward G Total</th>
                              <th>Outward Wheat URS</th>
                              <th>Outward Wheat FAQ</th>
                              <th>Outward Wheat Total</th>
                              <th>Outward Rice FRKBR</th>
                              <th>Outward Rice RRA</th>
                              <th>Outward Rice FRKRRA</th>
                              <th>Outward G Total</th>
                              {/* <th>Created Date</th> */}
                              {/* <th>Last Modified Date</th> */}
                            </tr>
                          </thead>
                          <tbody>
                            {monthlyDataCollection.map((region, index) => (
                              <tr key={index}>
                                <td>{region.state}</td>
                                {/* <td>{region.maxRunId}</td> */}
                                <td>{region.inward_Wheat_URS}</td>
                                <td>{region.inward_Wheat_FAQ}</td>
                                <td>{region.inward_Wheat_Total}</td>
                                <td>{region.inward_Rice_FRKBR}</td>
                                <td>{region.inward_Rice_RRA}</td>
                                <td>{region.inward_Rice_FRKRRA}</td>
                                <td>{region.inward_G_Total}</td>
                                <td>{region.outward_Wheat_URS}</td>
                                <td>{region.outward_Wheat_FAQ}</td>
                                <td>{region.outward_Wheat_Total}</td>
                                <td>{region.outward_Rice_FRKBR}</td>
                                <td>{region.outward_Rice_RRA}</td>
                                <td>{region.outward_Rice_FRKRRA}</td>
                                <td>{region.outward_G_Total}</td>
                                {/* <td>{region.createdDate}</td> */}
                                {/* <td>{region.lastModifiedDate}</td> */}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                  {/* <div style={{ fontSize: "20px", fontWeight: "700" }}>
                  <i className="fa fa-info-circle" aria-hidden="true"></i>{" "}
                  Configurations
                </div> */}
                  {/* <br /> */}
                  {/* <form style={{ marginLeft: "50px" }}>
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
                </form> */}

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
                          onChange={handleSolveRoutePlan}
                        />
                        <span></span>
                      </label>
                    </div>
                  </div>
                  <br />
                  <br />
                  <button onClick={FetchResultData}>Get result</button>
                  <button
                    className="btn btn-danger dropdown-toggle"
                    onClick={ExportData}
                  >
                    Export plan
                  </button>
                  {/* {solutionSolved && (
                    <div>
                      <button
                        style={{ color: "black", marginLeft: "15px" }}
                        className="btn btn-success dropdown-toggle"
                        // onClick={() => exportToExcel2()}
                      >
                        <i className="fa fa-bars"></i> Download Railhead To
                        Railhead Detailed Plan
                      </button>

                      <button
                        style={{ color: "black", marginLeft: "15px" }}
                        className="btn btn-success dropdown-toggle"
                        // onClick={ExportPlan}
                      >
                        <i className="fa fa-bars"></i>
                        Export plan
                      </button>
                    </div>
                  )} */}
                  <br />
                </div>
              </div>
            </div>
            <br />
            {/* {showMessage && (
                        <div
                          style={{
                            marginTop: 15,
                            marginLeft: 20,
                            width: "62vw",
                          }}
                        >
                          {Wheat_urs !== null && Wheat_urs.length > 0 ? (
                            <div>
                              <div>Wheat_urs</div>
                              <table>
                                <thead>
                                  <tr style={{ margin: "auto" }}>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "200px",
                                      }}
                                    >
                                      Sr. No
                                    </th>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "200px",
                                      }}
                                    >
                                      Src RH
                                    </th>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "200px",
                                      }}
                                    >
                                      Src state
                                    </th>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "200px",
                                      }}
                                    >
                                      Dest RH
                                    </th>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "200px",
                                      }}
                                    >
                                      Dest state
                                    </th>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "200px",
                                      }}
                                    >
                                      commodity
                                    </th>
                                    <th
                                      style={{
                                        padding: "10px",
                                        width: "350px",
                                      }}
                                    >
                                      Rakes
                                    </th>
                                  </tr>
                                </thead>
                                <tbody>
                                  {Wheat_urs.map((item, index) => (
                                    <tr key={item["Unnamed: 0"]}>
                                      <td>{index + 1}</td>
                                      <td>{item.From_state}</td>
                                      <td>{item.Bihar}</td>
                                      <td>{item.DestinationRailHead}</td>
                                      <td>{item.DestinationState}</td>
                                      <td>{item.Commodity}</td>
                                      <td>{item.Rakes}</td>
                                    </tr>
                                  ))}
                                </tbody>
                              </table>
                            </div>
                          ) : (
                            <div />
                          )}
                        </div>
                      )} */}
            <br />
          </div>
        </div>
        <div style={{ backgroundColor: "#ebab44b0", width: "29%" }}>
          <br />

          <span style={{ color: "black", fontSize: "32px", marginLeft: "5%" }}>
            Progress Bar
          </span>

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

export default Template;
