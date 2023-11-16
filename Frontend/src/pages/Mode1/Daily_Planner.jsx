import React, { useState, useEffect } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import config from "../../config";
import jsPDF from "jspdf";
// import style from "./Daily_Planner.css";
// import Surplus from "./Surplus";

function Daily_Planner() {
  //---------------------------------------------------------------------------------------------
  const [surplus, setSurplus] = useState([]);
  const [surplusInline, setSurplusInline] = useState([]);
  const [deficit, setDeficit] = useState([]);
  const [deficitInline, setDeficitInline] = useState([]);

  const [surplusState, setSurplusState] = useState();
  const [totalSurplusRailhead, setTotalSurplusRailhead] = useState([]);
  const [surplusRailhead, setSurplusRailhead] = useState();
  const [surplusValue, setSurplusValue] = useState(1);
  const [surplusCommodity, setSurplusCommodity] = useState();

  const [deficitState, setDeficitState] = useState();
  const [totalDeficitRailhead, setTotalDeficitRailhead] = useState([]);
  const [deficitRailhead, setDeficitRailhead] = useState();
  const [deficitValue, setDeficitValue] = useState(1);
  const [deficitCommodity, setDeficitCommodity] = useState();

  const [surplusInlineState1, setSurplusInlineState1] = useState();
  const [surplusInlineRailhead1, setSurplusInlineRailhead1] = useState();
  const [totalSurplusInlineRailhead1, setTotalSurplusInlineRailhead1] =
    useState([]);
  const [surplusInlineState2, setSurplusInlineState2] = useState();
  const [surplusInlineRailhead2, setSurplusInlineRailhead2] = useState();
  const [totalSurplusInlineRailhead2, setTotalSurplusInlineRailhead2] =
    useState([]);
  const [surplusInlineCommodity1, setSurplusInlineCommodity1] = useState();

  const [deficitInlineState1, setDeficitInlineState1] = useState();
  const [deficitInlineRailhead1, setDeficitInlineRailhead1] = useState();
  const [totalDeficitInlineRailhead1, setTotalDeficitInlineRailhead1] =
    useState([]);
  const [deficitInlineState2, setDeficitInlineState2] = useState();
  const [deficitInlineRailhead2, setDeficitInlineRailhead2] = useState();
  const [totalDeficitInlineRailhead2, setTotalDeficitInlineRailhead2] =
    useState([]);
  const [deficitInlineCommodity, setDeficitInlineCommodity] = useState();
  //----------------------------------------------------------------------------------------------------------
  const ProjectIp = config.serverUrl;
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
  const [selectedOptionWheat5, setSelectedOptionWheat5] = useState("default");
  const [subOptionsWheat5, setSubOptionsWheat5] = useState([]);
  const [subOption1, setSubOption1] = useState("");
  const [subOption2, setSubOption2] = useState("");
  const [selectedOption_fixed, setSelectedOption_fixed] = useState("default");
  const [subOptions_fixed, setSubOptions_fixed] = useState([]);
  const [selectedOption2_fixed, setSelectedOption2_fixed] = useState("default");
  const [subOptions2_fixed, setSubOptions2_fixed] = useState([]);
  const [subOption1_fixed, setSubOption1_fixed] = useState("");
  const [subOption2_fixed, setSubOption2_fixed] = useState("");
  const [commodity_fixed, setCommodity_fixed] = useState("");
  const [value_fixed, setValue_fixed] = useState("");
  const [TEFD, set_TEFD] = useState("");
  const [Scenerio, set_Scenerio] = useState("");
  const [solutionSolved, setSolutionSolved] = useState(false);
  const [scn, setscn] = useState(false);
  const [uploadst, setuploadst] = useState(false);
  const [Total_result, set_Total_Result] = useState();
  const [Relevant_result, set_Relevant_Result] = useState(null);
  const [excelData, setExcelData] = useState({});
  const [activeSheetName, setActiveSheetName] = useState(null);
  const [updateExcel, setUpdateExcel] = useState(false);
  const [updateExcel2, setUpdateExcel2] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [showMessage, setShowMessage] = useState(false);
  const [riceData, setRiceData] = useState(false);
  const [wheatData, setWheatData] = useState(false);
  const [downloadMessage, setDownloadMessage] = useState(false);
  const [progress, setProgress] = useState([]);
  const [inline_value_dest_rice, setDestInlineValueRice] = useState("");
  const [inline_value_dest_wheat, setDestInlineValueWheat] = useState("");
  const [block_dataDest2, setBlockdataDest2] = useState([]);
  const [block_dataDestWheat2, setBlockdataDestWheat2] = useState([]);
  useState("default");
  useState("default");
  const [selectedFile, setSelectedFile] = useState(null);
  const [coarseGrain, setCoarseGrain] = useState(false);
  const [frk, setFrk] = useState(false);
  const [frk_rra, setFrk_rra] = useState(false);
  const [frk_br, setFrk_br] = useState(false);
  const [frk_cgr, setFrk_cgr] = useState(false);
  const [w_cgr, setw_cgr] = useState(false);
  const [riceOriginvalue, setRiceOriginValue] = useState();
  const [riceDestinationValue, setRiceDestinationValue] = useState();
  const [wheatOriginValue, setWheatOriginValue] = useState();
  const [wheatDestinationValue, setWheatDestinationValue] = useState();
  const [coarseGrainOriginValue, setCoarseGrainOriginValue] = useState();
  const [coarseGrainDestinationValue, setCoarseGrainDestinationValue] =
    useState();
  const [frkrraOriginValue, setfrkrraOriginValue] = useState();
  const [frkrraDestinationValue, setfrkrraDestinationValue] = useState();
  const [frkbrOriginValue, setfrkbrOriginValue] = useState();
  const [frkbrDestinationValue, setfrkbrDestinationValue] = useState();
  const [wcgrOriginValue, setwcgrOriginValue] = useState();
  const [wcgrDestinationValue, setwcgrDestinationValue] = useState();
  const [frkcgrOriginValue, setfrkcgrOriginValue] = useState();
  const [frkcgrDestinationValue, setfrkcgrDestinationValue] = useState();
  const [frkOriginValue, setfrkOriginValue] = useState();
  const [frkDestinationValue, setfrkDestinationValue] = useState();
  // ---------------------------------------------------------------------------------------
  const processSheetData = (workbook, sheetIndices) => {
    const jsonData = [];
    sheetIndices.forEach((sheetIndex) => {
      const sheetName = workbook.SheetNames[sheetIndex];
      const sheet = workbook.Sheets[sheetName];
      const sheetData = XLSX.utils.sheet_to_json(sheet);
      sheetData.forEach((row) => {
        if (row.Value > 0) {
          let surplusCommodity = "";
          switch (sheetIndex) {
            case 0:
            case 1:
              surplusCommodity = "Wheat";
              break;
            case 2:
            case 3:
              surplusCommodity = "RRA";
              break;
            case 4:
            case 5:
              surplusCommodity = "FRK RRA";
              break;
            case 6:
            case 7:
              surplusCommodity = "FRK BR";
              break;
            case 8:
            case 9:
              surplusCommodity = "Coarse Grain";
              break;
            default:
              break;
          }

          row.Commodity = surplusCommodity;
          jsonData.push(row);
        }
      });
    });
    return jsonData;
  };

  const handleSurplusStateChange = async (e) => {
    const selectedValue = e.target.value;
    setSurplusState(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalSurplusRailhead(dropdownOptions);
  };

  const handleDefictStateChange = async (e) => {
    const selectedValue = e.target.value;
    setDeficitState(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalDeficitRailhead(dropdownOptions);
  };

  const handleSurplusInlineState1Change = async (e) => {
    const selectedValue = e.target.value;
    setSurplusInlineState1(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalSurplusInlineRailhead1(dropdownOptions);
  };
  const handleDeficitInlineState1Change = async (e) => {
    const selectedValue = e.target.value;
    setDeficitInlineState1(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalDeficitInlineRailhead1(dropdownOptions);
  };

  const handleSurplusInlineState2Change = async (e) => {
    const selectedValue = e.target.value;
    setSurplusInlineState2(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalSurplusInlineRailhead2(dropdownOptions);
  };

  const handleDeficitInlineState2Change = async (e) => {
    const selectedValue = e.target.value;
    setDeficitInlineState2(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalDeficitInlineRailhead2(dropdownOptions);
  };

  const AddSurplusInline = async (e) => {
    e.preventDefault();
    setSurplusInline((prev) => [
      ...prev,
      {
        Sno: Math.floor(Math.random() * 500) + 1,
        origin_railhead: surplusInlineRailhead1,
        origin_state: surplusInlineState1,
        Value: 1,
        Commodity: surplusInlineCommodity1,
      },
    ]);
    setSurplusInline((prev) => [
      ...prev,
      {
        Sno: Math.floor(Math.random() * 500) + 1,
        origin_railhead: surplusInlineRailhead2,
        origin_state: surplusInlineState2,
        Value: 1,
        Commodity: surplusInlineCommodity1,
      },
    ]);
  };

  const AddDeficitInline = async (e) => {
    e.preventDefault();
    setDeficitInline((prev) => [
      ...prev,
      {
        Sno: Math.floor(Math.random() * 500) + 1,
        origin_railhead: deficitInlineRailhead1,
        origin_state: deficitInlineState1,
        Value: 1,
        Commodity: deficitInlineCommodity,
      },
    ]);
    setDeficitInline((prev) => [
      ...prev,
      {
        Sno: Math.floor(Math.random() * 500) + 1,
        origin_railhead: deficitInlineRailhead2,
        origin_state: deficitInlineState2,
        Value: 1,
        Commodity: deficitInlineCommodity,
      },
    ]);
  };

  const AddSurplus = (e) => {
    e.preventDefault();
    const existingIndex = surplus.findIndex(
      (row) =>
        row.origin_railhead === surplusRailhead &&
        row.origin_state === surplusState &&
        row.Commodity === surplusCommodity
    );

    if (existingIndex !== -1) {
      const updatedSurplus = [...surplus];
      updatedSurplus[existingIndex].Value = updatedSurplus[
        existingIndex
      ].Value =
        parseInt(updatedSurplus[existingIndex].Value) + parseInt(surplusValue);
      setSurplus(updatedSurplus);
    } else {
      setSurplus((prev) => [
        ...prev,
        {
          Sno: Math.floor(Math.random() * 500) + 1,
          origin_railhead: surplusRailhead,
          origin_state: surplusState,
          Value: surplusValue,
          Commodity: surplusCommodity,
        },
      ]);
    }
    setSurplusRailhead("");
    setSurplusValue(1);
    setSurplusCommodity("");
  };

  const AddDeficit = (e) => {
    e.preventDefault();
    const existingIndex = deficit.findIndex(
      (row) =>
        row.origin_railhead === deficitRailhead &&
        row.origin_state === deficitState &&
        row.Commodity === deficitCommodity
    );

    if (existingIndex !== -1) {
      const updatedDeficit = [...deficit];
      updatedDeficit[existingIndex].Value =
        parseInt(updatedDeficit[existingIndex].Value) + parseInt(deficitValue);
      setDeficit(updatedDeficit);
    } else {
      setDeficit((prev) => [
        ...prev,
        {
          Sno: Math.floor(Math.random() * 500) + 1,
          origin_railhead: deficitRailhead,
          origin_state: deficitState,
          Value: deficitValue,
          Commodity: deficitCommodity,
        },
      ]);
    }
    setDeficitRailhead("");
    setDeficitValue(1);
    setDeficitCommodity("");
  };

  //---------------------------------------------------------------------------------------------------

  const handleFileChange_ = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleDeleteRow_surplus__source = (row, index) => {
    const updatedSurplus = [...surplus];
    updatedSurplus.splice(index, 1);
    setSurplus(updatedSurplus);
  };

  const handleDeleteRow_deficit__dest = (row, index) => {
    const updatedDeficit = [...deficit];
    updatedDeficit.splice(index, 1);
    setDeficit(updatedDeficit);
  };
  const handleDeleteRowInline_deficit__dest = (index) => {
    const updatedSurplusInline = [...surplusInline];
    updatedSurplusInline.splice(index, 1);
    setSurplusInline(updatedSurplusInline);
  };
  const handleDeleteRow_deficitInline__dest = (index) => {
    const updatedDeficitInline = [...deficitInline];
    updatedDeficitInline.splice(index, 1);
    setDeficitInline(updatedDeficitInline);
  };

  const handleFileUpload = () => {
    if (selectedFile) {
      const reader = new FileReader();

      reader.onload = async (event) => {
        const arrayBuffer = event.target.result;
        const data = new Uint8Array(arrayBuffer);
        const workbook = XLSX.read(data, { type: "array" });
        const surplusSheetIndices = [0, 2, 4, 6, 8, 10];
        const deficitSheetIndices = [1, 3, 5, 7, 9, 11];
        const surplusData = processSheetData(workbook, surplusSheetIndices);
        setSurplus(surplusData);
        const deficitData = processSheetData(workbook, deficitSheetIndices);
        setDeficit(deficitData);
      };

      reader.readAsArrayBuffer(selectedFile);
    } else {
      alert("Please select a file before uploading.");
    }
  };

  const handleCellChange = (sheetName, rowIndex, columnIndex, newValue) => {
    const updatedData = { ...excelData };
    updatedData[sheetName][rowIndex][columnIndex] = newValue;
    setExcelData(updatedData);
  };

  const getCommodityData = async () => {
    // setUpdateExcel(false);
    const response = await fetch(ProjectIp + "/getDataTemplate");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const waitForSheetToLoad = (sheetName, maxAttempts = 10) => {
      return new Promise((resolve, reject) => {
        let attempts = 0;

        const checkSheet = () => {
          if (workbook.Sheets[sheetName]) {
            resolve(workbook.Sheets[sheetName]);
          } else {
            attempts++;
            if (attempts >= maxAttempts) {
              reject(new Error(`Sheet "${sheetName}" not found in workbook.`));
            } else {
              setTimeout(checkSheet, 500); // Check every 500 milliseconds (adjust as needed)
            }
          }
        };

        checkSheet();
      });
    };

    try {
      const def_sheet_rice = "Deficit_rice";
      const surplus_sheet_rice = "Surplus_rice";
      const deficitSheetRice = await waitForSheetToLoad(def_sheet_rice);
      const surplusSheetRice = await waitForSheetToLoad(surplus_sheet_rice);
      const deficit_data_rice = XLSX.utils.sheet_to_json(deficitSheetRice, {
        header: 1,
      });
      const surplus_data_rice = XLSX.utils.sheet_to_json(surplusSheetRice, {
        header: 1,
      });
      const def_10_rice = [...deficit_data_rice.slice(1, 10)];
      const sur_10_rice = [...surplus_data_rice.slice(1, 10)];
      setBlockdata3([]);
      setRiceDestination([]);
      for (let i = 0; i < sur_10_rice.length; i++) {
        setBlockdata3((data) => [
          ...data,
          {
            origin_state: sur_10_rice[i][1],
            origin_railhead: sur_10_rice[i][0],
            origin_value: sur_10_rice[i][2],
            id: Date.now() + i.toString(),
          },
        ]);
      }
      for (let i = 0; i < def_10_rice.length; i++) {
        setRiceDestination((data) => [
          ...data,
          {
            origin_state: def_10_rice[i][1],
            origin_railhead: def_10_rice[i][0],
            origin_value: def_10_rice[i][2],
            id: Date.now() + i.toString(),
          },
        ]);
      }

      const def_sheet_wheat = "Deficit_wheat";
      const surplus_sheet_wheat = "Surplus_wheat";
      const deficitSheetWheat = await waitForSheetToLoad(def_sheet_wheat);
      const surplusSheetWheat = await waitForSheetToLoad(surplus_sheet_wheat);
      const deficit_data_wheat = XLSX.utils.sheet_to_json(deficitSheetWheat, {
        header: 1,
      });
      const surplus_data_wheat = XLSX.utils.sheet_to_json(surplusSheetWheat, {
        header: 1,
      });
      const def_10_wheat = [...deficit_data_wheat.slice(1, 10)];
      const sur_10_wheat = [...surplus_data_wheat.slice(1, 10)];
      setBlockdataWheat3([]);
      setWheatDestination([]);
      for (let i = 0; i < sur_10_wheat.length; i++) {
        setBlockdataWheat3((data) => [
          ...data,
          {
            origin_state: sur_10_wheat[i][1],
            origin_railhead: sur_10_wheat[i][0],
            origin_value: sur_10_wheat[i][2],
            id: Date.now() + i.toString(),
          },
        ]);
      }
      for (let i = 0; i < def_10_wheat.length; i++) {
        setWheatDestination((data) => [
          ...data,
          {
            origin_state: def_10_wheat[i][1],
            origin_railhead: def_10_wheat[i][0],
            origin_value: def_10_wheat[i][2],
            id: Date.now() + i,
          },
        ]);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  useEffect(() => {
    getCommodityData();
  }, []);

  const riceOrigin1 = surplus.filter((item) => item.Commodity === "RRA");
  const riceInlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "RRA"
  );
  const riceOrigin = riceOrigin1.concat(riceInlineOrigin);

  const riceDestination1 = deficit.filter((item) => item.Commodity === "RRA");
  const riceInlineDestination = deficitInline.filter(
    (item) => item.Commodity === "RRA"
  );
  const riceDestination = riceDestination1.concat(riceInlineDestination);

  const wheatOrigin1 = surplus.filter((item) => item.Commodity === "Wheat");
  const wheatInlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Wheat"
  );
  const wheatOrigin = wheatOrigin1.concat(wheatInlineOrigin);

  const wheatDestination1 = deficit.filter(
    (item) => item.Commodity === "Wheat"
  );
  const wheatInlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Wheat"
  );
  const wheatDestination = wheatDestination1.concat(wheatInlineDestination);

  const coarseGrainOrigin1 = surplus.filter(
    (item) => item.Commodity === "Coarse Grain"
  );
  const coarseInlineGrainOrigin = surplusInline.filter(
    (item) => item.Commodity === "Coarse Grain"
  );
  const coarseGrainOrigin = coarseGrainOrigin1.concat(coarseInlineGrainOrigin);

  const coarseGrainDestination1 = deficit.filter(
    (item) => item.Commodity === "Coarse Grain"
  );
  const coarseGrainInlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Coarse Grain"
  );
  const coarseGrainDestination = coarseGrainDestination1.concat(
    coarseGrainInlineDestination
  );

  const frkrraOrigin1 = surplus.filter((item) => item.Commodity === "FRK RRA");
  const frkrraInlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK RRA"
  );
  const frkrraOrigin = frkrraOrigin1.concat(frkrraInlineOrigin);

  const frkrraDestination1 = deficit.filter(
    (item) => item.Commodity === "FRK RRA"
  );
  const frkrraInlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK RRA"
  );
  const frkrraDestination = frkrraDestination1.concat(frkrraInlineDestination);

  const frkBr_Origin1 = surplus.filter((item) => item.Commodity === "FRK BR");
  const frkBr_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK BR"
  );
  const frkBr_Origin = frkBr_Origin1.concat(frkBr_InlineOrigin);

  const frkBr_Destination1 = deficit.filter(
    (item) => item.Commodity === "FRK BR"
  );
  const frkBr_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK BR"
  );
  const frkBr_Destination = frkBr_Destination1.concat(frkBr_InlineDestination);

  const frk_Origin1 = surplus.filter((item) => item.Commodity === "FRK");
  const frk_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK"
  );
  const frk_Origin = frk_Origin1.concat(frk_InlineOrigin);

  const frk_Destination1 = deficit.filter((item) => item.Commodity === "FRK");
  const frk_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK"
  );
  const frk_Destination = frk_Destination1.concat(frk_InlineDestination);

  const w_cgr_Origin1 = surplus.filter((item) => item.Commodity === "W+CGR");
  const w_cgr_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "W+CGR"
  );
  const w_cgr_Origin = w_cgr_Origin1.concat(w_cgr_InlineOrigin);

  const w_cgr_Destination1 = deficit.filter(
    (item) => item.Commodity === "W+CGR"
  );
  const w_cgr_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "W+CGR"
  );
  const w_cgr_Destination = w_cgr_Destination1.concat(w_cgr_InlineDestination);

  const frk_cgr_Origin1 = surplus.filter(
    (item) => item.Commodity === "FRK+CGR"
  );
  const frk_cgr_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK+CGR"
  );
  const frk_cgr_Origin = frk_cgr_Origin1.concat(frk_cgr_InlineOrigin);

  const frk_cgr_Destination1 = deficit.filter(
    (item) => item.Commodity === "FRK+CGR"
  );
  const frk_cgr_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK+CGR"
  );
  const frk_cgr_Destination = frk_cgr_Destination1.concat(
    frk_cgr_InlineDestination
  );

  useEffect(() => {
    setRiceOriginValue(
      riceOrigin.reduce((total, item) => total + item.Value, 0)
    );
    setRiceDestinationValue(
      riceDestination.reduce((total, item) => total + item.Value, 0)
    );

    setWheatOriginValue(
      wheatOrigin.reduce((total, item) => total + item.Value, 0)
    );
    setWheatDestinationValue(
      wheatDestination.reduce((total, item) => total + item.Value, 0)
    );

    setCoarseGrainOriginValue(
      coarseGrainOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setCoarseGrainDestinationValue(
      coarseGrainDestination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkrraOriginValue(
      frkrraOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkrraDestinationValue(
      frkrraDestination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkbrOriginValue(
      frkBr_Origin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkbrDestinationValue(
      frkBr_Destination.reduce((total, item) => total + item.Value, 0)
    );

    setwcgrOriginValue(
      w_cgr_Origin.reduce((total, item) => total + item.Value, 0)
    );

    setwcgrDestinationValue(
      w_cgr_Destination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkcgrOriginValue(
      frk_cgr_Origin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkcgrDestinationValue(
      frk_cgr_Destination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkOriginValue(
      frk_Origin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkDestinationValue(
      frk_Destination.reduce((total, item) => total + item.Value, 0)
    );
  });

  const handleSolve = async () => {
    setShowMessage(false);
    setDownloadMessage(false);
    if (
      riceOriginvalue < riceDestinationValue ||
      wheatOriginValue < wheatDestinationValue ||
      coarseGrainOriginValue < coarseGrainDestinationValue ||
      frkOriginValue < frkDestinationValue ||
      frkcgrOriginValue < frkcgrDestinationValue ||
      wcgrOriginValue < wcgrDestinationValue ||
      frkrraOriginValue < frkrraDestinationValue ||
      frkbrOriginValue < frkbrDestinationValue
    ) {
      alert("Destination indents more than Supply indents Please check");
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (isLoading) return;
    setIsLoading(true);

    const payload = {
      TEFD: TEFD,
      origin_state: selectedOption, //blocking state1
      org_rhcode: subOption1, //blocking railhead1
      destination_state: selectedOption2, //blocking state2
      dest_rhcode: subOption2, //blocking state2
      block_data: block_data, //blocking all data
      Scenerio: Scenerio,
      confirmed_data: fixed_data, // fixing all data

      rice_origin: riceOrigin, // rice origin data
      rice_destination: riceDestination, //rice destination data
      rice_inline: block_data2, //rice inline data
      rice_dest_inline: block_dataDest2,
      rice_dest_inline_value: inline_value_dest_rice,
      rice_inline_value: inline_value_rice, // rice inline value

      wheat_origin: wheatOrigin, //origin wheat data
      wheat_destination: wheatDestination, // wheat destination data
      wheat_inline: block_dataWheat2, //wheat inline data
      wheat_inline_value: inline_value_wheat, // wheat inline value
      wheat_dest_inline: block_dataDestWheat2,
      wheat_dest_inline_value: inline_value_dest_wheat,

      coarseGrain_origin: coarseGrainOrigin,
      coarseGrain_destination: coarseGrainDestination,

      frkrra_origin: frkrraOrigin,
      frkrra_destination: frkrraDestination,

      frkbr_origin: frkBr_Origin,
      frkbr_destination: frkBr_Destination,

      frk_origin: frk_Origin,
      frk_destination: frk_Destination,

      wcgr_origin: w_cgr_Origin,
      wcgr_destination: w_cgr_Destination,

      frkcgr_origin: frk_cgr_Origin,
      frkcgr_destination: frk_cgr_Destination,
    };

    try {
      const response = await fetch(ProjectIp + "/Daily_Planner", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      fetchReservationId_Total_result();
      fetchReservationId_Revelant_result();
      if (response.ok) {
        setSolutionSolved(true);
      } else {
        console.error("Failed to send inputs. Status code:", response.status);
      }
    } catch (error) {
      console.error("Error sending inputs:", error);
    } finally {
      setIsLoading(false);
      setDownloadMessage(true);
    }
    document.getElementById("toggle").checked = false;
  };

  const fetchReservationId_Total_result = () => {
    // var form = new FormData();
    fetch(ProjectIp + "/read_Daily_Planner_S1", {
      method: "GET",
      credentials: "include",
      // body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        set_Total_Result(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const fetchReservationId_Revelant_result = () => {
    var form = new FormData();
    fetch(ProjectIp + "/read_Daily_Planner_S1", {
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
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    // dropdownOptions=dropdownOptions_default+dropdownOptions;
    dropdownOptions.unshift(dropdownOptions_default);
    setSubOptions(dropdownOptions);
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
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    // dropdownOptions=dropdownOptions_default+dropdownOptions;
    dropdownOptions.unshift(dropdownOptions_default);
    setSubOptions2(dropdownOptions);
  };

  const exportToPDF = () => {
    if (Total_result == null) {
      window.alert("Fetching Result, Please Wait");
      fetchReservationId_Total_result();
    } else {
      const pdfDoc = new jsPDF();
      const timestamp = new Date().toISOString().replace(/[-:.]/g, "");
      Object.entries(Total_result).forEach(([column, data]) => {
        const parsedData = JSON.parse(data);

        pdfDoc.addPage();
        pdfDoc.text(`Column: ${column}`, 10, 10);

        // Display data from the column below the header
        let yPos = 20;
        parsedData.forEach((item) => {
          const formattedData = formatData(item);
          pdfDoc.text(formattedData, 10, yPos, { maxWidth: 180 });
          yPos +=
            pdfDoc.splitTextToSize(formattedData, { maxWidth: 180 }).length *
              10 +
            5;
        });
      });

      pdfDoc.save(`Railhead_data_${timestamp}.pdf`);
    }
  };

  // Function to format data with line breaks
  const formatData = (item) => {
    return `From: ${item.From}\nFrom State: ${item["From State"]}\nTo: ${item.To}\nTo State: ${item["To State"]}\nCommodity: ${item.Commodity}`;
  };

  const handleSubDropdownChange1 = (e) => {
    setSubOption1(e.target.value);
  };

  const handleSubDropdownChange2 = (e) => {
    setSubOption2(e.target.value);
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
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue_fixed.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    // dropdownOptions=dropdownOptions_default+dropdownOptions;
    dropdownOptions.unshift(dropdownOptions_default);
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
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    // dropdownOptions=dropdownOptions_default+dropdownOptions;
    dropdownOptions.unshift(dropdownOptions_default);
    setSubOptions2_fixed(dropdownOptions);
  };

  const handleSubDropdownChange1_fixed = (e) => {
    setSubOption1_fixed(e.target.value);
  };

  const handleSubDropdownChange2_fixed = (e) => {
    setSubOption2_fixed(e.target.value);
  };

  const handleDeleteRow = (e) => {
    let block_data_ = block_data.filter((item) => item["id"] !== e);
    setBlockdata(block_data_);
    setDownloadMessage(false);
  };
  const handleDeleteRow_fixed = (e) => {
    let fixed_data_ = fixed_data.filter((item) => item["id"] !== e);
    setFixeddata(fixed_data_);
    setDownloadMessage(false);
  };

  const addConstraint = (e) => {
    e.preventDefault();
    if (selectedOption && subOption1 && selectedOption2 && subOption2) {
      // Check if origin and destination railheads are the same
      if (subOption1 === subOption2) {
        alert("Origin and destination railheads cannot be the same.");
        return; // Do not proceed further
      }

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

      // Reset options and suboptions
      setSelectedOption("default");
      setSelectedOption2("default");
      setSubOptions([]);
      setSubOptions2([]);

      setProgress((prev) => [
        ...prev,
        `Route from ${subOption1} to ${subOption2} has been blocked`,
      ]);
    }
  };

  const addConstraint_fixed = (e) => {
    e.preventDefault();
    if (
      selectedOption_fixed &&
      subOption1_fixed &&
      selectedOption2_fixed &&
      subOption2_fixed &&
      commodity_fixed
      // && value_fixed
    ) {
      // Check if origin and destination railheads are the same
      if (subOption1_fixed === subOption2_fixed) {
        alert("Origin and destination railheads cannot be the same.");
        return;
      }

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

      // Reset options and suboptions
      setSelectedOption_fixed("default");
      setSelectedOption2_fixed("default");
      setSubOptions_fixed([]);
      setSubOptions2_fixed([]);

      setProgress((prev) => [
        ...prev,
        `Route from ${subOption1_fixed} to ${subOption2_fixed} has been fixed for ${commodity_fixed}`,
      ]);
    }
  };

  const viewGrid = () => {
    setShowMessage(true);
    const riceData = JSON.parse(Total_result?.rra ?? 0);
    const wheatData = JSON.parse(Total_result?.wheat ?? 0);
    const coarseGrainData = JSON.parse(Total_result?.coarse_grain ?? 0);
    const frk_rraData = JSON.parse(Total_result?.frk_rra ?? 0);
    const frk_brData = JSON.parse(Total_result?.frk_br ?? 0);
    const frkData = JSON.parse(Total_result?.frk ?? 0);
    const frkcgrData = JSON.parse(Total_result?.frkcgr ?? 0);
    const wcgrData = JSON.parse(Total_result?.wcgr ?? 0);
    setRiceData(riceData);
    setWheatData(wheatData);
    setCoarseGrain(coarseGrainData);
    setFrk_rra(frk_rraData);
    setFrk_br(frk_brData);
    setFrk(frkData);
    setFrk_cgr(frkcgrData);
    setw_cgr(wcgrData);
  };

  const exportToExcel1 = () => {
    if (Total_result == null) {
      // Commented out the alert statement
      window.alert("Fetching Result, Please Wait");
      fetchReservationId_Total_result();
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

      const currentDate = new Date();
      const year = currentDate.getFullYear();
      const month = String(currentDate.getMonth() + 1).padStart(2, "0"); // Months are zero-indexed, so we add 1
      const day = String(currentDate.getDate()).padStart(2, "0");
      const hours = String(currentDate.getHours()).padStart(2, "0");
      const minutes = String(currentDate.getMinutes()).padStart(2, "0");
      const seconds = String(currentDate.getSeconds()).padStart(2, "0");
      const dateAndTime = `${year}/${month}/${day}T${hours}/${minutes}/${seconds}`;
      const filenameWithDateTime = `Daily_Movement_Scenario1_${dateAndTime}.xlsx`;
      saveAs(excelBlob, filenameWithDateTime);
    }
  };

  return (
    <div className="page-container" style={{ backgroundColor: "#E7A63D" }}>
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
          </ul>

          <div className="page-content-wrap">
            <div className="row">
              <div className="col-md-12">
                <br />
                <div style={{ marginLeft: "35%" }}>
                  <input type="file" onChange={handleFileChange_} />
                  <button
                    style={{ margin: "5px", padding: "5px" }}
                    onClick={handleFileUpload}
                  >
                    Upload
                  </button>
                </div>
                <br />
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
                          setProgress((prev) => [
                            ...prev,
                            `You have selected the matrix system as ${e.target.value}`,
                          ]);
                        }}
                        style={{ marginLeft: "547px" }}
                      >
                        <option>Select Matrix System</option>
                        <option value="NON-TEFD">Non-TEFD</option>
                        <option value="TEFD">TEFD</option>
                        <option value="Non-TEFD+TC">Non-TEFD + TC</option>
                        <option value="TEFD+TC">TEFD + TC</option>
                      </select>
                    </label>

                    <br />
                    {/* ------------------------------------------------------------------------------------------------- */}
                    <div>
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "60vw",
                        }}
                      >
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Origin State
                          </strong>
                          <select
                            style={{
                              width: "200px",
                              padding: "5px",
                              marginRight: 25,
                            }}
                            onChange={handleSurplusStateChange}
                            value={surplusState}
                          >
                            <option value="default">Select Origin State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
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
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Origin Railhead
                          </strong>
                          <select
                            style={{
                              width: "200px",
                              padding: "5px",
                            }}
                            onChange={(e) => setSurplusRailhead(e.target.value)}
                            value={surplusRailhead}
                          >
                            {totalSurplusRailhead.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong
                            style={{
                              width: "200px",
                              padding: "5px",
                            }}
                          >
                            Select Commodity
                          </strong>
                          <select
                            value={surplusCommodity}
                            onChange={(e) => {
                              setSurplusCommodity(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="FRK">FRK</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grain">Coarse Grain</option>
                            <option value="W+CGR">W+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Enter Value:
                          </strong>
                          <input
                            type="number"
                            min={1}
                            onChange={(e) =>
                              setSurplusValue(parseInt(e.target.value))
                            }
                            value={surplusValue}
                          />
                        </div>
                        <button
                          onClick={AddSurplus}
                          disabled={
                            surplusState === undefined ||
                            surplusState === "default" ||
                            surplusRailhead === undefined ||
                            surplusRailhead === "" ||
                            surplusCommodity === undefined ||
                            surplusCommodity === ""
                          }
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                        >
                          Add
                        </button>
                      </div>
                      <br />
                      <div>Surplus</div>
                      <table style={{ width: "60vw" }}>
                        <thead>
                          <tr>
                            <th>Sno</th>
                            <th>Railhead</th>
                            <th>State</th>
                            <th>Value</th>
                            <th>Commodity</th>
                            <th>Delete</th>
                          </tr>
                        </thead>
                        <tbody>
                          {surplus.map((row, index) => (
                            <tr key={index}>
                              <td>{index}</td>
                              <td>{row.origin_railhead}</td>
                              <td>{row.origin_state}</td>
                              <td>{row.Value}</td>
                              <td>{row.Commodity}</td>
                              <td>
                                <span
                                  style={{
                                    cursor: "pointer",
                                    color: "#ff0000",
                                    fontSize: "1.2rem",
                                  }}
                                  onClick={() =>
                                    handleDeleteRow_surplus__source(row, index)
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
                      <br />
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "60vw",
                        }}
                      >
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Destination State
                          </strong>
                          <select
                            style={{
                              width: "200px",
                              padding: "5px",
                              marginRight: 25,
                            }}
                            onChange={handleDefictStateChange}
                            value={deficitState}
                          >
                            <option value="default">Select Origin State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
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
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Destination Railhead
                          </strong>
                          <select
                            style={{
                              width: "200px",
                              padding: "5px",
                            }}
                            onChange={(e) => setDeficitRailhead(e.target.value)}
                            value={deficitRailhead}
                          >
                            {totalDeficitRailhead.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong
                            style={{
                              width: "200px",
                              padding: "5px",
                            }}
                          >
                            Select Commodity
                          </strong>
                          <select
                            value={deficitCommodity}
                            onChange={(e) => {
                              setDeficitCommodity(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="FRK">FRK</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grain">Coarse Grain</option>
                            <option value="W+CGR">W+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Enter Value:
                          </strong>
                          <input
                            type="number"
                            min={1}
                            onChange={(e) =>
                              setDeficitValue(parseInt(e.target.value))
                            }
                            value={deficitValue}
                          />
                        </div>
                        <button
                          onClick={AddDeficit}
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                          disabled={
                            deficitState === undefined ||
                            deficitState === "default" ||
                            deficitRailhead === undefined ||
                            deficitRailhead === "" ||
                            deficitCommodity === undefined ||
                            deficitCommodity === ""
                          }
                        >
                          Add
                        </button>
                      </div>
                      <br />
                      <div>Deficit</div>
                      <table style={{ width: "60vw" }}>
                        <thead>
                          <tr>
                            <th>Sno</th>
                            <th>Railhead</th>
                            <th>State</th>
                            <th>Value</th>
                            <th>Commodity</th>
                            <th>Delete</th>
                          </tr>
                        </thead>
                        <tbody>
                          {deficit.map((row, index) => (
                            <tr key={index}>
                              <td>{index}</td>
                              <td>{row.origin_railhead}</td>
                              <td>{row.origin_state}</td>
                              <td>{row.Value}</td>
                              <td>{row.Commodity}</td>
                              <td>
                                <span
                                  style={{
                                    cursor: "pointer",
                                    color: "#ff0000",
                                    fontSize: "1.2rem",
                                  }}
                                  onClick={() =>
                                    handleDeleteRow_deficit__dest(row, index)
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
                      <p style={{ margin: 2, padding: 0, marginTop: 15 }}>
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
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "60vw",
                        }}
                      >
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleSurplusInlineState1Change}
                            value={surplusInlineState1}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
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
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={(e) =>
                              setSurplusInlineRailhead1(e.target.value)
                            }
                            value={surplusInlineRailhead1}
                          >
                            {totalSurplusInlineRailhead1.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleSurplusInlineState2Change}
                            value={surplusInlineState2}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
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
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={(e) =>
                              setSurplusInlineRailhead2(e.target.value)
                            }
                            value={surplusInlineRailhead2}
                          >
                            {totalSurplusInlineRailhead2.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong
                            style={{
                              width: "200px",
                              padding: "5px",
                            }}
                          >
                            Select Commodity
                          </strong>
                          <select
                            value={surplusInlineCommodity1}
                            onChange={(e) => {
                              setSurplusInlineCommodity1(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="FRK">FRK</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grain">Coarse Grain</option>
                            <option value="W+CGR">W+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                          </select>
                        </div>
                        <button
                          onClick={AddSurplusInline}
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                        >
                          Add
                        </button>
                      </div>
                      <table style={{ width: "60vw", marginTop: 20 }}>
                        <thead>
                          <tr>
                            <th>Sno</th>
                            <th>Railhead1</th>
                            <th>State1</th>
                            <th>Railhead2</th>
                            <th>State2</th>
                            <th>Value</th>
                            <th>Commodity</th>
                            <th>Delete</th>
                          </tr>
                        </thead>
                        <tbody>
                          {surplusInline
                            .filter((_, index) => index % 2 === 0)
                            .map((row, index) => {
                              const nextRow = surplusInline[index + 1];

                              return (
                                <tr key={index}>
                                  <td>{index}</td>
                                  <td>{row.origin_railhead}</td>
                                  <td>{row.origin_state}</td>
                                  <td>
                                    {nextRow ? nextRow.origin_railhead : ""}
                                  </td>
                                  <td>{nextRow ? nextRow.origin_state : ""}</td>
                                  <td>{row.Value}</td>
                                  <td>{row.Commodity}</td>
                                  <td>
                                    <span
                                      style={{
                                        cursor: "pointer",
                                        color: "#ff0000",
                                        fontSize: "1.2rem",
                                      }}
                                      onClick={() =>
                                        handleDeleteRowInline_deficit__dest(
                                          row,
                                          index
                                        )
                                      }
                                      title="Delete"
                                    >
                                      &times;
                                    </span>
                                  </td>
                                </tr>
                              );
                            })}
                        </tbody>
                      </table>

                      <p style={{ margin: 2, padding: 0, marginTop: 20 }}>
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
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "60vw",
                        }}
                      >
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleDeficitInlineState1Change}
                            value={deficitInlineState1}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
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
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={(e) =>
                              setDeficitInlineRailhead1(e.target.value)
                            }
                            value={deficitInlineRailhead1}
                          >
                            {totalDeficitInlineRailhead1.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={handleDeficitInlineState2Change}
                            value={deficitInlineState2}
                          >
                            <option value="default">Select Inline State</option>
                            <option value="Andhra Pradesh">
                              Andhra Pradesh
                            </option>
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
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "200px", padding: "5px" }}
                            onChange={(e) =>
                              setDeficitInlineRailhead2(e.target.value)
                            }
                            value={deficitInlineRailhead2}
                          >
                            {totalDeficitInlineRailhead2.map((option) => (
                              <option key={option.value} value={option.value}>
                                {option.label}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong
                            style={{
                              width: "200px",
                              padding: "5px",
                            }}
                          >
                            Select Commodity
                          </strong>
                          <select
                            value={deficitInlineCommodity}
                            onChange={(e) => {
                              setDeficitInlineCommodity(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="FRK">FRK</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grain">Coarse Grain</option>
                            <option value="W+CGR">W+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                          </select>
                        </div>
                        <button
                          onClick={AddDeficitInline}
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                        >
                          Add
                        </button>
                      </div>
                      <table style={{ width: "60vw", marginTop: 20 }}>
                        <thead>
                          <tr>
                            <th>Sno</th>
                            <th>Railhead1</th>
                            <th>State1</th>
                            <th>Railhead2</th>
                            <th>State2</th>
                            <th>Value</th>
                            <th>Commodity</th>
                            <th>Delete</th>
                          </tr>
                        </thead>
                        <tbody>
                          {deficitInline
                            .filter((_, index) => index % 2 === 0)
                            .map((row, index) => {
                              const nextRow = deficitInline[index + 1];
                              return (
                                <tr key={index}>
                                  <td>{index}</td>
                                  <td>{row.origin_railhead}</td>
                                  <td>{row.origin_state}</td>
                                  <td>
                                    {nextRow ? nextRow.origin_railhead : ""}
                                  </td>
                                  <td>{nextRow ? nextRow.origin_state : ""}</td>
                                  <td>{row.Value}</td>
                                  <td>{row.Commodity}</td>
                                  <td>
                                    <span
                                      style={{
                                        cursor: "pointer",
                                        color: "#ff0000",
                                        fontSize: "1.2rem",
                                      }}
                                      onClick={() =>
                                        handleDeleteRow_deficitInline__dest(
                                          row,
                                          index
                                        )
                                      }
                                      title="Delete"
                                    >
                                      &times;
                                    </span>
                                  </td>
                                </tr>
                              );
                            })}
                        </tbody>
                      </table>
                    </div>
                    {/* ----------------------------------------------------------------------------------------- */}
                    <br />
                    <p style={{ margin: 2, padding: 0 }}>
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
                    <div
                      style={{
                        display: "flex",
                        marginLeft: "20px",
                        width: 1170,
                      }}
                    >
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
                      <div>
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
                      <div onClick={addConstraint}>
                        <button
                          style={{
                            textAlign: "center",
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                            alignItems: "center",
                          }}
                        >
                          Add
                        </button>
                      </div>
                    </div>
                    <br />
                    {!solutionSolved && block_data.length !== 0 && (
                      <div>
                        <table>
                          <thead>
                            <tr style={{ margin: "auto" }}>
                              <th style={{ padding: "10px", width: "238px" }}>
                                Origin State
                              </th>
                              <th style={{ padding: "10px", width: "238px" }}>
                                Origin Railhead
                              </th>
                              <th style={{ padding: "10px", width: "238px" }}>
                                Destination State
                              </th>
                              <th style={{ padding: "10px", width: "238px" }}>
                                Destination Railhead
                              </th>
                              <th style={{ padding: "10px", width: "236px" }}>
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
                    <div
                      style={{
                        display: "flex",
                        marginLeft: "20px",
                        width: 1030,
                      }}
                    >
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
                    </div>
                    <div
                      style={{
                        display: "flex",
                        marginLeft: "20px",
                        marginTop: "10px",
                      }}
                    >
                      <strong style={{ fontSize: "16px", padding: "5px" }}>
                        Select Commodity
                      </strong>
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
                      {/* <div style={{ marginLeft: "50px" }}>
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
                      </div> */}

                      <div onClick={addConstraint_fixed}>
                        <button
                          style={{
                            textAlign: "center",
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                            marginLeft: 713,
                          }}
                        >
                          Add
                        </button>
                      </div>
                    </div>
                    <br />
                    {!solutionSolved && fixed_data.length !== 0 && (
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
                              {/* <th style={{ padding: "10px", width: "15%" }}>
                                Value
                              </th> */}
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
                                {/* <td>{item.value}</td> */}
                                <td>
                                  <span
                                    style={{
                                      cursor: "pointer",
                                      color: "#ff0000",
                                      fontSize: "1.2rem",
                                    }}
                                    onClick={() =>
                                      handleDeleteRow_fixed(item.id)
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
                  {/* <div>
              <br/>
                    <DynamicTable/>
                  </div> */}
                  <br />

                  {solutionSolved && (
                    <div>
                      <div>
                        <button
                          style={{ color: "white", marginLeft: "15px" }}
                          className="btn btn-danger dropdown-toggle"
                          onClick={() => exportToExcel1()}
                        >
                          <i className="fa fa-bars"></i>
                          Download Railhead-Railhead Detailed Plan
                        </button>

                        <button
                          style={{ color: "white", marginLeft: "15px" }}
                          className="btn btn-danger dropdown-toggle"
                          onClick={viewGrid}
                        >
                          View Railhead Detailed Plan
                        </button>

                        <button
                          style={{ color: "white", marginLeft: "15px" }}
                          className="btn btn-danger dropdown-toggle"
                          onClick={exportToPDF}
                        >
                          Download PDF
                        </button>
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {riceData !== null && riceData.length > 0 ? (
                              <div>
                                <div>RRA</div>
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {riceData.map((item, index) => (
                                      <tr key={item["Unnamed: 0"]}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {wheatData !== null && wheatData.length > 0 ? (
                              <div>
                                <div>Wheat</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {wheatData.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {coarseGrain !== null && coarseGrain.length > 0 ? (
                              <div>
                                <div>Coarse Grain</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {coarseGrain.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {frk_rra !== null && frk_rra.length > 0 ? (
                              <div>
                                <div>frk rra</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk_rra.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {frk_br !== null && frk_br.length > 0 ? (
                              <div>
                                <div>Frk Br</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk_br.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {frk !== null && frk.length > 0 ? (
                              <div>
                                <div>frk</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {frk_cgr !== null && frk_cgr.length > 0 ? (
                              <div>
                                <div>frk cgr</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk_cgr.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
                        {showMessage && (
                          <div style={{ marginTop: 15, marginLeft: 20 }}>
                            {w_cgr !== null && w_cgr.length > 0 ? (
                              <div>
                                <div>w+cgr</div>
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
                                        Dest State
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
                                        values
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {w_cgr.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.From}</td>
                                        <td>{item["From State"]}</td>
                                        <td>{item.To}</td>
                                        <td>{item["To State"]}</td>
                                        <td>{item.Commodity}</td>
                                        <td>{item.Values}</td>
                                      </tr>
                                    ))}
                                  </tbody>
                                </table>
                              </div>
                            ) : (
                              <div />
                            )}
                          </div>
                        )}
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
              {riceOriginvalue > 0 || riceDestinationValue > 0 ? (
                <div
                  style={{
                    color: riceDestinationValue > riceOriginvalue ? "red" : "",
                  }}
                >{`Supply Value of Rice is ${riceOriginvalue}`}</div>
              ) : null}
              {riceDestinationValue > 0 ? (
                <div>{`Destination Value of Rice is ${riceDestinationValue}`}</div>
              ) : null}
              {wheatOriginValue > 0 ? (
                <div
                  style={{
                    color:
                      wheatDestinationValue > wheatOriginValue ? "red" : "",
                  }}
                >{`Supply Value of Wheat is ${wheatOriginValue}`}</div>
              ) : null}
              {wheatDestinationValue > 0 ? (
                <div>{`Destination Value of Wheat is ${wheatDestinationValue}`}</div>
              ) : null}
              {coarseGrainOriginValue > 0 ? (
                <div
                  style={{
                    color:
                      coarseGrainDestinationValue > coarseGrainOriginValue
                        ? "red"
                        : "",
                  }}
                >{`Supply Value of Coarse Grain is ${coarseGrainOriginValue}`}</div>
              ) : null}
              {coarseGrainDestinationValue > 0 ? (
                <div>{`Supply Value of Coarse Grain is ${coarseGrainDestinationValue}`}</div>
              ) : null}
              {frkrraOriginValue > 0 ? (
                <div
                  style={{
                    color:
                      frkrraDestinationValue > frkrraOriginValue ? "red" : "",
                  }}
                >{`Supply Value of FRK RRA is ${frkrraOriginValue}`}</div>
              ) : null}
              {frkrraDestinationValue > 0 ? (
                <div>{`Supply Value of FRK RRA is ${frkrraDestinationValue}`}</div>
              ) : null}
              {frkbrOriginValue > 0 ? (
                <div
                  style={{
                    color:
                      frkbrDestinationValue > frkbrOriginValue ? "red" : "",
                  }}
                >{`Supply Value of FRK BR is ${frkbrOriginValue}`}</div>
              ) : null}
              {frkbrDestinationValue > 0 ? (
                <div>{`Supply Value of FRK BR is ${frkbrDestinationValue}`}</div>
              ) : null}
              {wcgrOriginValue > 0 ? (
                <div
                  style={{
                    color: wcgrDestinationValue > wcgrOriginValue ? "red" : "",
                  }}
                >{`Supply Value of W+CGR is ${wcgrOriginValue}`}</div>
              ) : null}
              {wcgrDestinationValue > 0 ? (
                <div>{`Supply Value of W+CGR is ${wcgrDestinationValue}`}</div>
              ) : null}
              {frkcgrOriginValue > 0 ? (
                <div
                  style={{
                    color:
                      frkcgrDestinationValue > frkcgrOriginValue ? "red" : "",
                  }}
                >{`Supply Value of FRK+CGR is ${frkcgrOriginValue}`}</div>
              ) : null}
              {frkcgrDestinationValue > 0 ? (
                <div>{`Supply Value of FRK+CGR is ${frkcgrDestinationValue}`}</div>
              ) : null}
              {frkOriginValue > 0 ? (
                <div
                  style={{
                    color: frkDestinationValue > frkOriginValue ? "red" : "",
                  }}
                >{`Supply Value of FRK is ${frkOriginValue}`}</div>
              ) : null}
              {frkDestinationValue > 0 ? (
                <div>{`Supply Value of FRK is ${frkDestinationValue}`}</div>
              ) : null}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Daily_Planner;
