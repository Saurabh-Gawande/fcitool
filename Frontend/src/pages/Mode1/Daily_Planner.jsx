import React, { useState, useEffect } from "react";
import config from "../../config";
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
  const [data, setData] = useState(null);

  function exportToExcel() {}
  function viewGrid() {}
  function exportToPDF() {}
  function uploadFile() {}

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

        setData(allData);
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

  const fetchData = (event) => {
    event.preventDefault();
    setLoading(true);
    fetch(`${portalUrl}/ToolOptimizerWebApi/DailyPlannerNextDayforTool`)
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        } else {
          setLoading(false);
          alert(`Failed to fetch data. Status code: ${response.status}`);
          return null;
        }
      })
      .then((data) => {
        if (data) {
          setProgress((prev) => [
            ...prev,
            "Successfully imported data from portal",
          ]);
          setNextDayData(data);
          if (data.sourceResponse) {
            const updatedSurplus = data.sourceResponse.map((item) => ({
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

          if (data.destinationResponse) {
            const updatedDeficit = data.destinationResponse.map((item) => ({
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
            }));
            setDeficit(updatedDeficit);
          }

          if (data.inlineSourceResponse) {
            const updatedSurplusInline = data.inlineSourceResponse.map(
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

          if (data.inlineDestinationResponse) {
            const updatedDeficitInline = data.inlineDestinationResponse.map(
              (item) => ({
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
                destinationInlineRailHeadName:
                  item.destinationInlineRailHeadName,
              })
            );
            setDeficitInline(updatedDeficitInline);
          }

          if (data.routeFixing) {
            const updatedRouteFixing = data.routeFixing.map((item) => ({
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

          if (data.routeBlocking) {
            const updatedRouteBlocking = data.routeBlocking.map((item) => ({
              sourceVirtualCode: item.sourceRailHead,
              destinationVirtualCode: item.destinationRailHead,
              origin_railhead: item.sourcevirtualcode,
              origin_state: item.sourceState,
              destination_railhead: item.destinationvirtualcode,
              destination_state: item.destinationState,
              Commodity: item.sourceCommodity,
              value: item.sourceValue,
              rake: item.rake,
            }));
            setBlockeddata(updatedRouteBlocking);
          }

          setDisableAfterImport(true);
          setLoading(false);
        }
      });
  };

  const handleSolve = async () => {
    try {
      const response = await fetch(ProjectIp + "/Daily_Planner1", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(nextDayData),
      });
      if (response.ok) {
        setSolutionSolved(true);
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } catch (error) {}
  };

  return (
    <div
      className="page-container"
      style={{ backgroundColor: "#E7A63D", height: "100vh", overflowY: "auto" }}
    >
      {loading && (
        <div className="spinner-overlay">
          <div className="spinner"></div>
        </div>
      )}
      <Sidenav />
      <div
        className="page-content"
        style={{
          display: "flex",
          backgroundImage: "url('static/img/bg8.jpg')",
          widows: "20px",
        }}
      >
        <div>
          <ul
            className="x-navigation x-navigation-horizontal x-navigation-panel"
            style={{ backgroundColor: "#E7A63D" }}
          >
            <li className="xn-icon-button">
              <a href="javascript:void(0)" className="x-navigation-minimize">
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
                Optimized Daily Plan
              </span>
              <a className="x-navigation-control"></a>
            </li>
          </ul>

          <ul className="breadcrumb">
            <li>
              <a href="/home">Home</a>
            </li>
            <li className="active">Daily plan</li>
            <li className="active">v15-10</li>
          </ul>

          {/* {showModal ? (
            <div className="modal-overlay" onClick={handleCloseModal}>
              <div className="modal-content">
                <span className="close-btn" onClick={closeModal}>
                  &times;
                </span>
                <div
                  style={{
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    flexDirection: "column",
                  }}
                >
                  <h2>Alert</h2>
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      textAlign: "center",
                      padding: "5px",
                    }}
                  >
                    {modalValue}
                  </div>
                </div>
                <div
                  style={{
                    display: "flex",
                    justifyContent: "end",
                    padding: "5px 2px",
                  }}
                >
                  <button
                    onClick={closeModal}
                    type="button"
                    className="btn btn-danger"
                  >
                    Close
                  </button>
                </div>
              </div>
            </div>
          ) : null} */}
          <div className="page-content-wrap">
            <div className="row">
              <div className="col-md-12" style={{ width: "70vw" }}>
                <br />
                <br />
                <div
                  style={{
                    display: "flex",
                    justifyContent: "end",
                    width: "80%",
                  }}
                >
                  <button
                    style={{
                      color: "white",
                      display: "flex",
                      flexFlow: 1,
                      alignItems: "center",
                    }}
                    className="btn btn-danger dropdown-toggle"
                    onClick={fetchData}
                  >
                    <i className="fa fa-bars"></i>
                    Import data
                  </button>
                </div>
                <div style={{ marginLeft: "15px" }}>
                  <div style={{ fontSize: "20px", fontWeight: "700" }}>
                    <i className="fa fa-info-circle" aria-hidden="true"></i>{" "}
                    Configurations
                  </div>
                  <br />
                  <form style={{ marginLeft: "50px" }}>
                    <br />
                    {surplus.length !== 0 && (
                      <p style={{ margin: 2, padding: 0, marginTop: 15 }}>
                        <strong
                          style={{
                            color: "#9d0921",
                            fontSize: "20px",
                            marginLeft: "15px",
                          }}
                        >
                          For Origin:
                        </strong>
                      </p>
                    )}
                    <div>
                      <br />
                      {surplus.length !== 0 && (
                        <table style={{ width: "65vw" }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Region</th>
                              <th>Division</th>
                              <th>Railhead</th>
                              <th>Commodity</th>
                              <th>Rake preference</th>
                              <th>Rakes</th>
                            </tr>
                          </thead>
                          <tbody>
                            {surplus.map((row, index) => (
                              <tr key={index}>
                                <td>{index + 1}</td>
                                <td>{row.origin_state}</td>
                                <td>{row.sourceDivision}</td>
                                <td>{row.virtualCode}</td>
                                <td>{row.Commodity}</td>
                                <td>{row.rake}</td>
                                <td>{row.Value}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      )}
                      {deficit.length !== 0 && (
                        <p style={{ margin: 2, padding: 0, marginTop: 20 }}>
                          <strong
                            style={{
                              color: "#9d0921",
                              fontSize: "20px",
                              marginLeft: "15px",
                            }}
                          >
                            For Destination:
                          </strong>
                        </p>
                      )}
                      <br />
                      {deficit.length !== 0 && (
                        <table style={{ width: "65vw" }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Region</th>
                              <th>Division</th>
                              <th>Railhead</th>
                              <th>Commodity</th>
                              <th>Rake preference</th>
                              <th>Rakes</th>
                            </tr>
                          </thead>
                          <tbody>
                            {deficit.map((row, index) => (
                              <tr key={index}>
                                <td>{index + 1}</td>
                                <td>{row.origin_state}</td>
                                <td>{row.destinationDivision}</td>
                                <td>{row.virtualCode}</td>
                                <td>{row.Commodity}</td>
                                <td>{row.rake}</td>
                                <td>{row.Value}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      )}
                      {surplusInline.length !== 0 && (
                        <p style={{ margin: 2, padding: 0, marginTop: 12 }}>
                          <strong
                            style={{
                              color: "#9d0921",
                              fontSize: "20px",
                              marginLeft: "15px",
                            }}
                          >
                            For Inline Origin:
                          </strong>
                        </p>
                      )}
                      {surplusInline.length > 0 && (
                        <table style={{ width: "65vw", marginTop: 20 }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Commodity</th>
                              <th>Rake preference</th>
                              <th>Value</th>
                            </tr>
                          </thead>
                          <tbody>
                            {surplusInline.map((row, index) => {
                              return (
                                <tr key={index}>
                                  <td>{index + 1}</td>
                                  <td>{row.virtualCode}</td>
                                  <td>{row.origin_state}</td>
                                  <td>{row.inlineVirtualCode}</td>
                                  <td>{row.destination_state}</td>
                                  <td>{row.Commodity}</td>
                                  <td>{row.rake}</td>
                                  <td>{row.Value}</td>
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
                      )}

                      {deficitInline.length !== 0 && (
                        <p style={{ margin: 2, padding: 0, marginTop: 30 }}>
                          <strong
                            style={{
                              color: "#9d0921",
                              fontSize: "20px",
                              marginLeft: "15px",
                            }}
                          >
                            For Inline Destination:
                          </strong>
                        </p>
                      )}
                      {deficitInline.length > 0 && (
                        <table style={{ width: "65vw", marginTop: 20 }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Commodity</th>
                              <th>Rake preference</th>
                              <th>Value</th>
                            </tr>
                          </thead>
                          <tbody>
                            {deficitInline.map((row, index) => {
                              return (
                                <tr key={index}>
                                  <td>{index + 1}</td>
                                  <td>{row.virtualCode}</td>
                                  <td>{row.origin_state}</td>
                                  <td>{row.inlineVirtualCode}</td>
                                  <td>{row.destination_state}</td>
                                  <td>{row.Commodity}</td>
                                  <td>{row.rake}</td>
                                  <td>{row.Value}</td>
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
                      )}
                    </div>
                    <br />
                    {fixed_data.length !== 0 && (
                      <p style={{ margin: 0, padding: 0 }}>
                        <strong
                          style={{
                            color: "#9d0921",
                            fontSize: "20px",
                            marginLeft: "15px",
                          }}
                        >
                          For Route Fixing:
                        </strong>
                      </p>
                    )}
                    <br />
                    <br />
                    {fixed_data.length !== 0 && (
                      <div>
                        <table style={{ width: "65vw" }}>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Destination State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Destination Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Rake preference
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Commodity
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Rakes
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {fixed_data.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>
                                  {item.sourceVirtualCode &&
                                  item.sourceInlineRailHead
                                    ? item.sourceVirtualCode +
                                      "+" +
                                      item.sourceInlineRailHead
                                    : item.sourceVirtualCode}
                                </td>
                                <td>{item.destination_state}</td>
                                <td>
                                  {item.destinationVirtualCode &&
                                  item.destinationInlineRailHead
                                    ? item.destinationVirtualCode +
                                      "+" +
                                      item.destinationInlineRailHead
                                    : item.destinationVirtualCode}
                                </td>
                                <td>{item.sourceRakeType}</td>
                                <td>{item.Commodity}</td>
                                <td>{item.value}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}

                    {blocked_data.length !== 0 && (
                      <p style={{ margin: 2, padding: 0, marginTop: 10 }}>
                        <strong
                          style={{
                            color: "#9d0921",
                            fontSize: "20px",
                            marginLeft: "15px",
                          }}
                        >
                          For Route Blocking:
                        </strong>
                      </p>
                    )}
                    <br />
                    {blocked_data.length !== 0 && (
                      <div>
                        <table style={{ width: "65vw" }}>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Destination State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Destination Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Commodity
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Rake preference
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Value
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {blocked_data.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>{item.sourceVirtualCode}</td>
                                <td>{item.destination_state}</td>
                                <td>{item.destinationVirtualCode}</td>
                                <td>{item.Commodity}</td>
                                <td>{item.rake}</td>
                                <td>{item.value}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}
                    <br />
                  </form>

                  {disableAfterImport && (
                    <>
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
                          <span
                            style={{ textAlign: "center", fontWeight: "bold" }}
                          >
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
                              disabled={!disableAfterImport}
                            />
                            <span></span>
                          </label>
                        </div>
                      </div>
                    </>
                  )}

                  <br />
                  <br />
                  {solutionSolved && (
                    <div>
                      <div>
                        <button
                          style={{ color: "black", marginLeft: "15px" }}
                          className="btn btn-success dropdown-toggle"
                          onClick={() => exportToExcel()}
                        >
                          <i className="fa fa-bars"></i>
                          Download Railhead-Railhead Detailed Plan
                        </button>

                        <button
                          style={{ color: "black", marginLeft: "15px" }}
                          className="btn btn-success dropdown-toggle"
                          onClick={viewGrid}
                        >
                          <i className="fa fa-bars"></i>
                          View Railhead Detailed Plan
                        </button>

                        <button
                          style={{ color: "black", marginLeft: "15px" }}
                          className="btn btn-success dropdown-toggle"
                          onClick={exportToPDF}
                        >
                          <i className="fa fa-bars"></i>
                          Download PDF
                        </button>
                        <button
                          style={{ color: "black", marginLeft: "15px" }}
                          className="btn btn-success dropdown-toggle"
                          onClick={uploadFile}
                          disabled={!disableAfterImport}
                        >
                          <i className="fa fa-bars"></i>
                          Export Plan
                        </button>
                      </div>
                    </div>
                  )}
                  <br />
                </div>
              </div>
            </div>
            <br />
          </div>
        </div>
        <div
          style={{
            backgroundColor: "#E7A63D",
            width: "20%",
            display: "flex",
            flexDirection: "column",
            alignContent: "center",
            alignItems: "center",
          }}
        >
          <span style={{ color: "black", fontSize: "32px" }}>Progress Bar</span>

          <div
            style={{
              padding: "8px 0",
              width: "90%",
              display: "flex",
              flexDirection: "column",
              border: "2px dashed black",
              marginTop: 15,
              maxHeight: "110vh",
              overflowY: "auto",
            }}
            id="console_"
          >
            <div
              style={{
                margin: "0px 8px",
                display: "flex",
                flexDirection: "column",
                gap: 8,
              }}
            >
              {/* <div style={{ fontWeight: "bold" }}>{status}</div> */}
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
        </div>
      </div>
    </div>
  );
}

export default Daily_Planner;
