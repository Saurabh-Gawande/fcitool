import React, { useEffect, useState } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import config from "../../config";

function Daily_Scheduler(props) {
  useEffect(() => {
    const inject = document.createElement("script");
    inject.innerHTML = `
    var fd = new FormData();
    var obj = null;
  $("#Solve_Daily_Scheduler").click(function(){
    $("#wait").css("display", "inline-block");
    
    $.ajax({
        url: projectIp + "/Daily_Scheduler",
        type: 'post',
        contentType: false,
        processData: false,
        xhrFields: { withCredentials: true },
        success: function(response){
        if(response != 0){
            var obj = JSON.parse(response);
            if(obj["status"]==1){
                $("#wait").css("display", "none");
                setTimeout(() => {
                  alert("Result are available, Please Download Result");
                  window.location.reload();
                }, 100);  
            }
            else{
                $("#wait").css("display", "none");
                alert(obj["message"]);
            }
        }
        },
        error: function(){
            $("#wait").css("display", "none");
            alert("Error Occured");
        },
        timeout:10000000000000
    });
});`;
    document.body.appendChild(inject);
    return () => {
      document.body.removeChild(inject);
    };
  });

  const [Daily_Scheduler_result, set_Daily_Scheduler_Result] = useState(null);
  const fetchReservationId_Daily_Scheduler_result = () => {
    var form = new FormData();
    const projectIp = config.serverUrl;
    fetch(projectIp + "/read_Daily_Scheduler", {
      method: "POST",
      credentials: "include",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        const fetched_Daily_Scheduler_Result = data;
        set_Daily_Scheduler_Result(fetched_Daily_Scheduler_Result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const exportToExcel = () => {
    fetchReservationId_Daily_Scheduler_result();
    if (Daily_Scheduler_result == null) {
      window.alert("Fetching Result, Please Wait");
    } else {
      const workbook = XLSX.utils.book_new();
      Object.entries(Daily_Scheduler_result).forEach(([column, data]) => {
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
      saveAs(excelBlob, "Daily_Scheduler.xlsx");
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
              {" "}
              DAILY SCHEDULER
            </span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>

        <ul className="breadcrumb">
          <li>
            <a href="/home">Home</a>
          </li>
          <li className="active">Daily Scheduler</li>
        </ul>

        <div className="page-content-wrap">
          <div className="row">
            <div className="col-md-12">
              <br />
              <br />
              <br />
              <br />
              <div className="col-md-12">
                <button
                  style={{ color: "white", marginLeft: "20px" }}
                  type="submit"
                  className="btn btn-primary pull-left"
                  value="Solve"
                  id="Solve_Daily_Scheduler"
                >
                  Solve for Daily Scheduler
                </button>
              </div>
              <br />
              <br />
              <div className="panel-heading">
                <h3 className="panel-title"></h3>
                <div className="btn-group pull-left">
                  <button
                    style={{ color: "white", marginLeft: "15px" }}
                    className="btn btn-danger dropdown-toggle"
                    onClick={() => exportToExcel()}
                  >
                    <i className="fa fa-bars"></i> Download Result of Daily
                    Scheduler
                  </button>
                </div>
              </div>
            </div>
            <br />
            <br />
            <br />
            <br /> <br />
            <br />
            <br />
            <br />
            <br /> <br />
            <br />
            <br />
            <br />
            <br /> <br />
            <br />
            <br />
            <br />
            <br /> <br />
            <br />
            <br />
            <br />
            <br />
            <br /> <br />
            <br />
            <br />
            <br />
            <br /> <br />
            <br />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Daily_Scheduler;
