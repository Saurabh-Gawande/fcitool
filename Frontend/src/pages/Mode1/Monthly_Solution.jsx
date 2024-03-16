import React, { useEffect, useState } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import background1 from "./../../assets/upload1_.png";
import "./Monthly_sol.css";
import config from "../../config";

function Monthly_Solution() {
  const ProjectIp = config.serverUrl;
  const [fileSelected, setFileSelected] = useState(false);
  const [importedFile1, setImportedFile1] = useState(null);
  const [importedFile2, setImportedFile2] = useState(null);
  const [TEFD, set_TEFD] = useState("");
  const [type, set_type] = useState("");
  const [solutionSolved, setSolutionSolved] = useState(false);
  const [Relevant_result, set_Relevant_Result] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [showMessage, setShowMessage] = useState(false);
  const [Bajra, setBajra] = useState(false);
  const [Jowar, setJowar] = useState(false);
  const [Maize, setMaize] = useState(false);
  const [Ragi, setRagi] = useState(false);
  const [Misc1, setMisc1] = useState(false);
  const [Misc2, setMisc2] = useState(false);
  const [RRA, setRRA] = useState(false);
  const [Wheat_faq, setWheat_faq] = useState(false);
  const [Wheat_urs, setWheat_urs] = useState(false);
  const [frk_br, setFrk_br] = useState(false);
  const [frk_rra, setFrk_rra] = useState(false);
  const [excelfiledata, setExcelFileData] = useState();

  const handleFileChange = (e) => {
    setFileSelected(e.target.files[0]);
  };

  //for import the data 
  const ImportData = () => {
    fetch(
      "https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/MonthlyPlanforTool?status=Inward"
    )
      .then((res) => res.blob())
      .then(async (blob) => {
        const excelFile = new File([blob], "MonthlyPlanforTool.xlsx", {
          type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        });
        setImportedFile1(excelFile);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });

    fetch(
      "https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/MonthlyPlanforTool?status=Outward"
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
    set_type("Imported");
  };

  useEffect(() => {
    if (importedFile1) {
      const uploadFile = async () => {
        try {
          const formData1 = new FormData();
          formData1.append("uploadFile1", importedFile1);

          const response1 = await fetch(
            ProjectIp + "/Import_Monthly_File_Invard",
            {
              method: "POST",
              credentials: "include",
              body: formData1,
            }
          );

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

          const response2 = await fetch(
            ProjectIp + "/Import_Monthly_File_Outward",
            {
              method: "POST",
              credentials: "include",
              body: formData2,
            }
          );

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

  // for uploading the data to the server
  const handleUploadConfig = async () => {
    if (!fileSelected) {
      alert("Please Select The File First");
      return;
    }
    try {
      set_type("Uploaded");
      const formData = new FormData();
      formData.append("uploadFile", fileSelected);

      const response = await fetch(ProjectIp + "/upload_Monthly_File", {
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
      } else {
        alert("Error uploading file");
      }
    } catch (error) {
      console.error("Error during file upload:", error);
      alert("An error occurred during file upload. Please try again later.");
    }
  };

  // function for solving the monthly planner problem
  const handleSolve = async () => {
    document.getElementById("toggle").checked = true;
    if (isLoading) return;
    setIsLoading(true);
    document.getElementById("console_").style.display = "block";
    document.getElementById("console_").innerHTML += "Processing..." + "<br/>";
    const payload = {
      TEFD: TEFD,
      type: type,
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
      "Solution has been done" +
      "<br/> " +
      "Click on download RH to RH Detailed plan" +
      "<br/>";

    document.getElementById("toggle").checked = false;
  };

  const fetchReservationId_Revelant_result = () => {
    fetch(ProjectIp + "/read_Relevant_Result", {
      method: "GET",
      credentials: "include",
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

  const ExportPlan = () => {
    const relevantData = Relevant_result["RH_RH_tag"];
    fetch(
      "https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/PostMonthlyPlanner",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: relevantData,
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

  const exportToExcel2 = async () => {
    if (Relevant_result === null) {
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

  return (
    <div
      className="page-container"
      style={{ backgroundColor: "#ebab44b0", height: "100vh" }}
    >
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
                <div className="row" style={{ marginLeft: "15px" }}>
                  <div
                    style={{
                      color: "white",
                      display: "flex",
                      width: "42vw",
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
                              required
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
                <div style={{ marginLeft: "15px" }}>
                  {/* <div style={{ fontSize: "20px", fontWeight: "700" }}>
                    <i className="fa fa-info-circle" aria-hidden="true"></i>{" "}
                    Configurations
                  </div> */}
                  <br />
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
                          onChange={handleSolve}
                        />
                        <span></span>
                      </label>
                    </div>
                  </div>
                  <br />
                  <br />
                  {solutionSolved && (
                    <div>
                      <button
                        style={{ color: "black", marginLeft: "15px" }}
                        className="btn btn-success dropdown-toggle"
                        onClick={() => exportToExcel2()}
                      >
                        <i className="fa fa-bars"></i> Download Railhead To
                        Railhead Detailed Plan
                      </button>

                      <button
                        style={{ color: "black", marginLeft: "15px" }}
                        className="btn btn-success dropdown-toggle"
                        onClick={ExportPlan}
                      >
                        <i className="fa fa-bars"></i>
                        Export plan
                      </button>
                    </div>
                  )}
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
        <div style={{ backgroundColor: "#ebab44b0", width: "20%" }}>
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

export default Monthly_Solution;
