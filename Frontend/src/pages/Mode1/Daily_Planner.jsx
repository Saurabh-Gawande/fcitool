import React, { useState, useEffect } from "react";
// import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import config from "../../config";
import jsPDF from "jspdf";
import "jspdf-autotable";
import "./Daily_Planner.css";
import Sidenav from "./sidenav";

function Daily_Planner() {
  const ProjectIp = config.serverUrl;
  const portalUrl = config.portalUrl;
  const [solutionSolved, setSolutionSolved] = useState(false);
  const [loading, setLoading] = useState(true);
  const [progress, setProgress] = useState([]);
  const [surplus, setSurplus] = useState([]);
  const [deficit, setDeficit] = useState([]);
  const [surplusInline, setSurplusInline] = useState([]);
  const [deficitInline, setDeficitInline] = useState([]);
  const [fixed_data, setFixeddata] = useState([]);
  const [blocked_data, setBlockeddata] = useState([]);
  const [disableAfterImport, setDisableAfterImport] = useState(false);
  const [nextDayData, setNextDayData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState([]);
  const [showResult, setShowResult] = useState(false);
  const [counts, setCounts] = useState({});

  const exportToExcel = () => {
    if (!result || result.length === 0) {
      window.alert("Fetching Result, Please Wait");
      return;
    }

    const currentDateUTC = new Date();
    const istOffset = 5.5 * 60 * 60 * 1000;
    const currentDateIST = new Date(currentDateUTC.getTime() + istOffset);
    const dateAndTime = currentDateIST
      .toISOString()
      .replace(/[:.]/g, "-")
      .split(".")[0];
    const filenameWithDateTime = `Daily_Movement_Scenario1_${dateAndTime}.xlsx`;

    const workbook = XLSX.utils.book_new();

    // Map the result array to extract required fields for Excel
    const filteredData = result.map((item) => ({
      SourceRailHead: item.SourceRailHead,
      SourceState: item.SourceState,
      DestinationRailHead: item.DestinationRailHead,
      DestinationState: item.DestinationState,
      Commodity: item.Commodity,
      Rakes: item.Rakes,
    }));

    // Define the columns to include in the Excel sheet
    const selectedColumns = [
      "SourceRailHead",
      "SourceState",
      "DestinationRailHead",
      "DestinationState",
      "Commodity",
      "Rakes",
    ];

    // Create the worksheet from the filtered data
    const worksheet = XLSX.utils.json_to_sheet(filteredData, {
      header: selectedColumns,
    });

    // Append the worksheet to the workbook
    XLSX.utils.book_append_sheet(workbook, worksheet, "RH_RH_tags");

    // Convert the workbook to Excel buffer
    const excelBuffer = XLSX.write(workbook, {
      type: "array",
      bookType: "xlsx",
    });

    const excelBlob = new Blob([excelBuffer], {
      type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    });

    saveAs(excelBlob, filenameWithDateTime);

    setProgress((prev) => [
      ...prev,
      "Downloaded Railhead detail Plan in Excel format",
    ]);
  };

  const exportToPDF = () => {
    if (!result || result.length === 0) {
      window.alert("No data to create PDF");
      return;
    }

    const pdfDoc = new jsPDF("p", "mm", "a4");
    const currentDateUTC = new Date();
    const istOffset = 5.5 * 60 * 60 * 1000;
    const currentDateIST = new Date(currentDateUTC.getTime() + istOffset);

    const year = currentDateIST.getFullYear();
    const month = String(currentDateIST.getMonth() + 1).padStart(2, "0");
    const date = String(currentDateIST.getDate()).padStart(2, "0");
    const hours = String(currentDateIST.getHours()).padStart(2, "0");
    const minutes = String(currentDateIST.getMinutes()).padStart(2, "0");
    const seconds = String(currentDateIST.getSeconds()).padStart(2, "0");

    const timestamp = `${year}/${month}/${date} |  Time: ${hours}:${minutes}:${seconds}`;

    pdfDoc.setFontSize(10);
    pdfDoc.text(`Date: ${timestamp}`, 15, 10);

    const headers = [
      "Commodity",
      "SourceState",
      "SourceRailHead",
      "DestinationState",
      "DestinationRailHead",
      "Rakes",
    ];

    const rows = result.map((item) => [
      item.Commodity,
      item.SourceState,
      item.SourceRailHead,
      item.DestinationState,
      item.DestinationRailHead,
      item.Rakes,
    ]);

    pdfDoc.autoTable({
      head: [headers],
      body: rows,
      startY: 20, // Start position of the table
      theme: "striped",
    });

    pdfDoc.save(`Railhead_data_${timestamp}.pdf`);
    setProgress((prev) => [
      ...prev,
      "Downloaded Railhead detail Plan in Pdf format",
    ]);
  };

  const ExpotPlan = async () => {
    try {
      const response = await fetch(
        `${portalUrl}/ToolOptimizerWebApi/PostDailyPlanner`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(result),
        }
      );

      // Check if the response is okay
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      } else {
        alert("Data successfully exported to the portal");
        setProgress((prev) => [
          ...prev,
          "Data successfully exported to the portal",
        ]);
      }
    } catch (error) {
      console.error("An error occurred:", error.message);
      return null;
    }
  };

  const getCounts = (data) => {
    const counts = {};

    const processResponse = (response, type) => {
      response.forEach((item) => {
        const key = `${item.rake} ${item.commodity}`;
        if (!counts[key]) {
          counts[key] = { S: 0, D: 0 };
        }
        counts[key][type] += item.value;
      });
    };

    processResponse(data.sourceResponse, "S");
    processResponse(data.destinationResponse, "D");
    processResponse(data.inlineSourceResponse, "S");
    processResponse(data.inlineDestinationResponse, "D");

    return counts;
  };

  useEffect(() => {
    const fetchData = async () => {
      const urls = [
        `${portalUrl}/ToolOptimizerWebApi/SelectedCostRateMatrixforTool?matrixType=FreightRate&rakeType=BCN&commodity=WHEAT`,
        `${portalUrl}/ToolOptimizerWebApi/SelectedCostRateMatrixforTool?matrixType=FreightRate&rakeType=BCN&commodity=RICE`,
        `${portalUrl}/ToolOptimizerWebApi/SelectedCostRateMatrixforTool?matrixType=FreightRate&rakeType=BCNHL&commodity=WHEAT`,
        `${portalUrl}/ToolOptimizerWebApi/SelectedCostRateMatrixforTool?matrixType=FreightRate&rakeType=BCNHL&commodity=RICE`,
      ];

      try {
        // Fetch all URLs in parallel
        const responses = await Promise.all(
          urls.map((url) => fetch(url).then((response) => response.json()))
        );

        // Combine all responses into one object
        const allData = {
          wheat_42w: responses[0],
          rice_42w: responses[1],
          wheat_58w: responses[2],
          rice_58w: responses[3],
        };

        await sendDataToBackend(allData);
        // Store fetched data in state
        setLoading(false); // Set loading state to false
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const sendDataToBackend = async (allData) => {
    try {
      console.log(allData);
      const response = await fetch(`${ProjectIp}/process-data`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(allData),
      });

      if (!response.ok) {
        throw new Error("Failed to send data to backend");
      }
    } catch (error) {
      console.error("Error sending data to backend:", error);
    }
  };

  // const ImportData = (event) => {
  //   event.preventDefault();
  //   setLoading(true);
  //   fetch(`${portalUrl}/ToolOptimizerWebApi/DailyPlannerNextDayforTool`)
  //     .then((response) => {
  //       if (response.status === 200) {
  //         return response.json();
  //       } else {
  //         setLoading(false);
  //         alert(`Failed to fetch data. Status code: ${response.status}`);
  //         return null;
  //       }
  //     })
  //     .then((data) => {
  //       if (data) {
  //         setProgress((prev) => [
  //           ...prev,
  //           "Successfully imported data from portal",
  //         ]);
  //         setNextDayData(data);
  //         if (data.sourceResponse) {
  //           const updatedSurplus = data.sourceResponse.map((item) => ({
  //             virtualCode: item.sourceRailHead,
  //             origin_railhead: item.virtualCode,
  //             origin_state: item.sourceState,
  //             Value: item.value,
  //             Commodity: item.commodity,
  //             sourceDivision: item.sourceDivision,
  //             sourceId: item.sourceId,
  //             rake: item.rake,
  //             sourceMergingId: item.sourceMergingId,
  //             sourceIndentIds: item.sourceIndentIds,
  //             sourceRailHeadName: item.sourceRailHeadName,
  //           }));
  //           setSurplus(updatedSurplus);
  //         }

  //         if (data.destinationResponse) {
  //           const updatedDeficit = data.destinationResponse.map((item) => ({
  //             virtualCode: item.destinationRailHead,
  //             origin_railhead: item.virtualCode,
  //             origin_state: item.destinationState,
  //             Value: item.value,
  //             Commodity: item.commodity,
  //             destinationDivision: item.destinationDivision,
  //             destinationId: item.destinationId,
  //             rake: item.rake,
  //             destinationMergingId: item.destinationMergingId,
  //             destinationIndentIds: item.destinationIndentIds,
  //             destinationRailHeadName: item.destinationRailHeadName,
  //           }));
  //           setDeficit(updatedDeficit);
  //         }

  //         if (data.inlineSourceResponse) {
  //           const updatedSurplusInline = data.inlineSourceResponse.map(
  //             (item) => ({
  //               virtualCode: item.sourceRailHead,
  //               inlineVirtualCode: item.sourceInlineRailHead,
  //               origin_railhead: item.virtualCode,
  //               origin_state: item.sourceState,
  //               destination_railhead: item.inlinevirtualcode,
  //               destination_state: item.sourceState,
  //               Value: 1,
  //               Commodity: item.commodity,
  //               sourceDivision: item.sourceDivision,
  //               inlineSourceDivision: item.inlineSourceDivision,
  //               sourceId: item.sourceId,
  //               rake: item.rake,
  //               sourceMergingId: item.sourceMergingId,
  //               sourceIndentIds: item.sourceIndentIds,
  //               sourceRailHeadName: item.sourceRailHeadName,
  //               sourceInlineRailHeadName: item.sourceInlineRailHeadName,
  //             })
  //           );
  //           setSurplusInline(updatedSurplusInline);
  //         }

  //         if (data.inlineDestinationResponse) {
  //           const updatedDeficitInline = data.inlineDestinationResponse.map(
  //             (item) => ({
  //               virtualCode: item.destinationRailHead,
  //               inlineVirtualCode: item.destinationInlineRailHead,
  //               origin_railhead: item.virtualCode,
  //               origin_state: item.destinationState,
  //               destination_railhead: item.inlinevirtualcode,
  //               destination_state: item.destinationState,
  //               Value: 1,
  //               Commodity: item.commodity,
  //               destinationDivision: item.destinationDivision,
  //               inlineDestinationDivision: item.inlineDestinationDivision,
  //               destinationId: item.destinationId,
  //               rake: item.rake,
  //               destinationMergingId: item.destinationMergingId,
  //               destinationIndentIds: item.destinationIndentIds,
  //               destinationRailHeadName: item.destinationRailHeadName,
  //               destinationInlineRailHeadName:
  //                 item.destinationInlineRailHeadName,
  //             })
  //           );
  //           setDeficitInline(updatedDeficitInline);
  //         }

  //         if (data.routeFixing) {
  //           const updatedRouteFixing = data.routeFixing.map((item) => ({
  //             sourceVirtualCode: item.sourceRailHead,
  //             destinationVirtualCode: item.destinationRailHead,
  //             origin_railhead: item.sourcevirtualcode,
  //             origin_state: item.sourceState,
  //             destination_railhead: item.destinationvirtualcode,
  //             destination_state: item.destinationState,
  //             Commodity: item.sourceCommodity,
  //             value: item.sourceValue,
  //             sourceRakeType: item.sourceRakeType,
  //             destinationRakeType: item.destinationRakeType,
  //             sourceDivision: item.sourceDivision,
  //             destinationDivision: item.destinationDivision,
  //             sourceId: item.sourceId,
  //             destinationId: item.destinationId,
  //             destinationMergingId: item.destinationMergingId,
  //             sourceMergingId: item.sourceMergingId,
  //             sourceIndentIds: item.sourceIndentIds,
  //             destinationIndentIds: item.destinationIndentIds,
  //             destinationRailHeadName: item.destinationRailHeadName,
  //             sourceRailHeadName: item.sourceRailHeadName,
  //             sourceInlineRailHead: item.sourceInlineRailHead,
  //             destinationInlineRailHead: item.destinationInlineRailHead,
  //             destinationInlineRailHeadName: item.destinationInlineRailHeadName,
  //             sourceInlineRailHeadName: item.sourceInlineRailHeadName,
  //           }));
  //           setFixeddata(updatedRouteFixing);
  //         }

  //         if (data.routeBlocking) {
  //           const updatedRouteBlocking = data.routeBlocking.map((item) => ({
  //             sourceVirtualCode: item.sourceRailHead,
  //             destinationVirtualCode: item.destinationRailHead,
  //             origin_railhead: item.sourcevirtualcode,
  //             origin_state: item.sourceState,
  //             destination_railhead: item.destinationvirtualcode,
  //             destination_state: item.destinationState,
  //             Commodity: item.sourceCommodity,
  //             value: item.sourceValue,
  //             rake: item.rake,
  //           }));
  //           setBlockeddata(updatedRouteBlocking);
  //         }

  //         setDisableAfterImport(true);
  //         setLoading(false);
  //         setCounts(getCounts(data));
  //       }
  //     });
  // };

  const handleSolve = async () => {
    try {
      // Import data from the portal
      const response = await fetch(
        `${portalUrl}/ToolOptimizerWebApi/DailyPlannerNextDayforTool`
      );

      if (response.status === 200) {
        const next_day_data = await response.json();
        setProgress((prev) => [
          ...prev,
          "Successfully imported data from portal",
        ]);
        setNextDayData(next_day_data);

        if (next_day_data.sourceResponse) {
          const updatedSurplus = next_day_data.sourceResponse.map((item) => ({
            virtualCode: item.sourceRailHead,
            origin_railhead: item.virtualCode,
            origin_state: item.sourceState,
            Value: item.value,
            Commodity: item.commodity,
            sourceDivision: item.sourceDivision,
            sourceId: item.sourceId,
            rake: item.rake,
            sourceMergingId: item.sourceMergingId,
            sourceIndentIds: item.sourceIndentIds,
            sourceRailHeadName: item.sourceRailHeadName,
          }));
          setSurplus(updatedSurplus);
        }

        if (next_day_data.destinationResponse) {
          const updatedDeficit = next_day_data.destinationResponse.map(
            (item) => ({
              virtualCode: item.destinationRailHead,
              origin_railhead: item.virtualCode,
              origin_state: item.destinationState,
              Value: item.value,
              Commodity: item.commodity,
              destinationDivision: item.destinationDivision,
              destinationId: item.destinationId,
              rake: item.rake,
              destinationMergingId: item.destinationMergingId,
              destinationIndentIds: item.destinationIndentIds,
              destinationRailHeadName: item.destinationRailHeadName,
            })
          );
          setDeficit(updatedDeficit);
        }

        if (next_day_data.inlineSourceResponse) {
          const updatedSurplusInline = next_day_data.inlineSourceResponse.map(
            (item) => ({
              virtualCode: item.sourceRailHead,
              inlineVirtualCode: item.sourceInlineRailHead,
              origin_railhead: item.virtualCode,
              origin_state: item.sourceState,
              destination_railhead: item.inlinevirtualcode,
              destination_state: item.sourceState,
              Value: 1,
              Commodity: item.commodity,
              sourceDivision: item.sourceDivision,
              inlineSourceDivision: item.inlineSourceDivision,
              sourceId: item.sourceId,
              rake: item.rake,
              sourceMergingId: item.sourceMergingId,
              sourceIndentIds: item.sourceIndentIds,
              sourceRailHeadName: item.sourceRailHeadName,
              sourceInlineRailHeadName: item.sourceInlineRailHeadName,
            })
          );
          setSurplusInline(updatedSurplusInline);
        }

        if (next_day_data.inlineDestinationResponse) {
          const updatedDeficitInline =
            next_day_data.inlineDestinationResponse.map((item) => ({
              virtualCode: item.destinationRailHead,
              inlineVirtualCode: item.destinationInlineRailHead,
              origin_railhead: item.virtualCode,
              origin_state: item.destinationState,
              destination_railhead: item.inlinevirtualcode,
              destination_state: item.destinationState,
              Value: 1,
              Commodity: item.commodity,
              destinationDivision: item.destinationDivision,
              inlineDestinationDivision: item.inlineDestinationDivision,
              destinationId: item.destinationId,
              rake: item.rake,
              destinationMergingId: item.destinationMergingId,
              destinationIndentIds: item.destinationIndentIds,
              destinationRailHeadName: item.destinationRailHeadName,
              destinationInlineRailHeadName: item.destinationInlineRailHeadName,
            }));
          setDeficitInline(updatedDeficitInline);
        }

        if (next_day_data.routeFixing) {
          const updatedRouteFixing = next_day_data.routeFixing.map((item) => ({
            sourceVirtualCode: item.sourceRailHead,
            destinationVirtualCode: item.destinationRailHead,
            origin_railhead: item.sourcevirtualcode,
            origin_state: item.sourceState,
            destination_railhead: item.destinationvirtualcode,
            destination_state: item.destinationState,
            Commodity: item.sourceCommodity,
            value: item.sourceValue,
            sourceRakeType: item.sourceRakeType,
            destinationRakeType: item.destinationRakeType,
            sourceDivision: item.sourceDivision,
            destinationDivision: item.destinationDivision,
            sourceId: item.sourceId,
            destinationId: item.destinationId,
            destinationMergingId: item.destinationMergingId,
            sourceMergingId: item.sourceMergingId,
            sourceIndentIds: item.sourceIndentIds,
            destinationIndentIds: item.destinationIndentIds,
            destinationRailHeadName: item.destinationRailHeadName,
            sourceRailHeadName: item.sourceRailHeadName,
            sourceInlineRailHead: item.sourceInlineRailHead,
            destinationInlineRailHead: item.destinationInlineRailHead,
            destinationInlineRailHeadName: item.destinationInlineRailHeadName,
            sourceInlineRailHeadName: item.sourceInlineRailHeadName,
          }));
          setFixeddata(updatedRouteFixing);
        }

        if (next_day_data.routeBlocking) {
          const updatedRouteBlocking = next_day_data.routeBlocking.map(
            (item) => ({
              sourceVirtualCode: item.sourceRailHead,
              destinationVirtualCode: item.destinationRailHead,
              origin_railhead: item.sourcevirtualcode,
              origin_state: item.sourceState,
              destination_railhead: item.destinationvirtualcode,
              destination_state: item.destinationState,
              Commodity: item.sourceCommodity,
              value: item.sourceValue,
              rake: item.rake,
            })
          );
          setBlockeddata(updatedRouteBlocking);
        }

        setDisableAfterImport(true);
        setCounts(getCounts(next_day_data));

        try {
          const response = await fetch(ProjectIp + "/Daily_Planner", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(next_day_data),
          });

          const result_data = await response.json();
          if (result_data.status === 1) {
            setResult(result_data.result);
            setSolutionSolved(true);
            setIsLoading(false);
            document.getElementById("toggle").checked = false;
            setProgress((prev) => [...prev, result_data.message]);

            // Export the data to the portal
            // try {
            //   const response = await fetch(
            //     `${portalUrl}/ToolOptimizerWebApi/PostDailyPlanner`,
            //     {
            //       method: "POST",
            //       headers: {
            //         "Content-Type": "application/json",
            //       },
            //       body: JSON.stringify(result_data.result),
            //     }
            //   );

            //   // Check if the response is okay
            //   if (!response.ok) {
            //     throw new Error(`HTTP error! Status: ${response.status}`);
            //   } else {
            //     alert("Data successfully exported to the portal");
            //     setProgress((prev) => [
            //       ...prev,
            //       "Data successfully exported to the portal",
            //     ]);
            //   }
            // } catch (error) {
            //   console.error("An error occurred:", error.message);
            //   return null;
            // }
          } else {
            setIsLoading(false);
            document.getElementById("toggle").checked = false;
            setProgress((prev) => [...prev, result_data.message]);
          }
        } catch (error) {
          setIsLoading(false);
          document.getElementById("toggle").checked = false;
          console.error("Error:", error);
        }
      } else {
        throw new Error(
          `Failed to fetch data. Status code: ${response.status}`
        );
      }
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div style={{ backgroundColor: "#f1f1f1" }}>
      {loading && (
        <div className="spinner-overlay">
          <div className="spinner"></div>
        </div>
      )}
      <div>
        <Sidenav />
        <div class="grid-container">
          <div class="sidebar">
            <div
              style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                margin: "10px 0px",
                fontSize: 20,
              }}
            >
              Summary
            </div>
            <div
              style={{
                margin: "0px 8px",
                display: "flex",
                flexDirection: "column",
                gap: 8,
              }}
            >
              <div>
                <div
                  style={{
                    display: "flex",
                    justifyContent: "center",
                  }}
                >
                  Commodity Counts
                </div>
                <ul>
                  {Object.keys(counts).map((key) => (
                    <li key={key}>
                      {/* {key} (S/D) : {counts[key].S} / {counts[key].D} */}
                      {key}: {counts[key].S}
                    </li>
                  ))}
                </ul>
              </div>

              {progress.map((progress) => (
                <div>{progress}</div>
              ))}
              {isLoading ? (
                <div
                  style={{
                    width: "fit-content",
                    display: "flex",
                    alignItems: "center",
                    width: 100,
                  }}
                >
                  Processing
                  <span
                    className="container"
                    style={{
                      display: "flex",
                      gap: "2px",
                      marginLeft: "-13px",
                    }}
                  >
                    <div className="dot"></div>
                    <div className="dot"></div>
                    <div className="dot"></div>
                  </span>
                </div>
              ) : null}
            </div>
          </div>
          <div class="dashboard">
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
                    // disabled={!disableAfterImport}
                  />
                  <span></span>
                </label>
              </div>
            </div>

            {solutionSolved && (
              <div>
                <div style={{ marginTop: 20 }}>
                  <button
                    style={{ marginLeft: "15px", borderRadius: "5px" }}
                    className="btn btn-success"
                    onClick={() => exportToExcel()}
                  >
                    Download Railhead-Railhead Detailed Plan
                  </button>

                  {/* <button
                          style={{ color: "black", marginLeft: "15px" }}
                          className="btn btn-success dropdown-toggle"
                          onClick={() => {
                            setShowResult(true);
                          }}
                        >
                          <i className="fa fa-bars"></i>
                          View Railhead Detailed Plan
                        </button> */}

                  <button
                    style={{ marginLeft: "15px", borderRadius: "5px" }}
                    className="btn btn-success"
                    onClick={exportToPDF}
                  >
                    Download PDF
                  </button>

                  <button
                    style={{ marginLeft: "15px", borderRadius: "5px" }}
                    className="btn btn-success"
                    onClick={ExpotPlan}
                  >
                    Export Plan
                  </button>

                  {true && (
                    <div
                      style={{
                        marginTop: 15,
                        marginLeft: 20,
                        width: "62vw",
                      }}
                    >
                      {result !== null && result.length > 0 ? (
                        <div>
                          <div
                            id="result"
                            style={{
                              border: "1px black solid",
                              backgroundColor: "#2a3f54",
                              color: "white",
                              borderRadius: "5px 5px 0px 0px",
                              padding: "10px",
                            }}
                          >
                            Result
                          </div>
                          {/* Responsive wrapper */}
                          <div
                            style={{
                              overflowX: "auto",
                              // border: "1px solid #ddd",
                            }}
                          >
                            <table
                              style={{
                                width: "100%",
                                borderCollapse: "collapse",
                              }}
                            >
                              <thead style={{ backgroundColor: "#dedede" }}>
                                <tr>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Sr. No
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Src RH
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Src RH Name
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Src State
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Dest RH
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Dest RH Name
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Dest State
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Commodity
                                  </th>
                                  <th
                                    style={{
                                      padding: "10px",
                                      textAlign: "left",
                                    }}
                                  >
                                    Rakes
                                  </th>
                                </tr>
                              </thead>
                              <tbody>
                                {result.map((item, index) => (
                                  <tr key={index}>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {index + 1}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.SourceRailHead}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.SourceRailHeadName}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.SourceState}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.DestinationRailHead}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.DestinationRailHeadName}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.DestinationState}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.Commodity}
                                    </td>
                                    <td
                                      style={{
                                        padding: "10px",
                                        textAlign: "left",
                                      }}
                                    >
                                      {item.Rakes}
                                    </td>
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      ) : (
                        <div />
                      )}
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Daily_Planner;
