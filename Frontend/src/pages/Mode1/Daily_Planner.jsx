import React, { useRef, useState, useEffect } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import background1 from "./../../assets/upload1_.png";

function Daily_Planner() {
  const ProjectIp = "http://localhost:5000";
  const [fileSelected, setFileSelected] = useState(false);
  const [inline_value_rice, setInlineValueRice] = useState("");
  const [inline_value_wheat, setInlineValueWheat] = useState("");
  const [block_data, setBlockdata] = useState([]);
  const [block_data2, setBlockdata2] = useState([]);
  const [block_dataWheat2, setBlockdataWheat2] = useState([]);
  const [block_data3, setBlockdata3] = useState([]);
  const [block_dataWheat3, setBlockdataWheat3] = useState([]);
  const [rice_destination, setRiceDestination] = useState([]);
  const [wheat_destination, setWheatDestination] = useState([]);
  const [fixed_data, setFixeddata] = useState([]);
  const [selectedOption, setSelectedOption] = useState("default");
  const [subOptions, setSubOptions] = useState([]);
  const [selectedOption2, setSelectedOption2] = useState("default");
  const [subOptions2, setSubOptions2] = useState([]);
  const [selectedOption3, setSelectedOption3] = useState("default");
  const [subOptions3, setSubOptions3] = useState([]);
  const [selectedOptionWheat3, setSelectedOptionWheat3] = useState("default");
  const [subOptionsWheat3, setSubOptionsWheat3] = useState([]);
  const [selectedOption4, setSelectedOption4] = useState("default");
  const [subOptions4, setSubOptions4] = useState([]);
  const [selectedOptionWheat4, setSelectedOptionWheat4] = useState("default");
  const [subOptionsWheat4, setSubOptionsWheat4] = useState([]);
  const [selectedOption5, setSelectedOption5] = useState("default");
  const [subOptions5, setSubOptions5] = useState([]);
  const [selectedOption6, setSelectedOption6] = useState("default");
  const [subOptions6, setSubOptions6] = useState([]);
  const [selectedOptionWheat5, setSelectedOptionWheat5] = useState("default");
  const [subOptionsWheat5, setSubOptionsWheat5] = useState([]);
  const [selectedOptionWheat6, setSelectedOptionWheat6] = useState("default");
  const [subOptionsWheat6, setSubOptionsWheat6] = useState([]);
  const [subOption1, setSubOption1] = useState("");
  const [subOption2, setSubOption2] = useState("");
  const [subOption3, setSubOption3] = useState("");
  const [subOptionWheat3, setSubOptionWheat3] = useState("");
  const [subOption4, setSubOption4] = useState("");
  const [subOptionWheat4, setSubOptionWheat4] = useState("");
  const [subOption5, setSubOption5] = useState("");
  const [subOption6, setSubOption6] = useState("");
  const [subOptionWheat5, setSubOptionWheat5] = useState("");
  const [subOptionWheat6, setSubOptionWheat6] = useState("");
  const [selectedOption_fixed, setSelectedOption_fixed] = useState("default");
  const [subOptions_fixed, setSubOptions_fixed] = useState([]);
  const [selectedOption2_fixed, setSelectedOption2_fixed] = useState("default");
  const [subOptions2_fixed, setSubOptions2_fixed] = useState([]);
  const [subOption1_fixed, setSubOption1_fixed] = useState("");
  const [subOption2_fixed, setSubOption2_fixed] = useState("");
  const [commodity_fixed, setCommodity_fixed] = useState("RICE");
  const [value_fixed, setValue_fixed] = useState("");
  const [TEFD, set_TEFD] = useState("");
  const [Scenerio, set_Scenerio] = useState("");
  const [solutionSolved, setSolutionSolved] = useState(false);
  const [scn, setscn] = useState(false);
  const [uploadst, setuploadst] = useState(false);
  const [Total_result, set_Total_Result] = useState(null);
  const [Relevant_result, set_Relevant_Result] = useState(null);
  const [excelData, setExcelData] = useState({});
  const [activeSheetName, setActiveSheetName] = useState(null);
  const [sheet, setSheet] = useState(null);
  const [updateExcel, setUpdateExcel] = useState(false);
  const [updateExcel2, setUpdateExcel2] = useState(false);
  const [modifiedExcel, setModifiedExcel] = useState({});

  // Block_data for blocking, fixed_data for fixing, block_data3 for rice_origin, block_data4 for rice_destination

  const handleCellChange = (sheetName, rowIndex, columnIndex, newValue) => {
    const updatedData = { ...excelData };
    updatedData[sheetName][rowIndex][columnIndex] = newValue;
    setExcelData(updatedData);
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

  const update_excel = async () => {
    setUpdateExcel2(false);
    const response = await fetch(ProjectIp + "/getDaily1ExcelData");
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
  };

  const update_excel2 = async () => {
    setUpdateExcel(false);
    const response = await fetch(ProjectIp + "/getDaily2ExcelData");
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
    setUpdateExcel2(true);
  };

  const save_excel = async () => {
    const newWorkbook = XLSX.utils.book_new();
    Object.keys(excelData).forEach((sheetName) => {
      const worksheet = XLSX.utils.json_to_sheet(excelData[sheetName]);
      XLSX.utils.book_append_sheet(newWorkbook, worksheet, sheetName);
    });

    try {
      var scenario;
      if (updateExcel == true) {
        scenario = "/Modify_Daily_Template_S01";
      } else {
        scenario = "/Modify_Daily_Template_S02";
      }
      const response = await fetch(ProjectIp + scenario, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newWorkbook),
      });
      if (response.ok) {
        console.log("Data sent to backend successfully");
      } else {
        console.error("Failed to send data to backend");
      }
    } catch (error) {
      console.error("Error sending data:", error);
    }
    setUpdateExcel(false);
    setUpdateExcel2(false);
    document.getElementById('console_').style.display='block';
    document.getElementById('console_').innerHTML+="Template has been updated"+'<br/>';
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

      const response = await fetch(ProjectIp + "/uploadDailyFile_S2", {
        method: "POST",
        credentials: "include",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const jsonResponse = await response.json();

      if (jsonResponse.status === 1) {
        alert("File Uploaded");
      } else {
        console.log(jsonResponse);
        alert("Error uploading file");
      }
    } catch (error) {
      console.error("Error during file upload:", error);
      alert("An error occurred during file upload. Please try again later.");
    }
  };

  const handleUploadConfig1 = async () => {
    if (!fileSelected) {
      alert("Please Select The File First");
      return;
    }

    try {
      const files = document.getElementById("uploadFile").files;
      const formData = new FormData();
      formData.append("uploadFile", files[0]);

      const response = await fetch(ProjectIp + "/uploadDailyFile_S1", {
        method: "POST",
        credentials: "include",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const jsonResponse = await response.json();

      if (jsonResponse.status === 1) {
        alert("File Uploaded");
      } else {
        console.log(jsonResponse);
        alert("Error uploading file");
      }
    } catch (error) {
      console.error("Error during file upload:", error);
      alert("An error occurred during file upload. Please try again later.");
    }
  };


 const handle_check = async () => {
     try {
        const payload1 = {
          rice_inline: block_data2,
          rice_inline_value: inline_value_rice,
          wheat_inline: block_dataWheat2,
          wheat_inline_value: inline_value_wheat,
        };
    
        console.log(block_data2, inline_value_rice, inline_value_wheat, block_dataWheat2);
    
        const response2 = await fetch(ProjectIp + "/Daily_Planner_Check", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload1),
        });
    
        const responseData1 = await response2.json(); // Parse response JSON
        console.log(responseData1); // Log the response data
    
        if (responseData1.status === 0) {
          alert("Distance is not within range. Please check again.");
        }
      } catch (error) {
        console.error("Error sending inputs:", error);
      } 
 }
  


  const handleSolve = async () => {
    document.getElementById("toggle").checked = true;
    alert("This action will take time, click OK to continue.");
    document.getElementById("console_").style.display="block"; 
    document.getElementById("console_").innerHTML+="Processing..."+'<br/>';
    if (Scenerio == "Scenerio 2") {
      setscn(true);
      setuploadst(true);
    }

    const payload = {
      TEFD: TEFD,
      origin_state: selectedOption,
      org_rhcode: subOption1,
      destination_state: selectedOption2,
      dest_rhcode: subOption2,
      block_data: block_data,
      Scenerio: Scenerio,
      confirmed_data: fixed_data,
      rice_origin: block_data3,
      rice_destination: rice_destination,
      rice_inline: block_data2,
      rice_inline_value: inline_value_rice,
      wheat_origin: block_dataWheat3,
      wheat_destination: wheat_destination,
      wheat_inline: block_dataWheat2,
      wheat_inline_value: inline_value_wheat,
    };
    try {
      const response = await fetch(ProjectIp + "/Daily_Planner", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        alert("Solution Done!, Now you can download results");
        setSolutionSolved(true);
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } catch (error) {
      console.error("Error sending inputs:", error);
    }    
    document.getElementById("console_").innerHTML+="Solution has been done"+'<br/>';
    document.getElementById("toggle").checked = false;
  };

  const fetchReservationId_Total_result = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Daily_Planner_S1", {
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
    fetch(ProjectIp + "/read_Daily_Planner_S2", {
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

  const handleDropdownChange3 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption3(selectedValue);
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

    setSubOptions3(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions3(dropdownOptions);
  };

  const handleDropdownChangeWheat3 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOptionWheat3(selectedValue);
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

    setSubOptionsWheat3(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptionsWheat3(dropdownOptions);
  };

  const handleDropdownChange5 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption5(selectedValue);
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

    setSubOptions5(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions5(dropdownOptions);
  };

  const handleDropdownChangeWheat5 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOptionWheat5(selectedValue);
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

    setSubOptionsWheat5(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptionsWheat5(dropdownOptions);
  };

  const handleDropdownChange6 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption6(selectedValue);
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

    setSubOptions6(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions6(dropdownOptions);
  };

  const handleDropdownChangeWheat6 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOptionWheat6(selectedValue);
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

    setSubOptionsWheat6(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptionsWheat6(dropdownOptions);
  };

  const handleDropdownChange4 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption4(selectedValue);
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

    setSubOptions4(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions4(dropdownOptions);
  };

  const handleDropdownChangeWheat4 = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOptionWheat4(selectedValue);
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

    setSubOptionsWheat4(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptionsWheat4(dropdownOptions);
  };

  const handleSubDropdownChange1 = (e) => {
    setSubOption1(e.target.value);
  };

  const handleSubDropdownChange2 = (e) => {
    setSubOption2(e.target.value);
  };
  const handleSubDropdownChange3 = (e) => {
    setSubOption3(e.target.value);
  };
  const handleSubDropdownChangeWheat3 = (e) => {
    setSubOptionWheat3(e.target.value);
  };

  const handleSubDropdownChange4 = (e) => {
    setSubOption4(e.target.value);
  };
  const handleSubDropdownChangeWheat4 = (e) => {
    setSubOptionWheat4(e.target.value);
  };

  const handleSubDropdownChange5 = (e) => {
    setSubOption5(e.target.value);
  };

  const handleSubDropdownChangeWheat5 = (e) => {
    setSubOptionWheat5(e.target.value);
  };

  const handleSubDropdownChange6 = (e) => {
    setSubOption6(e.target.value);
  };
  const handleSubDropdownChangeWheat6 = (e) => {
    setSubOptionWheat6(e.target.value);
  };

  const handleInlineValueWheat = (e) => {
    setInlineValueWheat(e.target.value);
  };
  const handleInlineValueRice = (e) => {
    setInlineValueRice(e.target.value);
  };

  const handleDropdownChange_fixed = async (e) => {
    const selectedValue_fixed = e.target.value;
    setSelectedOption_fixed(selectedValue_fixed);
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
      if (jsonData[i][1] == selectedValue_fixed) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));

    setSubOptions_fixed(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue_fixed);
    setSubOptions_fixed(dropdownOptions);
  };

  const handleDropdownChange2_fixed = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption2_fixed(selectedValue);
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

    setSubOptions2_fixed(dropdownOptions);
    console.log(jsonData[1][1], dropdownOptions, selectedValue);
    setSubOptions2_fixed(dropdownOptions);
  };

  const handleSubDropdownChange1_fixed = (e) => {
    setSubOption1_fixed(e.target.value);
  };

  const handleSubDropdownChange2_fixed = (e) => {
    setSubOption2_fixed(e.target.value);
  };

  const handleDeleteRow = (e) => {
    console.log(e);
    let block_data_ = block_data.filter((item) => item["id"] !== e);
    setBlockdata(block_data_);
  };
  const handleDeleteRow_fixed = (e) => {
    console.log(e);
    let fixed_data_ = fixed_data.filter((item) => item["id"] !== e);
    setFixeddata(fixed_data_);
  };
  const handleDeleteRow_inline = (e) => {
    console.log(e);
    let fixed_data_ = block_data2.filter((item) => item["id"] !== e);
    setBlockdata2(fixed_data_);
  };
  const handleDeleteRow_inlineWheat = (e) => {
    console.log(e);
    let fixed_data_ = block_dataWheat2.filter((item) => item["id"] !== e);
    setBlockdataWheat2(fixed_data_);
  };
  const handleDeleteRow_Rice_s = (e) => {
    console.log(e);
    let block_data3_ = block_data3.filter((item) => item["id"] !== e);
    setBlockdata3(block_data3_);
  };

  const handleDeleteRow_Wheat_s = (e) => {
    console.log(e);
    let block_data3_ = block_dataWheat3.filter((item) => item["id"] !== e);
    setBlockdataWheat3(block_data3_);
  };

  const handleDeleteRow_Rice__dest = (e) => {
    console.log(e);
    let rice_destination_ = rice_destination.filter((item) => item["id"] !== e);
    setRiceDestination(rice_destination_);
  };

  const handleDeleteRow_Wheat__dest = (e) => {
    console.log(e);
    let wheat_destination_ = wheat_destination.filter(
      (item) => item["id"] !== e
    );
    setWheatDestination(wheat_destination_);
  };

  const addConstraint = () => {
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (selectedOption && subOption1 && selectedOption2 && subOption2) {
      setBlockdata((data) => [
        ...data,
        {
          origin_state: selectedOption,
          origin_railhead: subOption1,
          destination_state: selectedOption2,
          destination_railhead: subOption2,
          id: Date.now(),
        },
      ]);
      console.log(block_data3);
      setSelectedOption("default");
      setSelectedOption2("default");
      setSubOptions([]);
      setSubOptions2([]);
      document.getElementById("console_").style.display="block"; 
      // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML+="Route from "+subOption1+" to " + subOption2 +" has been blocked"+'<br/>';
    }
  };

<<<<<<< Updated upstream
  const addConstraint2 = () => {
    // handle_check();
=======
  const addConstraint2 = async () => {
>>>>>>> Stashed changes
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (selectedOption5 && subOption5 && selectedOption6 && subOption6) {
      setBlockdata2((data) => [
        ...data,
        {
          origin_state: selectedOption5,
          origin_railhead: subOption5,
          destination_state: selectedOption6,
          destination_railhead: subOption6,
          id: Date.now(),
        },
      ]);
<<<<<<< Updated upstream
=======
      var data = block_data2;
      var data1 = block_dataWheat2;
      data.push({
        origin_state: selectedOption5,
          origin_railhead: subOption5,
          destination_state: selectedOption6,
          destination_railhead: subOption6,
          id: Date.now()
      })
      console.log(data);
>>>>>>> Stashed changes
      setSelectedOption5("default");
      setSelectedOption6("default");
      setSubOptions5([]);
      setSubOptions6([]);
<<<<<<< Updated upstream
      console.log(block_data2);
=======

      // await handle_check();
      try {
        const payload1 = {
          rice_inline: data,
          rice_inline_value: inline_value_rice,
          wheat_inline: data1,
          wheat_inline_value: inline_value_wheat,
        };
    
        console.log(block_data2, inline_value_rice, inline_value_wheat, block_dataWheat2);
    
        const response2 = await fetch(ProjectIp + "/Daily_Planner_Check", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload1),
        });
    
        const responseData1 = await response2.json(); // Parse response JSON
        console.log(responseData1); // Log the response data
    
        if (responseData1.status === 0) {
          alert("Distance is not within range. Please check again.");
        }
      } catch (error) {
        console.error("Error sending inputs:", error);
      } 
>>>>>>> Stashed changes
    }
    document.getElementById("console_").style.display="block"; 
    // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
    document.getElementById("console_").innerHTML+="New Inline details has been added for rice"+'<br/>';
  };

  const addConstraintWheat2 = () => {
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (
      selectedOptionWheat5 &&
      subOptionWheat5 &&
      selectedOptionWheat6 &&
      subOptionWheat6
    ) {
      setBlockdataWheat2((data) => [
        ...data,
        {
          origin_state: selectedOptionWheat5,
          origin_railhead: subOptionWheat5,
          destination_state: selectedOptionWheat6,
          destination_railhead: subOptionWheat6,
          id: Date.now(),
        },
      ]);
      console.log(block_dataWheat2);
      setSelectedOption5("default");
      setSelectedOption6("default");
      setSubOptions5([]);
      setSubOptions6([]);
    }
    document.getElementById("console_").style.display="block"; 
    // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
    document.getElementById("console_").innerHTML+="New Inline details has been added for wheat"+'<br/>';
  };

  const addConstraint3 = () => {
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (selectedOption3 && subOption3) {
      setBlockdata3((data) => [
        ...data,
        {
          origin_state: selectedOption3,
          origin_railhead: subOption3,
          id: Date.now(),
        },
      ]);
      setSelectedOption3("default");
      setSubOptions3([]);
      document.getElementById("console_").style.display="block"; 
      // document.getElementById("console_").innerHTML+="Origin railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML+="New origin railhead has been added for rice"+'<br/>';
    }
  };

  const addConstraintWheat3 = () => {
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (selectedOptionWheat3 && subOptionWheat3) {
      setBlockdataWheat3((data) => [
        ...data,
        {
          origin_state: selectedOptionWheat3,
          origin_railhead: subOptionWheat3,
          id: Date.now(),
        },
      ]);
      setSelectedOptionWheat3("default");
      setSubOptionsWheat3([]);
      document.getElementById("console_").style.display="block"; 
      // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML+="New origin railhead has been added for wheat"+'<br/>';
    }
  };

  const addConstraint4 = () => {
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (selectedOption4 && subOption4) {
      setRiceDestination((data) => [
        ...data,
        {
          origin_state: selectedOption4,
          origin_railhead: subOption4,
          id: Date.now(),
        },
      ]);
      setSelectedOption4("default");
      setSubOptions4([]);
      document.getElementById("console_").style.display="block"; 
      // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML+="New destination railhead has been added for rice"+'<br/>';
    }
  };
  const addConstraintWheat4 = () => {
    // console.log(selectedOption, subOption1, selectedOption2, subOption2);
    if (selectedOptionWheat4 && subOptionWheat4) {
      setWheatDestination((data) => [
        ...data,
        {
          origin_state: selectedOptionWheat4,
          origin_railhead: subOptionWheat4,
          id: Date.now(),
        },
      ]);
      setSelectedOptionWheat4("default");
      setSubOptionsWheat4([]);
      document.getElementById("console_").style.display="block"; 
      // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML+="New destination railhead has been added for wheat"+'<br/>';
    }
  };

  const addConstraint_fixed = () => {
    if (
      selectedOption_fixed &&
      subOption1_fixed &&
      selectedOption2_fixed &&
      subOption2_fixed &&
      commodity_fixed &&
      value_fixed
    ) {
      setFixeddata((data) => [
        ...data,
        {
          origin_state: selectedOption_fixed,
          origin_railhead: subOption1_fixed,
          destination_state: selectedOption2_fixed,
          destination_railhead: subOption2_fixed,
          commodity: commodity_fixed,
          value: value_fixed,
          id: Date.now(),
        },
      ]);
      console.log(fixed_data);
      setSelectedOption_fixed("default");
      setSelectedOption2_fixed("default");
      setSubOptions_fixed([]);
      setSubOptions2_fixed([]);
      document.getElementById("console_").style.display="block"; 
      // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML+="Route from "+subOption1_fixed+" to " + subOption2_fixed +" has been fixed for "+commodity_fixed+" with value "+ value_fixed+'<br/>';
    }
  };

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
      saveAs(excelBlob, "Daily_Movement_Scenerio1.xlsx");
    }
  };

  const exportToExcel2 = () => {
    fetchReservationId_Revelant_result();
    if (Relevant_result == null) {
      window.alert("Fetching Result, Please Wait");
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
      saveAs(excelBlob, "Daily_Movement_results_Scenerio2.xlsx");
    }
  };

  const buttonStyle = {
    border: updateExcel ? "4px solid rgba(235, 171, 68)" : "2px solid black",
    padding: "5px",
  };

  const buttonStyle2 = {
    border: updateExcel2 ? "4px solid rgba(235, 171, 68)" : "2px solid black",
    padding: "5px",
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
                {/* <form
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
                            onChange={handleFileChange}
                            id="uploadFile"
                            name="uploadFile"
                            defaultValue=""
                            required=""
                          />
                        </div>
                        <span className="help-block" style={{ color: "black" }}>
                          Choose Data Template
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-3">
                    {setuploadst && (
                      <div>
                        <img
                          className="upload_class"
                          src={background1}
                          id="uploadConfig"
                          onClick={handleUploadConfig}
                          disabled={!fileSelected}
                        />
                      </div>
                    )}
                    {!setuploadst && (
                      <div>
                        <img
                          className="upload_class"
                          src={background1}
                          id="uploadConfig"
                          onClick={handleUploadConfig1}
                          disabled={!fileSelected}
                        />
                      </div>
                    )}
                    <div style={{ marginTop: "-25px" }}>Click here</div>
                  </div>
                </form> */}
              </div>
              <br />
              <br />
              <div style={{ display: "flex", marginLeft: "245px" }}>
                {/* {fileSelected && ( */}
                <div style={{ marginTop: "-20px" }}>
                  <button style={buttonStyle} onClick={() => update_excel()}>
                    Update Template for Scenario 1
                  </button>
                </div>
                {/* )} */}
                {/* {updateExcel && ( */}
                <div style={{ marginLeft: "150px", marginTop: "-20px" }}>
                  <button style={buttonStyle2} onClick={() => update_excel2()}>
                    Update Template for Scenario 2
                  </button>
                </div>
                {/* )} */}
              </div>
              {(updateExcel || updateExcel2) && (
                <div style={{ marginLeft: "480px" }}>
                  <br />
                  <button
                    style={{ padding: "5px" }}
                    onClick={() => save_excel()}
                  >
                    Save changes
                  </button>
                </div>
              )}
              {activeSheetName &&
                (updateExcel || updateExcel2) &&
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
              <div style={{ margin:'10px', marginLeft:'20%',width:'60%', border:'2px dashed black', padding:'10px', display:'none'}} id="console_">
                
              </div>
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
                      onChange={(e) => {set_TEFD(e.target.value); document.getElementById("console_").style.display="block"; document.getElementById("console_").innerHTML+="You have selected the matrix system as "+e.target.value+'<br/>';}}
                      style={{ marginLeft: "547px" }}
                    >
                      <option value="">Select Matrix System</option>
                      <option value="NON-TEFD">Non-TEFD</option>
                      <option value="TEFD">TEFD</option>
                      <option value="Non-TEFD+TC">Non-TEFD + TC</option>
                      <option value="TEFD+TC">TEFD + TC</option>
                    </select>
                  </label>
                  <label>
                    <strong
                      style={{
                        fontSize: "20px",
                        marginLeft: "15px",
                        color: "#9d0921",
                      }}
                    >
                      Select Scenerio
                    </strong>
                    <select
                      value={Scenerio}
                      onChange={(e) => {set_Scenerio(e.target.value);  document.getElementById("console_").style.display="block"; document.getElementById("console_").innerHTML+="You have selected the scenario as "+e.target.value+'<br/>';}}
                      style={{ marginLeft: "600px" }}
                    >
                      <option value="">Select Scenario</option>
                      <option value="Scenerio 1">Scenerio 1</option>
                      <option value="Scenerio 2">Scenerio 2</option>
                    </select>
                  </label>
                  <br />
                  <br />
                  <div>
                    <p style={{ margin: 0, padding: 0 }}>
                      <strong
                        style={{
                          color: "#9d0921",
                          fontSize: "20px",
                          marginLeft: "15px",
                        }}
                      >
                        For Rice:
                      </strong>
                    </p>
                    <br />
                    <div style={{ display: "flex", marginLeft: "20px" }}>
                      {/* <label htmlFor="origin_state"> */}
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Origin State:
                        </strong>
                        <select
                          style={{ width: "200px", padding: "5px" }}
                          
                          onChange={handleDropdownChange3}
                          value={selectedOption3}
                        >
                          <option value="default">Select Origin State</option>
                          <option value="Andhra Pradesh">Andhra Pradesh</option>
                          <option value="Bihar">Bihar</option>
                          <option value="Chattisgarh">Chattisgarh</option>
                          <option value="Goa">Goa</option>
                          <option value="Gujarat">Gujarat</option>
                          <option value="Haryana">Haryana</option>
                          <option value="Jammu & Kashmir">
                            Jammu & Kashmir
                          </option>
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

                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Origin Railhead
                        </strong>
                        <select
                          
                          style={{ width: "200px", padding: "5px" }}
                          onChange={handleSubDropdownChange3}
                          value={subOption3}
                        >
                          {subOptions3.map((option) => (
                            <option key={option.value} value={option.value}>
                              {option.label}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div
                        style={{
                          padding: "2px",
                          margin: "2px",
                          marginLeft: "500px",
                          width: "70px",
                          background: "orange",
                          cursor: "pointer",
                          height: "40px",
                          marginTop: "-5px",
                        }}
                        onClick={addConstraint3}
                      >
                        <p style={{ textAlign: "center", marginTop: "10px" }}>
                          Add
                        </p>
                      </div>
                    </div>

                    <br />

                    {block_data3.length != 0 && (
                      <div>
                        <table>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Delete
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {block_data3.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>{item.origin_railhead}</td>

                                <td>
                                  <span
                                    style={{
                                      cursor: "pointer",
                                      color: "#ff0000",
                                      fontSize: "1.2rem",
                                    }}
                                    onClick={() =>
                                      handleDeleteRow_Rice_s(item.id)
                                    }
                                    title="Delete"
                                  >
                                    &times;
                                  </span>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}

                    <br />

                    <div style={{ display: "flex", marginLeft: "20px" }}>
                      {/* <label htmlFor="origin_state"> */}
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Destination State:
                        </strong>
                        <select
                          style={{ width: "200px", padding: "5px" }}
                          id="destination"
                          onChange={handleDropdownChange4}
                          value={selectedOption4}
                        >
                          <option value="default">
                            Select Destination State
                          </option>
                          <option value="Andhra Pradesh">Andhra Pradesh</option>
                          <option value="Bihar">Bihar</option>
                          <option value="Chattisgarh">Chattisgarh</option>
                          <option value="Goa">Goa</option>
                          <option value="Gujarat">Gujarat</option>
                          <option value="Haryana">Haryana</option>
                          <option value="Jammu & Kashmir">
                            Jammu & Kashmir
                          </option>
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

                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Destination Railhead
                        </strong>
                        <select
                          
                          style={{ width: "200px", padding: "5px" }}
                          onChange={handleSubDropdownChange4}
                          value={subOption4}
                        >
                          {subOptions4.map((option) => (
                            <option key={option.value} value={option.value}>
                              {option.label}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div
                        style={{
                          padding: "2px",
                          margin: "2px",
                          marginLeft: "440px",
                          width: "70px",
                          background: "orange",
                          cursor: "pointer",
                          height: "40px",
                          marginTop: "-5px",
                        }}
                        onClick={addConstraint4}
                      >
                        <p style={{ textAlign: "center", marginTop: "10px" }}>
                          Add
                        </p>
                      </div>
                    </div>
                    <br />
                    <div>
                      {rice_destination.length != 0 && (
                        <div>
                          <table>
                            <thead>
                              <tr style={{ margin: "auto" }}>
                                <th style={{ padding: "10px", width: "15%" }}>
                                  Destination State
                                </th>
                                <th style={{ padding: "10px", width: "15%" }}>
                                  Destination Railhead
                                </th>
                                <th style={{ padding: "10px", width: "15%" }}>
                                  Delete
                                </th>
                              </tr>
                            </thead>
                            <tbody>
                              {rice_destination.map((item) => (
                                <tr key={item.id}>
                                  <td>{item.origin_state}</td>
                                  <td>{item.origin_railhead}</td>

                                  <td>
                                    <span
                                      style={{
                                        cursor: "pointer",
                                        color: "#ff0000",
                                        fontSize: "1.2rem",
                                      }}
                                      onClick={() =>
                                        handleDeleteRow_Rice__dest(item.id)
                                      }
                                      title="Delete"
                                    >
                                      &times;
                                    </span>
                                  </td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      )}
                    </div>
                    <br />
                    <br />
                    <div>
                      <div style={{ display: "flex", marginLeft: "20px" }}>
                        {/* <label htmlFor="origin_state"> */}
                        <div>
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            
                            onChange={handleDropdownChange5}
                            value={selectedOption5}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
                            <option value="Bihar">Bihar</option>
                            <option value="Chattisgarh">Chattisgarh</option>
                            <option value="Goa">Goa</option>
                            <option value="Gujarat">Gujarat</option>
                            {/* <option value="Haryana">Haryana</option> */}
                            <option value="Jammu & Kashmir">
                              Jammu & Kashmir
                            </option>
                            <option value="Jharkhand">Jharkhand</option>
                            <option value="Karnataka">Karnataka</option>
                            <option value="Kerala">Kerala</option>
                            {/* <option value="MP">Madhya Pradesh</option> */}
                            <option value="Maharashtra">Maharashtra</option>
                            <option value="NE">North East</option>
                            <option value="Odisha">Odisha</option>
                            {/* <option value="Punjab">Punjab</option> */}
                            <option value="Rajasthan">Rajasthan</option>
                            <option value="Tamil Nadu">Tamil Nadu</option>
                            <option value="Telangana">Telangana</option>
                            <option value="UP">Uttar Pradesh</option>
                            <option value="Uttarakhand">Uttarakhand</option>
                            <option value="West Bengal">West Bengal</option>
                          </select>
                        </div>

                        <div>
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleSubDropdownChange5}
                            value={subOption5}
                          >
                            {subOptions5.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        {/* </label> */}
                        <div>
                          {/* <label htmlFor="deficit_state"> */}
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            
                            onChange={handleDropdownChange6}
                            value={selectedOption6}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
                            <option value="Bihar">Bihar</option>
                            <option value="Chattisgarh">Chattisgarh</option>
                            <option value="Goa">Goa</option>
                            <option value="Gujarat">Gujarat</option>
                            {/* <option value="Haryana">Haryana</option> */}
                            <option value="Jammu & Kashmir">
                              Jammu & Kashmir
                            </option>
                            <option value="Jharkhand">Jharkhand</option>
                            <option value="Karnataka">Karnataka</option>
                            <option value="Kerala">Kerala</option>
                            {/* <option value="MP">Madhya Pradesh</option> */}
                            <option value="Maharashtra">Maharashtra</option>
                            <option value="NE">North East</option>
                            <option value="Odisha">Odisha</option>
                            {/* <option value="Punjab">Punjab</option> */}
                            <option value="Rajasthan">Rajasthan</option>
                            <option value="Tamil Nadu">Tamil Nadu</option>
                            <option value="Telangana">Telangana</option>
                            <option value="UP">Uttar Pradesh</option>
                            <option value="Uttarakhand">Uttarakhand</option>
                            <option value="West Bengal">West Bengal</option>
                          </select>
                        </div>
                        {/* </label> */}
                        {/* <label htmlFor="deficit_railhead"> */}
                        <div>
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleSubDropdownChange6}
                            value={subOption6}
                          >
                            {subOptions6.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        {/* </label> */}
                        <div
                          style={{
                            padding: "5px",
                            margin: "2px",
                            float: "right",
                            width: "100px",
                            background: "orange",
                            padding: "auto",
                            cursor: "pointer",
                          }}
                          onClick={addConstraint2}
                        >
                          <p style={{ textAlign: "center", marginTop: "15px" }}>
                            Add
                          </p>
                        </div>
                      </div>
                    </div>
                    <br/>
                    <div style={{ marginLeft: "15px" }}>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Enter Inline Value
                      </strong>
                      <input
                        type="number"
                        value={inline_value_rice}
                        onChange={(e) => setInlineValueRice(e.target.value)}
                        style={{
                          marginLeft: "40px",
                          width: "200px",
                          padding: "5px",
                        }}
                      />
                    </div>
                    <br />
                    {block_data2.length != 0 && (
                      <div>
                        {/* <div
                      style={{
                        fontSize: "20px",
                        fontWeight: "700",
                        textAlign: "center",
                      }}
                    >
                      Route Block
                    </div> */}
                        <table>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Delete
                              </th>
                            </tr>
                            {/* <tr  style={{ padding: "10px", width: "100%" , textAlign:'center'}}>
                      <div style={{textAlign:'center', width:'100%'}}>Routes Block</div></tr> */}
                          </thead>
                          <tbody>
                            {/* <tr style={{ margin: "auto" }}>
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
                      <th style={{ padding: "10px", width: "15%" }}>Delete</th>
                    </tr> */}
                            {block_data2.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>{item.origin_railhead}</td>
                                <td>{item.destination_state}</td>
                                <td>{item.destination_railhead}</td>
                                <td>
                                  <span
                                    style={{
                                      cursor: "pointer",
                                      color: "#ff0000",
                                      fontSize: "1.2rem",
                                    }}
                                    onClick={() =>
                                      handleDeleteRow_inline(item.id)
                                    }
                                    title="Delete"
                                  >
                                    &times;
                                  </span>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}
                  </div>
                  <br />
                  <div>
                    <p style={{ margin: 0, padding: 0 }}>
                      <strong
                        style={{
                          color: "#9d0921",
                          fontSize: "20px",
                          marginLeft: "15px",
                        }}
                      >
                        For Wheat:
                      </strong>
                    </p>
                    <br />
                    <div style={{ display: "flex", marginLeft: "20px" }}>
                      {/* <label htmlFor="origin_state"> */}
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Origin State:
                        </strong>
                        <select
                          style={{ width: "200px", padding: "5px" }}
                          
                          onChange={handleDropdownChangeWheat3}
                          value={selectedOptionWheat3}
                        >
                          <option value="default">Select Origin State</option>
                          <option value="Andhra Pradesh">Andhra Pradesh</option>
                          <option value="Bihar">Bihar</option>
                          <option value="Chattisgarh">Chattisgarh</option>
                          <option value="Goa">Goa</option>
                          <option value="Gujarat">Gujarat</option>
                          <option value="Haryana">Haryana</option>
                          <option value="Jammu & Kashmir">
                            Jammu & Kashmir
                          </option>
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

                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Origin Railhead
                        </strong>
                        <select
                          
                          style={{ width: "200px", padding: "5px" }}
                          onChange={handleSubDropdownChangeWheat3}
                          value={subOptionWheat3}
                        >
                          {subOptionsWheat3.map((option) => (
                            <option key={option.value} value={option.value}>
                              {option.label}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div
                        style={{
                          padding: "2px",
                          margin: "2px",
                          marginLeft: "500px",
                          width: "70px",
                          background: "orange",
                          cursor: "pointer",
                          height: "40px",
                          marginTop: "-5px",
                        }}
                        onClick={addConstraintWheat3}
                      >
                        <p style={{ textAlign: "center", marginTop: "10px" }}>
                          Add
                        </p>
                      </div>
                    </div>

                    <br />

                    {block_dataWheat3.length != 0 && (
                      <div>
                        <table>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Origin Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Delete
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {block_dataWheat3.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>{item.origin_railhead}</td>

                                <td>
                                  <span
                                    style={{
                                      cursor: "pointer",
                                      color: "#ff0000",
                                      fontSize: "1.2rem",
                                    }}
                                    onClick={() =>
                                      handleDeleteRow_Wheat_s(item.id)
                                    }
                                    title="Delete"
                                  >
                                    &times;
                                  </span>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}

                    <br />

                    <div style={{ display: "flex", marginLeft: "20px" }}>
                      {/* <label htmlFor="origin_state"> */}
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Destination State:
                        </strong>
                        <select
                          style={{ width: "200px", padding: "5px" }}
                          id="destination"
                          onChange={handleDropdownChangeWheat4}
                          value={selectedOptionWheat4}
                        >
                          <option value="default">
                            Select Destination State
                          </option>
                          <option value="Andhra Pradesh">Andhra Pradesh</option>
                          <option value="Bihar">Bihar</option>
                          <option value="Chattisgarh">Chattisgarh</option>
                          <option value="Goa">Goa</option>
                          <option value="Gujarat">Gujarat</option>
                          <option value="Haryana">Haryana</option>
                          <option value="Jammu & Kashmir">
                            Jammu & Kashmir
                          </option>
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

                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Destination Railhead
                        </strong>
                        <select
                          
                          style={{ width: "200px", padding: "5px" }}
                          onChange={handleSubDropdownChangeWheat4}
                          value={subOptionWheat4}
                        >
                          {subOptionsWheat4.map((option) => (
                            <option key={option.value} value={option.value}>
                              {option.label}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div
                        style={{
                          padding: "2px",
                          margin: "2px",
                          marginLeft: "440px",
                          width: "70px",
                          background: "orange",
                          cursor: "pointer",
                          height: "40px",
                          marginTop: "-5px",
                        }}
                        onClick={addConstraintWheat4}
                      >
                        <p style={{ textAlign: "center", marginTop: "10px" }}>
                          Add
                        </p>
                      </div>
                    </div>
                    <br />
                    <div>
                      {wheat_destination.length != 0 && (
                        <div>
                          <table>
                            <thead>
                              <tr style={{ margin: "auto" }}>
                                <th style={{ padding: "10px", width: "15%" }}>
                                  Destination State
                                </th>
                                <th style={{ padding: "10px", width: "15%" }}>
                                  Destination Railhead
                                </th>
                                <th style={{ padding: "10px", width: "15%" }}>
                                  Delete
                                </th>
                              </tr>
                            </thead>
                            <tbody>
                              {wheat_destination.map((item) => (
                                <tr key={item.id}>
                                  <td>{item.origin_state}</td>
                                  <td>{item.origin_railhead}</td>

                                  <td>
                                    <span
                                      style={{
                                        cursor: "pointer",
                                        color: "#ff0000",
                                        fontSize: "1.2rem",
                                      }}
                                      onClick={() =>
                                        handleDeleteRow_Wheat__dest(item.id)
                                      }
                                      title="Delete"
                                    >
                                      &times;
                                    </span>
                                  </td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      )}
                    </div>
                    <br />
                    <br />
                    <div>
                      <div style={{ display: "flex", marginLeft: "20px" }}>
                        {/* <label htmlFor="origin_state"> */}
                        <div>
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleDropdownChangeWheat5}
                            value={selectedOptionWheat5}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
                            <option value="Bihar">Bihar</option>
                            <option value="Chattisgarh">Chattisgarh</option>
                            <option value="Goa">Goa</option>
                            <option value="Gujarat">Gujarat</option>
                            {/* <option value="Haryana">Haryana</option> */}
                            <option value="Jammu & Kashmir">
                              Jammu & Kashmir
                            </option>
                            <option value="Jharkhand">Jharkhand</option>
                            <option value="Karnataka">Karnataka</option>
                            <option value="Kerala">Kerala</option>
                            {/* <option value="MP">Madhya Pradesh</option> */}
                            <option value="Maharashtra">Maharashtra</option>
                            <option value="NE">North East</option>
                            <option value="Odisha">Odisha</option>
                            {/* <option value="Punjab">Punjab</option> */}
                            <option value="Rajasthan">Rajasthan</option>
                            <option value="Tamil Nadu">Tamil Nadu</option>
                            <option value="Telangana">Telangana</option>
                            <option value="UP">Uttar Pradesh</option>
                            <option value="Uttarakhand">Uttarakhand</option>
                            <option value="West Bengal">West Bengal</option>
                          </select>
                        </div>

                        <div>
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleSubDropdownChangeWheat5}
                            value={subOptionWheat5}
                          >
                            {subOptionsWheat5.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        {/* </label> */}
                        <div>
                          {/* <label htmlFor="deficit_state"> */}
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            
                            onChange={handleDropdownChangeWheat6}
                            value={selectedOptionWheat6}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
                            <option value="Bihar">Bihar</option>
                            <option value="Chattisgarh">Chattisgarh</option>
                            <option value="Goa">Goa</option>
                            <option value="Gujarat">Gujarat</option>
                            {/* <option value="Haryana">Haryana</option> */}
                            <option value="Jammu & Kashmir">
                              Jammu & Kashmir
                            </option>
                            <option value="Jharkhand">Jharkhand</option>
                            <option value="Karnataka">Karnataka</option>
                            <option value="Kerala">Kerala</option>
                            {/* <option value="MP">Madhya Pradesh</option> */}
                            <option value="Maharashtra">Maharashtra</option>
                            <option value="NE">North East</option>
                            <option value="Odisha">Odisha</option>
                            {/* <option value="Punjab">Punjab</option> */}
                            <option value="Rajasthan">Rajasthan</option>
                            <option value="Tamil Nadu">Tamil Nadu</option>
                            <option value="Telangana">Telangana</option>
                            <option value="UP">Uttar Pradesh</option>
                            <option value="Uttarakhand">Uttarakhand</option>
                            <option value="West Bengal">West Bengal</option>
                          </select>
                        </div>
                        {/* </label> */}
                        {/* <label htmlFor="deficit_railhead"> */}
                        <div>
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleSubDropdownChangeWheat6}
                            value={subOptionWheat6}
                          >
                            {subOptionsWheat6.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        {/* </label> */}
                        <div
                          style={{
                            padding: "5px",
                            margin: "2px",
                            float: "right",
                            width: "100px",
                            background: "orange",
                            padding: "auto",
                            cursor: "pointer",
                          }}
                          onClick={addConstraintWheat2}
                        >
                          <p style={{ textAlign: "center", marginTop: "15px" }}>
                            Add
                          </p>
                        </div>
                      </div>
                    </div>
                    <br />
                    <br/>
                    <div style={{ marginLeft: "15px" }}>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Enter Inline Value
                      </strong>
                      <input
                        type="number"
                        value={inline_value_wheat}
                        onChange={(e) => setInlineValueWheat(e.target.value)}
                        style={{
                          marginLeft: "40px",
                          width: "200px",
                          padding: "5px",
                        }}
                      />
                    </div>
                    {block_dataWheat2.length != 0 && (
                      <div>
                        {/* <div
                      style={{
                        fontSize: "20px",
                        fontWeight: "700",
                        textAlign: "center",
                      }}
                    >
                      Route Block
                    </div> */}
                        <table>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline State
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Inline Railhead
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Delete
                              </th>
                            </tr>
                            {/* <tr  style={{ padding: "10px", width: "100%" , textAlign:'center'}}>
                      <div style={{textAlign:'center', width:'100%'}}>Routes Block</div></tr> */}
                          </thead>
                          <tbody>
                            {block_dataWheat2.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>{item.origin_railhead}</td>
                                <td>{item.destination_state}</td>
                                <td>{item.destination_railhead}</td>
                                <td>
                                  <span
                                    style={{
                                      cursor: "pointer",
                                      color: "#ff0000",
                                      fontSize: "1.2rem",
                                    }}
                                    onClick={() =>
                                      handleDeleteRow_inlineWheat(item.id)
                                    }
                                    title="Delete"
                                  >
                                    &times;
                                  </span>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}
                  </div>
                  <br />
                  <p style={{ margin: 0, padding: 0 }}>
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
                  <br />
                  <div style={{ display: "flex", marginLeft: "20px" }}>
                    {/* <label htmlFor="origin_state"> */}
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Origin State
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
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

                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Origin Railhead
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
                        onChange={handleSubDropdownChange1}
                        value={subOption1}
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
                      {/* <label htmlFor="deficit_state"> */}
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Destination State
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
                        onChange={handleDropdownChange2}
                        value={selectedOption2}
                      >
                        <option value="default">
                          Select Destination State
                        </option>
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
                    {/* </label> */}
                    {/* <label htmlFor="deficit_railhead"> */}
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Destination Railhead
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
                        onChange={handleSubDropdownChange2}
                        value={subOption2}
                      >
                        {subOptions2.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    </div>
                    {/* </label> */}
                    <div
                      style={{
                        padding: "5px",
                        margin: "2px",
                        float: "right",
                        width: "100px",
                        background: "orange",
                        padding: "auto",
                        cursor: "pointer",
                      }}
                      onClick={addConstraint}
                    >
                      <p style={{ textAlign: "center", marginTop: "20px" }}>
                        Add
                      </p>
                    </div>
                  </div>
                  <br />
                  {!solutionSolved && block_data.length != 0 && (
                    <div>
                      <table>
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
                              Delete
                            </th>
                          </tr>
                          {/* <tr  style={{ padding: "10px", width: "100%" , textAlign:'center'}}>
                      <div style={{textAlign:'center', width:'100%'}}>Routes Block</div></tr> */}
                        </thead>
                        <tbody>
                          {/* <tr style={{ margin: "auto" }}>
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
                      <th style={{ padding: "10px", width: "15%" }}>Delete</th>
                    </tr> */}
                          {block_data.map((item) => (
                            <tr key={item.id}>
                              <td>{item.origin_state}</td>
                              <td>{item.origin_railhead}</td>
                              <td>{item.destination_state}</td>
                              <td>{item.destination_railhead}</td>
                              <td>
                                <span
                                  style={{
                                    cursor: "pointer",
                                    color: "#ff0000",
                                    fontSize: "1.2rem",
                                  }}
                                  onClick={() => handleDeleteRow(item.id)}
                                  title="Delete"
                                >
                                  &times;
                                </span>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                  <br />
                  <br />
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
                  <br />
                  <div style={{ display: "flex", marginLeft: "20px" }}>
                    {/* <label htmlFor="origin_state"> */}
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Origin State
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
                        
                        onChange={handleDropdownChange_fixed}
                        value={selectedOption_fixed}
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
                    {/* </label> */}
                    {/* <label htmlFor="origin_railhead"> */}
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Origin Railhead
                      </strong>
                      <select
                        
                        style={{ width: "200px", padding: "5px" }}
                        onChange={handleSubDropdownChange1_fixed}
                        value={subOption1_fixed}
                      >
                        {subOptions_fixed.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    </div>
                    {/* </label> */}
                    <div>
                      {/* <label htmlFor="deficit_state"> */}
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Destination State
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
                        
                        onChange={handleDropdownChange2_fixed}
                        value={selectedOption2_fixed}
                      >
                        <option value="default">
                          Select Destination State
                        </option>
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
                    {/* </label> */}
                    {/* <label htmlFor="deficit_railhead"> */}
                    <div>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Destination Railhead
                      </strong>
                      <select
                        style={{ width: "200px", padding: "5px" }}
                        onChange={handleSubDropdownChange2_fixed}
                        value={subOption2_fixed}
                      >
                        {subOptions2_fixed.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    </div>
                    {/* </label> */}
                    <div
                      style={{
                        padding: "5px",
                        margin: "2px",
                        float: "right",
                        width: "100px",
                        background: "orange",
                        padding: "auto",
                        cursor: "pointer",
                        marginTop: "50px",
                      }}
                      onClick={addConstraint_fixed}
                    >
                      <p style={{ textAlign: "center", marginTop: "20px" }}>
                        Add
                      </p>
                    </div>
                  </div>
                  <div
                    style={{
                      display: "flex",
                      marginLeft: "20px",
                      marginTop: "-20px",
                    }}
                  >
                    <strong>Select Commodity</strong>
                    <select
                      value={commodity_fixed}
                      onChange={(e) => setCommodity_fixed(e.target.value)}
                      style={{
                        marginLeft: "40px",
                        width: "200px",
                        padding: "5px",
                      }}
                    >
                      <option value="">Select Commodity</option>
                      <option value="RICE">Rice</option>
                      <option value="WHEAT">Wheat</option>
                    </select>
                    <div style={{ marginLeft: "50px" }}>
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Enter Value
                      </strong>
                      <input
                        type="number"
                        value={value_fixed}
                        onChange={(e) => setValue_fixed(e.target.value)}
                        style={{
                          marginLeft: "40px",
                          width: "200px",
                          padding: "5px",
                        }}
                      />
                    </div>
                  </div>
                  <br />
                  {!solutionSolved && fixed_data.length != 0 && (
                    <div>
                      <table>
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
                            <th style={{ padding: "10px", width: "15%" }}></th>
                            <th style={{ padding: "10px", width: "15%" }}>
                              Delete
                            </th>
                          </tr>
                          {/* <tr  style={{ padding: "10px", width: "100%" , textAlign:'center'}}>
                      <div style={{textAlign:'center', width:'100%'}}>Routes Block</div></tr> */}
                        </thead>
                        <tbody>
                          {/* <tr style={{ margin: "auto" }}>
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
                      <th style={{ padding: "10px", width: "15%" }}>Delete</th>
                    </tr> */}
                          {fixed_data.map((item) => (
                            <tr key={item.id}>
                              <td>{item.origin_state}</td>
                              <td>{item.origin_railhead}</td>
                              <td>{item.destination_state}</td>
                              <td>{item.destination_railhead}</td>
                              <td>{item.commodity}</td>
                              <td>{item.value}</td>
                              <td>
                                <span
                                  style={{
                                    cursor: "pointer",
                                    color: "#ff0000",
                                    fontSize: "1.2rem",
                                  }}
                                  onClick={() => handleDeleteRow_fixed(item.id)}
                                  title="Delete"
                                >
                                  &times;
                                </span>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                  <br />
                  <br />
                </form>

                <div style={{ fontSize: "20px", fontWeight: "700" }}>
                  <i className="fa fa-list-alt" aria-hidden="true"></i> Optimal
                  Plan
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
                {/* <div>
              <br/>
                    <DynamicTable/>
                  </div> */}
                <br />
                {solutionSolved && (
                  <div>
                    {scn && (
                      <div>
                        <button
                          style={{ color: "white", marginLeft: "15px" }}
                          className="btn btn-danger dropdown-toggle"
                          onClick={() => exportToExcel2()}
                        >
                          <i className="fa fa-bars"></i> Download
                          Railhead-Railhead Detailed Plan
                        </button>
                      </div>
                    )}
                    {!scn && (
                      <div>
                        <button
                          style={{ color: "white", marginLeft: "15px" }}
                          className="btn btn-danger dropdown-toggle"
                          onClick={() => exportToExcel1()}
                        >
                          <i className="fa fa-bars"></i> Download
                          Railhead-Railhead Detailed Plan
                        </button>
                      </div>
                    )}
                  </div>
                )}
                <br />
              </div>
            </div>
          </div>
          {/* {solutionSolved && (
            <div>
              <p style={{ display: "inline", marginLeft: "25px" }}>
                <strong style={{ fontSize: "16px" }}>
                  Optimal Cost of Transportation is INR{" "}
                  <span style={{ color: "#FF0509" }}>{cost}</span> Lakhs
                </strong>
              </p>
            </div>
          )} */}

          <br />
        </div>
      </div>
    </div>
  );
}

export default Daily_Planner;
