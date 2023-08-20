import React, { useRef, useState } from "react";
import Sidenav from "./sidenav_M02";

function Alternate_Railhead_M02() {
  const [rhSource, setRhSource] = useState("");
  const [rhDest, setRhDest] = useState("");
  const [zone, setZone] = useState("");
  const [n, setN] = useState(0);
  const buttonRef = useRef(null);
  const [data, setData] = useState([]);

  const fetchData = () => {
    fetch("http://localhost:5000/Alternate_Railhead_readPickle")
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
      n: n,
    };
    try {
      const response = await fetch(
        "http://localhost:5000/Alternate_Railhead_Solve",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }
      );

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
              ALTERNATE RAILHEAD
            </span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>

        <ul className="breadcrumb">
          <li>
            <a href="/home">Home</a>
          </li>
          <li className="active">Alternate Railhead</li>
        </ul>

        <div className="page-content-wrap">
          <div className="row">
            <div className="col-md-12">
              <div>
                <br />
                <br />
                <form>
                  <label>
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Enter source railhead:
                    </strong>
                    <input
                      type="text"
                      value={rhSource}
                      onChange={(e) => setRhSource(e.target.value)}
                      style={{ marginLeft: "285px" }}
                    />
                  </label>
                  <br />
                  <br />
                  <label>
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Enter destination railhead:
                    </strong>
                    <input
                      type="text"
                      value={rhDest}
                      onChange={(e) => setRhDest(e.target.value)}
                      style={{ marginLeft: "250px" }}
                    />
                  </label>
                  <br />
                  <br />
                  <label>
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Alternate railhead option for destination tagging:
                    </strong>
                    <select
                      value={zone}
                      onChange={(e) => setZone(e.target.value)}
                      style={{ marginLeft: "75px" }}
                    >
                      <option value="">Select a zone</option>
                      <option value="south">South Zone</option>
                      <option value="north">North Zone</option>
                      <option value="east">East Zone</option>
                      <option value="west">West Zone</option>
                      <option value="northeast">Northeast Zone</option>
                    </select>
                  </label>
                  <br />
                  <br />
                  <label>
                    <strong style={{ fontSize: "16px", marginLeft: "15px" }}>
                      Cost rate increment factor allowed:
                    </strong>
                    <input
                      type="number"
                      value={n}
                      onChange={(e) => setN(parseFloat(e.target.value))}
                      style={{ marginLeft: "185px" }}
                    />
                  </label>
                  <br />
                  <br />
                </form>
                <button
                  style={{
                    color: "white",
                    backgroundColor: "blue",
                    fontSize: "20px",
                    width: "8%",
                    marginLeft: "465px",
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
      </div>
    </div>
  );
}

export default Alternate_Railhead_M02;
