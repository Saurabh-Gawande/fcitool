import React, { useState, useEffect } from "react";
import Sidenav from "./sidenav";
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import config from "../../config";
import jsPDF from "jspdf";
import "jspdf-autotable";
import "./Daily_Planner.css";

function Daily_Planner() {
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

  const ProjectIp = config.serverUrl;
  const [fixed_data, setFixeddata] = useState([]);
  const [blocked_data, setBlockeddata] = useState([]);
  const [selectedOption_fixed, setSelectedOption_fixed] = useState("default");
  const [subOptions_fixed, setSubOptions_fixed] = useState([]);
  const [selectedOption2_fixed, setSelectedOption2_fixed] = useState("default");
  const [subOptions2_fixed, setSubOptions2_fixed] = useState([]);
  const [subOption1_fixed, setSubOption1_fixed] = useState("");
  const [subOption2_fixed, setSubOption2_fixed] = useState("");
  const [commodity_fixed, setCommodity_fixed] = useState("");
  const [TEFD, set_TEFD] = useState(null);
  const [TEFDdata, set_TEFDdata] = useState();
  const [solutionSolved, setSolutionSolved] = useState(false);
  const [Total_result, set_Total_Result] = useState();
  const [Relevant_result, set_Relevant_Result] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [showMessage, setShowMessage] = useState(false);
  const [riceData, setRiceData] = useState(false);
  const [wheatData, setWheatData] = useState(false);
  const [progress, setProgress] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [coarseGrain, setCoarseGrain] = useState(false);
  const [frk, setFrk] = useState(false);
  const [frk_rra, setFrk_rra] = useState(false);
  const [frk_br, setFrk_br] = useState(false);
  const [frk_cgr, setFrk_cgr] = useState(false);
  const [w_cgr, setw_cgr] = useState(false);
  const [wheat_rra, setWheat_rra] = useState(false);
  const [frkPlusRRA, setFkrPlusRRA] = useState(false);
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

  const [rrcOriginValue, setRrcOriginValue] = useState();
  const [ragiOriginValue, setRagiOriginValue] = useState();
  const [jowarOriginValue, setJowarOriginValue] = useState();
  const [bajraOriginValue, setBajraOriginValue] = useState();
  const [maizeOriginValue, setMiazeOriginValue] = useState();
  const [wheatUrsOriginValue, setWheatUrsOriginValue] = useState();
  const [wheatFaqOriginValue, setWheatFaqOriginValue] = useState();
  const [misc1OriginValue, setMisc1OriginValue] = useState();
  const [misc2OriginValue, setMisc2OriginValue] = useState();
  const [misc3OriginValue, setMisc3OriginValue] = useState();
  const [misc4OriginValue, setMisc4OriginValue] = useState();
  const [frk_rraOriginValue, setfrk_rraOriginValue] = useState();
  const [wheat_rraOriginValue, setwheat_rraOriginValue] = useState();

  const [rrcDestinationValue, setRrcDestinationValue] = useState();
  const [ragiDestinationValue, setRagiDestinationValue] = useState();
  const [jowarDestinationValue, setJowarDestinationValue] = useState();
  const [bajraDestinationValue, setBajraDestinationValue] = useState();
  const [maizeDestinationValue, setMiazeDestinationValue] = useState();
  const [wheatUrsDestinationValue, setWheatUrsDestinationValue] = useState();
  const [wheatFaqDestinationValue, setWheatFaqDestinationValue] = useState();
  const [misc1DestinationValue, setMisc1DestinationValue] = useState();
  const [misc2DestinationValue, setMisc2DestinationValue] = useState();
  const [misc3DestinationValue, setMisc3DestinationValue] = useState();
  const [misc4DestinationValue, setMisc4DestinationValue] = useState();
  const [frk_rraDestinationValue, setfrk_rraDestinationValue] = useState();
  const [wheat_rraDestinationValue, setwheat_rraDestinationValue] = useState();

  const [frkDestinationValue, setfrkDestinationValue] = useState();
  const [excelfiledata, setExcelFileData] = useState(null);
  const [railheadData, setRailheadData] = useState();
  const [rrc, setRrc] = useState(false);
  const [ragi, setRagi] = useState(false);
  const [jowar, setJowar] = useState(false);
  const [bajra, setBajra] = useState(false);
  const [maize, setMaize] = useState(false);
  const [wheat_urs, setWheat_urs] = useState(false);
  const [wheat_faq, setWheat_faq] = useState(false);
  const [misc1, setMisc1] = useState(false);
  const [misc2, setMisc2] = useState(false);
  const [misc3, setMisc3] = useState(false);
  const [misc4, setMisc4] = useState(false);
  const [disableAfterImport, setDisableAfterImport] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [modalValue, setModalValue] = useState("");

  const closeModal = () => {
    setShowModal(false);
  };
  const handleCloseModal = (e) => {
    if (e.target.className === "modal-overlay") {
      closeModal();
    }
  };

  useEffect(() => {
    try {
      fetch(
        `https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/RailHeadCodesforTool`
      )
        .then((response) => {
          if (response.status === 200) {
            return response.json();
          }
        })
        .then((data) => {
          setRailheadData(data);
        });
    } catch (error) {
      console.error("Error during Fetching railhead:", error);
    }
  }, []);

  useEffect(() => {
    const fetchTefdData = async () => {
      try {
        const response = await fetch(
          `https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/CostRateMatrixforTool?matrixType=${TEFD}`
        );

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.json();
        set_TEFDdata(result);
        try {
          if (TEFD === null) {
            return;
          }
          fetch(ProjectIp + "/rail_cost_matraix", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              credentials: "include",
            },
            body: JSON.stringify({ TEFDdata: result }),
          });
        } catch (error) {
          console.error("file is not created for TEFD", error);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchTefdData();
  }, [TEFD]);

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

    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setTotalSurplusRailhead(uniqueRailheadCodes);
    }
  };

  const handleDefictStateChange = async (e) => {
    const selectedValue = e.target.value;
    setDeficitState(selectedValue);

    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setTotalDeficitRailhead(uniqueRailheadCodes);
    }
  };

  const handleSurplusInlineState1Change = async (e) => {
    const selectedValue = e.target.value;
    setSurplusInlineState1(selectedValue);

    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];

      setTotalSurplusInlineRailhead1(uniqueRailheadCodes);
    }
  };

  const handleDeficitInlineState1Change = async (e) => {
    const selectedValue = e.target.value;
    setDeficitInlineState1(selectedValue);
    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setTotalDeficitInlineRailhead1(uniqueRailheadCodes);
    }
  };

  const handleSurplusInlineState2Change = async (e) => {
    const selectedValue = e.target.value;
    setSurplusInlineState2(selectedValue);
    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setTotalSurplusInlineRailhead2(uniqueRailheadCodes);
    }
  };

  const handleDeficitInlineState2Change = async (e) => {
    const selectedValue = e.target.value;
    setDeficitInlineState2(selectedValue);
    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setTotalDeficitInlineRailhead2(uniqueRailheadCodes);
    }
  };

  const AddSurplusInline = async (e) => {
    e.preventDefault();
    setSurplusInline((prev) => [
      ...prev,
      {
        Sno: Math.floor(Math.random() * 500) + 1,
        origin_railhead: surplusInlineRailhead1,
        origin_state: surplusInlineState1,
        destination_railhead: surplusInlineRailhead2,
        destination_state: surplusInlineState2,
        Value: 1,
        Commodity: surplusInlineCommodity1,
      },
    ]);
    setSurplusInlineRailhead1("");
    setSurplusInlineRailhead2("");
  };

  const AddDeficitInline = async (e) => {
    e.preventDefault();
    setDeficitInline((prev) => [
      ...prev,
      {
        Sno: Math.floor(Math.random() * 500) + 1,
        origin_railhead: deficitInlineRailhead1,
        origin_state: deficitInlineState1,
        destination_railhead: deficitInlineRailhead2,
        destination_state: deficitInlineState2,
        Value: 1,
        Commodity: deficitInlineCommodity,
      },
    ]);
    setDeficitInlineRailhead1("");
    setDeficitInlineRailhead2("");
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

  const handleFileChange_ = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleDeleteRow_surplus__source = (row, index) => {
    if (!disableAfterImport) {
      const updatedSurplus = [...surplus];
      updatedSurplus.splice(index, 1);
      setSurplus(updatedSurplus);
    }
  };

  const handleDeleteRow_deficit__dest = (row, index) => {
    if (!disableAfterImport) {
      const updatedDeficit = [...deficit];
      updatedDeficit.splice(index, 1);
      setDeficit(updatedDeficit);
    }
  };
  const handleDeleteRowInline_deficit__dest = (index) => {
    if (!disableAfterImport) {
      const updatedSurplusInline = [...surplusInline];
      updatedSurplusInline.splice(index, 1);
      setSurplusInline(updatedSurplusInline);
    }
  };
  const handleDeleteRow_deficitInline__dest = (index) => {
    if (!disableAfterImport) {
      const updatedDeficitInline = [...deficitInline];
      updatedDeficitInline.splice(index, 1);
      setDeficitInline(updatedDeficitInline);
    }
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
      setModalValue("Please select a file before uploading.");
      setShowModal(true);
    }
  };

  const riceOrigin = surplus.filter((item) => item.Commodity === "RRA");
  const block_data2 = surplusInline.filter((item) => item.Commodity === "RRA");

  const riceDestination = deficit.filter((item) => item.Commodity === "RRA");
  const block_dataDest2 = deficitInline.filter(
    (item) => item.Commodity === "RRA"
  );

  const wheatOrigin = surplus.filter((item) => item.Commodity === "Wheat");
  const block_dataWheat2 = surplusInline.filter(
    (item) => item.Commodity === "Wheat"
  );

  const wheatDestination = deficit.filter((item) => item.Commodity === "Wheat");
  const block_dataDestWheat2 = deficitInline.filter(
    (item) => item.Commodity === "Wheat"
  );

  const coarseGrainOrigin = surplus.filter(
    (item) => item.Commodity === "Coarse Grains"
  );
  const coarseGrainInlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Coarse Grains"
  );

  const coarseGrainDestination = deficit.filter(
    (item) => item.Commodity === "Coarse Grains"
  );
  const coarseGrainInlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Coarse Grains"
  );

  const frkrraOrigin = surplus.filter((item) => item.Commodity === "FRK RRA");
  const frkrraInlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK RRA"
  );

  const frkrraDestination = deficit.filter(
    (item) => item.Commodity === "FRK RRA"
  );
  const frkrraInlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK RRA"
  );

  const frkBr_Origin = surplus.filter((item) => item.Commodity === "FRK BR");
  const frkBr_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK BR"
  );

  const frkBr_Destination = deficit.filter(
    (item) => item.Commodity === "FRK BR"
  );
  const frkBr_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK BR"
  );

  const frk_Origin = surplus.filter((item) => item.Commodity === "Wheat+FRK");
  const frk_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Wheat+FRK"
  );

  const frk_Destination = deficit.filter(
    (item) => item.Commodity === "Wheat+FRK"
  );
  const frk_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Wheat+FRK"
  );

  const w_cgr_Origin = surplus.filter((item) => item.Commodity === "Wheat+CGR");
  const w_cgr_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Wheat+CGR"
  );

  const w_cgr_Destination = deficit.filter(
    (item) => item.Commodity === "Wheat+CGR"
  );
  const w_cgr_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Wheat+CGR"
  );

  const frk_cgr_Origin = surplus.filter((item) => item.Commodity === "FRK+CGR");
  const frk_cgr_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK+CGR"
  );

  const frk_cgr_Destination = deficit.filter(
    (item) => item.Commodity === "FRK+CGR"
  );
  const frk_cgr_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK+CGR"
  );

  const rrc_Origin = surplus.filter((item) => item.Commodity === "RRC");
  const rrc_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "RRC"
  );
  const rrc_Destination = deficit.filter((item) => item.Commodity === "RRC");
  const rrc_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "RRC"
  );

  const ragi_Origin = surplus.filter((item) => item.Commodity === "Ragi");
  const ragi_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Ragi"
  );
  const ragi_Destination = deficit.filter((item) => item.Commodity === "Ragi");
  const ragi_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Ragi"
  );

  const jowar_Origin = surplus.filter((item) => item.Commodity === "Jowar");
  const jowar_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Jowar"
  );
  const jowar_Destination = deficit.filter(
    (item) => item.Commodity === "Jowar"
  );
  const jowar_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Jowar"
  );

  const bajra_Origin = surplus.filter((item) => item.Commodity === "Bajra");
  const bajra_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Bajra"
  );
  const bajra_Destination = deficit.filter(
    (item) => item.Commodity === "Bajra"
  );
  const bajra_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Bajra"
  );

  const maize_Origin = surplus.filter((item) => item.Commodity === "Maize");
  const maize_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Maize"
  );
  const maize_Destination = deficit.filter(
    (item) => item.Commodity === "Maize"
  );
  const maize_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Maize"
  );

  const misc1_Origin = surplus.filter((item) => item.Commodity === "Misc1");
  const misc1_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Misc1"
  );
  const misc1_Destination = deficit.filter(
    (item) => item.Commodity === "Misc1"
  );
  const misc1_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Misc1"
  );

  const misc2_Origin = surplus.filter((item) => item.Commodity === "Misc2");
  const misc2_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Misc2"
  );
  const misc2_Destination = deficit.filter(
    (item) => item.Commodity === "Misc2"
  );
  const misc2_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Misc2"
  );

  const wheaturs_Origin = surplus.filter(
    (item) => item.Commodity === "Wheat(URS)"
  );
  const wheaturs_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Wheat(URS)"
  );
  const wheaturs_Destination = deficit.filter(
    (item) => item.Commodity === "Wheat(URS)"
  );
  const wheaturs_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Wheat(URS)"
  );

  const wheatfaq_Origin = surplus.filter(
    (item) => item.Commodity === "Wheat(FAQ)"
  );
  const wheatfaq_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Wheat(FAQ)"
  );
  const wheatfaq_Destination = deficit.filter(
    (item) => item.Commodity === "Wheat(FAQ)"
  );
  const wheatfaq_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Wheat(FAQ)"
  );

  const wheat_rra_Origin = surplus.filter(
    (item) => item.Commodity === "Wheat+RRA"
  );
  const wheat_rra_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Wheat+RRA"
  );
  const wheat_rra_Destination = deficit.filter(
    (item) => item.Commodity === "Wheat+RRA"
  );
  const wheat_rra_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Wheat+RRA"
  );

  const frk_rra_Origin = surplus.filter((item) => item.Commodity === "FRK+RRA");
  const frk_rra_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "FRK+RRA"
  );
  const frk_rra_Destination = deficit.filter(
    (item) => item.Commodity === "FRK+RRA"
  );
  const frk_rra_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "FRK+RRA"
  );

  const misc3_Origin = surplus.filter((item) => item.Commodity === "Misc3");
  const misc3_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Misc3"
  );
  const misc3_Destination = deficit.filter(
    (item) => item.Commodity === "Misc3"
  );
  const misc3_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Misc3"
  );

  const misc4_Origin = surplus.filter((item) => item.Commodity === "Misc4");
  const misc4_InlineOrigin = surplusInline.filter(
    (item) => item.Commodity === "Misc4"
  );
  const misc4_Destination = deficit.filter(
    (item) => item.Commodity === "Misc4"
  );
  const misc4_InlineDestination = deficitInline.filter(
    (item) => item.Commodity === "Misc4"
  );

  useEffect(() => {
    setRiceOriginValue(
      riceOrigin.reduce((total, item) => total + item.Value, 0) +
        block_data2.reduce((total, item) => total + item.Value, 0)
    );

    setRiceDestinationValue(
      riceDestination.reduce((total, item) => total + item.Value, 0) +
        block_dataDest2.reduce((total, item) => total + item.Value, 0)
    );

    setWheatOriginValue(
      wheatOrigin.reduce((total, item) => total + item.Value, 0) +
        block_dataWheat2.reduce((total, item) => total + item.Value, 0)
    );
    setWheatDestinationValue(
      wheatDestination.reduce((total, item) => total + item.Value, 0) +
        block_dataDestWheat2.reduce((total, item) => total + item.Value, 0)
    );

    setCoarseGrainOriginValue(
      coarseGrainOrigin.reduce((total, item) => total + item.Value, 0) +
        coarseGrainInlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setCoarseGrainDestinationValue(
      coarseGrainDestination.reduce((total, item) => total + item.Value, 0) +
        coarseGrainInlineDestination.reduce(
          (total, item) => total + item.Value,
          0
        )
    );

    setfrkrraOriginValue(
      frkrraOrigin.reduce((total, item) => total + item.Value, 0) +
        frkrraInlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkrraDestinationValue(
      frkrraDestination.reduce((total, item) => total + item.Value, 0) +
        frkrraInlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkbrOriginValue(
      frkBr_Origin.reduce((total, item) => total + item.Value, 0) +
        frkBr_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkbrDestinationValue(
      frkBr_Destination.reduce((total, item) => total + item.Value, 0) +
        frkBr_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setwcgrOriginValue(
      w_cgr_Origin.reduce((total, item) => total + item.Value, 0) +
        w_cgr_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setwcgrDestinationValue(
      w_cgr_Destination.reduce((total, item) => total + item.Value, 0) +
        w_cgr_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkcgrOriginValue(
      frk_cgr_Origin.reduce((total, item) => total + item.Value, 0) +
        frk_cgr_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkcgrDestinationValue(
      frk_cgr_Destination.reduce((total, item) => total + item.Value, 0) +
        frk_cgr_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setfrkOriginValue(
      frk_Origin.reduce((total, item) => total + item.Value, 0) +
        frk_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setfrkDestinationValue(
      frk_Destination.reduce((total, item) => total + item.Value, 0) +
        frk_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setRrcOriginValue(
      rrc_Origin.reduce((total, item) => total + item.Value, 0) +
        rrc_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setRrcDestinationValue(
      rrc_Destination.reduce((total, item) => total + item.Value, 0) +
        rrc_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setRagiOriginValue(
      ragi_Origin.reduce((total, item) => total + item.Value, 0) +
        ragi_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setRagiDestinationValue(
      ragi_Destination.reduce((total, item) => total + item.Value, 0) +
        ragi_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setJowarOriginValue(
      jowar_Origin.reduce((total, item) => total + item.Value, 0) +
        jowar_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setJowarDestinationValue(
      jowar_Destination.reduce((total, item) => total + item.Value, 0) +
        jowar_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setBajraOriginValue(
      bajra_Origin.reduce((total, item) => total + item.Value, 0) +
        bajra_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setBajraDestinationValue(
      bajra_Destination.reduce((total, item) => total + item.Value, 0) +
        bajra_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setMiazeOriginValue(
      maize_Origin.reduce((total, item) => total + item.Value, 0) +
        maize_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setMiazeDestinationValue(
      maize_Destination.reduce((total, item) => total + item.Value, 0) +
        maize_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setMisc1OriginValue(
      misc1_Origin.reduce((total, item) => total + item.Value, 0) +
        misc1_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setMisc1DestinationValue(
      misc1_Destination.reduce((total, item) => total + item.Value, 0) +
        misc1_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setMisc2OriginValue(
      misc2_Origin.reduce((total, item) => total + item.Value, 0) +
        misc2_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setMisc2DestinationValue(
      misc2_Destination.reduce((total, item) => total + item.Value, 0) +
        misc2_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setWheatUrsOriginValue(
      wheaturs_Origin.reduce((total, item) => total + item.Value, 0) +
        wheaturs_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setWheatUrsDestinationValue(
      wheaturs_Destination.reduce((total, item) => total + item.Value, 0) +
        wheaturs_InlineDestination.reduce(
          (total, item) => total + item.Value,
          0
        )
    );

    setWheatFaqOriginValue(
      wheatfaq_Origin.reduce((total, item) => total + item.Value, 0) +
        wheatfaq_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setWheatFaqDestinationValue(
      wheatfaq_Destination.reduce((total, item) => total + item.Value, 0) +
        wheatfaq_InlineDestination.reduce(
          (total, item) => total + item.Value,
          0
        )
    );

    setwheat_rraOriginValue(
      wheat_rra_Origin.reduce((total, item) => total + item.Value, 0) +
        wheat_rra_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setwheat_rraDestinationValue(
      wheat_rra_Destination.reduce((total, item) => total + item.Value, 0) +
        wheat_rra_InlineDestination.reduce(
          (total, item) => total + item.Value,
          0
        )
    );

    setfrk_rraOriginValue(
      frk_rra_Origin.reduce((total, item) => total + item.Value, 0) +
        frk_rra_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setfrk_rraDestinationValue(
      frk_rra_Destination.reduce((total, item) => total + item.Value, 0) +
        frk_rra_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setMisc3OriginValue(
      misc3_Origin.reduce((total, item) => total + item.Value, 0) +
        misc3_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setMisc3DestinationValue(
      misc3_Destination.reduce((total, item) => total + item.Value, 0) +
        misc3_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );

    setMisc4OriginValue(
      misc4_Origin.reduce((total, item) => total + item.Value, 0) +
        misc4_InlineOrigin.reduce((total, item) => total + item.Value, 0)
    );

    setMisc4DestinationValue(
      misc4_Destination.reduce((total, item) => total + item.Value, 0) +
        misc4_InlineDestination.reduce((total, item) => total + item.Value, 0)
    );
  });

  const handleSolve = async () => {
    setShowMessage(false);
    setSolutionSolved(false);
    if (
      riceOriginvalue < riceDestinationValue ||
      wheatOriginValue < wheatDestinationValue ||
      coarseGrainOriginValue < coarseGrainDestinationValue ||
      frkOriginValue < frkDestinationValue ||
      frkcgrOriginValue < frkcgrDestinationValue ||
      wcgrOriginValue < wcgrDestinationValue ||
      frkrraOriginValue < frkrraDestinationValue ||
      frkbrOriginValue < frkbrDestinationValue ||
      wheat_rraOriginValue < wheat_rraDestinationValue ||
      frk_rraOriginValue < frk_rraDestinationValue ||
      rrcOriginValue < rrcDestinationValue ||
      ragiOriginValue < ragiDestinationValue ||
      jowarOriginValue < jowarDestinationValue ||
      bajraOriginValue < bajraDestinationValue ||
      maizeOriginValue < maizeDestinationValue ||
      misc1OriginValue < misc1DestinationValue ||
      misc2OriginValue < misc2DestinationValue ||
      wheatUrsOriginValue < wheatUrsDestinationValue ||
      wheatFaqOriginValue < wheatFaqDestinationValue
    ) {
      setModalValue(
        "Destination indents more than Supply indents Please check."
      );
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      block_data2.reduce((total, item) => total + item.Value, 0) > 0 &&
      riceDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for RRA");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      block_dataWheat2.reduce((total, item) => total + item.Value, 0) > 0 &&
      wheatDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Wheat");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      coarseGrainInlineOrigin.reduce((total, item) => total + item.Value, 0) >
        0 &&
      coarseGrainDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Coarse Grain");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      wheaturs_InlineOrigin.reduce((total, item) => total + item.Value, 0) >
        0 &&
      wheatUrsDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for wheat(URS)");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      wheatfaq_InlineOrigin.reduce((total, item) => total + item.Value, 0) >
        0 &&
      wheatFaqDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for wheat(FAQ)");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      frk_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      frkDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for wheat+FRK");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      wheat_rra_InlineOrigin.reduce((total, item) => total + item.Value, 0) >
        0 &&
      wheat_rraDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Wheat+RRA");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      frkrraInlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      frkrraDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for FRK RRA");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      frk_rra_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      frk_rraDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for FRK+RRA");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      frkBr_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      frkbrDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for FRK BR");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      w_cgr_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      wcgrDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Wheat+CGR");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      frk_cgr_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      frkcgrDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for FRK+CGR");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      rrc_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      rrcDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for RRC");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (
      ragi_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      ragiDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Ragi");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      jowar_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      jowarDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Jowar");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      bajra_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      bajraDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Bajra");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      maize_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      maizeDestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Maize");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      misc1_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      misc1DestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Misc 1");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }
    if (
      misc2_InlineOrigin.reduce((total, item) => total + item.Value, 0) > 0 &&
      misc2DestinationValue == 0
    ) {
      setModalValue("Please Add destination indents for Misc 2");
      setShowModal(true);
      setIsLoading(false);
      document.getElementById("toggle").checked = false;
      return;
    }

    if (isLoading) return;
    setIsLoading(true);

    const payload = {
      TEFD: TEFD,
      confirmed_data: fixed_data, // fixing all data

      rice_origin: riceOrigin, // rice origin data
      rice_destination: riceDestination, //rice destination data
      rice_inline: block_data2, //rice inline data
      rice_dest_inline: block_dataDest2, //rice destination inline data

      wheat_origin: wheatOrigin, //origin wheat data
      wheat_destination: wheatDestination, // wheat destination data
      wheat_inline: block_dataWheat2, //wheat inline data
      wheat_dest_inline: block_dataDestWheat2, //wheat destination inline data

      coarseGrain_origin: coarseGrainOrigin,
      coarseGrain_destination: coarseGrainDestination,
      coarseGrain_inline: coarseGrainInlineOrigin,
      coarseGrain_dest_inline: coarseGrainInlineDestination,

      frkrra_origin: frkrraOrigin,
      frkrra_destination: frkrraDestination,
      frkrra_inline: frkrraInlineOrigin,
      frkrra_dest_inline: frkrraInlineDestination,

      frkbr_origin: frkBr_Origin,
      frkbr_destination: frkBr_Destination,
      frkbr_inline: frkBr_InlineOrigin,
      frkbr_dest_inline: frkBr_InlineDestination,

      frk_origin: frk_Origin,
      frk_destination: frk_Destination,
      frk_inline: frk_InlineOrigin,
      frk_dest_inline: frk_InlineDestination,

      wcgr_origin: w_cgr_Origin,
      wcgr_destination: w_cgr_Destination,
      wcgr_inline: w_cgr_InlineOrigin,
      wcgr_dest_inline: w_cgr_InlineDestination,

      frkcgr_origin: frk_cgr_Origin,
      frkcgr_destination: frk_cgr_Destination,
      frkcgr_inline: frk_cgr_InlineOrigin,
      frkcgr_dest_inline: frk_cgr_InlineDestination,

      rrc_Origin: rrc_Origin,
      rrc_InlineOrigin: rrc_InlineOrigin,
      rrc_Destination: rrc_Destination,
      rrc_InlineDestination: rrc_InlineDestination,

      ragi_Origin: ragi_Origin,
      ragi_InlineOrigin: ragi_InlineOrigin,
      ragi_Destination: ragi_Destination,
      ragi_InlineDestination: ragi_InlineDestination,

      jowar_Origin: jowar_Origin,
      jowar_InlineOrigin: jowar_InlineOrigin,
      jowar_Destination: jowar_Destination,
      jowar_InlineDestination: jowar_InlineDestination,

      bajra_Origin: bajra_Origin,
      bajra_InlineOrigin: bajra_InlineOrigin,
      bajra_Destination: bajra_Destination,
      bajra_InlineDestination: bajra_InlineDestination,

      maize_Origin: maize_Origin,
      maize_InlineOrigin: maize_InlineOrigin,
      maize_Destination: maize_Destination,
      maize_InlineDestination: maize_InlineDestination,

      misc1_Origin: misc1_Origin,
      misc1_InlineOrigin: misc1_InlineOrigin,
      misc1_Destination: misc1_Destination,
      misc1_InlineDestination: misc1_InlineDestination,

      misc2_Origin: misc2_Origin,
      misc2_InlineOrigin: misc2_InlineOrigin,
      misc2_Destination: misc2_Destination,
      misc2_InlineDestination: misc2_InlineDestination,

      wheaturs_Origin: wheaturs_Origin,
      wheaturs_InlineOrigin: wheaturs_InlineOrigin,
      wheaturs_Destination: wheaturs_Destination,
      wheaturs_InlineDestination: wheaturs_InlineDestination,

      wheatfaq_Origin: wheatfaq_Origin,
      wheatfaq_InlineOrigin: wheatfaq_InlineOrigin,
      wheatfaq_Destination: wheatfaq_Destination,
      wheatfaq_InlineDestination: wheatfaq_InlineDestination,

      wheat_rra_Origin: wheat_rra_Origin,
      wheat_rra_Destination: wheat_rra_Destination,
      wheat_rra_InlineOrigin: wheat_rra_InlineOrigin,
      wheat_rra_InlineDestination: wheat_rra_InlineDestination,

      frk_rra_Origin: frk_rra_Origin,
      frk_rra_Destination: frk_rra_Destination,
      frk_rra_InlineOrigin: frk_rra_InlineOrigin,
      frk_rra_InlineDestination: frk_rra_InlineDestination,

      misc3_Origin: misc3_Origin,
      misc3_InlineOrigin: misc3_InlineOrigin,
      misc3_Destination: misc3_Destination,
      misc3_InlineDestination: misc3_InlineDestination,

      misc4_Origin: misc4_Origin,
      misc4_InlineOrigin: misc4_InlineOrigin,
      misc4_Destination: misc4_Destination,
      misc4_InlineDestination: misc4_InlineDestination,

      TEFDdata: TEFDdata,
      region: sessionStorage.getItem("region"),
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
    }
    document.getElementById("toggle").checked = false;
    setProgress((prev) => [...prev, "Successfully generated daily plan"]);
  };

  const fetchReservationId_Total_result = () => {
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

  const exportToPDF = () => {
    if (Total_result == null) {
      window.alert("Fetching Result, Please Wait");
    } else {
      const pdfDoc = new jsPDF("p", "mm", "a4");
      const currentDateUTC = new Date();
      const istOffset = 5.5 * 60 * 60 * 1000;
      const currentDateIST = new Date(currentDateUTC.getTime() + istOffset);

      const year = currentDateIST.getUTCFullYear();
      const month = String(currentDateIST.getUTCMonth() + 1).padStart(2, "0");
      const date = String(currentDateIST.getUTCDate()).padStart(2, "0");
      const hours = String(currentDateIST.getUTCHours()).padStart(2, "0");
      const minutes = String(currentDateIST.getUTCMinutes()).padStart(2, "0");
      const seconds = String(currentDateIST.getUTCSeconds()).padStart(2, "0");

      const timestamp = `${year}/${month}/${date} |  Time: ${hours}:${minutes}:${seconds}`;

      pdfDoc.setFontSize(10);
      pdfDoc.text(
        `Region: ${sessionStorage.getItem("region")}  |  Date: ${timestamp}`,
        15,
        10
      );

      let startY = 5; // Initial startY value

      Object.entries(Total_result).forEach(([column, data], index) => {
        const parsedData = JSON.parse(data);

        if (parsedData && parsedData.length > 0) {
          const headers = [
            "SourceState",
            "SourceRailHead",
            "DestinationState",
            "DestinationRailHead",
            "Commodity",
            "Rakes",
          ];
          const rows = parsedData.map((item) => [
            item.SourceState,
            item.SourceRailHead,
            item.DestinationState,
            item.DestinationRailHead,
            item.Commodity,
            item.Rakes,
          ]);

          pdfDoc.autoTable({
            head: [headers],
            body: rows,
            // startY: startY,
          });

          startY = pdfDoc.lastAutoTable.finalY + 20; // Set startY for next content
        }
      });

      pdfDoc.save(`Railhead_data_${timestamp}.pdf`);
      setProgress((prev) => [
        ...prev,
        "Downloaded Railhead detail Plan in Pdf format",
      ]);
    }
  };

  const handleDropdownChange_fixed = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption_fixed(selectedValue);
    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setSubOptions_fixed(uniqueRailheadCodes);
    }
  };

  const handleDropdownChange2_fixed = async (e) => {
    const selectedValue = e.target.value;
    setSelectedOption2_fixed(selectedValue);
    if (railheadData.response && railheadData.response.length > 0) {
      const filteredRailheads = railheadData.response.filter(
        (region) => region.region === selectedValue
      );

      const uniqueRailheadCodes = [
        ...new Set(filteredRailheads.map((region) => region.railheadCode)),
      ];
      setSubOptions2_fixed(uniqueRailheadCodes);
    }
  };

  const handleDeleteRow_fixed = (e) => {
    let fixed_data_ = fixed_data.filter((item) => item["id"] !== e);
    setFixeddata(fixed_data_);
  };

  const addConstraint_fixed = (e) => {
    e.preventDefault();
    if (
      selectedOption_fixed &&
      subOption1_fixed &&
      selectedOption2_fixed &&
      subOption2_fixed &&
      commodity_fixed
    ) {
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
          Commodity: commodity_fixed,
          value: 1,
          id: Date.now(),
        },
      ]);

      setSubOption1_fixed("");
      setSubOption2_fixed("");

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
    const frkData = JSON.parse(Total_result?.wheat_frk ?? 0);
    const frkcgrData = JSON.parse(Total_result?.frkcgr ?? 0);
    const wcgrData = JSON.parse(Total_result?.wcgr ?? 0);
    const rrc = JSON.parse(Total_result?.rrc ?? 0);
    const ragi = JSON.parse(Total_result?.ragi ?? 0);
    const bajra = JSON.parse(Total_result?.bajra ?? 0);
    const jowar = JSON.parse(Total_result?.jowar ?? 0);
    const maize = JSON.parse(Total_result?.maize ?? 0);
    const wheat_faq = JSON.parse(Total_result?.wheat_faq ?? 0);
    const wheat_urs = JSON.parse(Total_result?.wheat_urs ?? 0);
    const misc1 = JSON.parse(Total_result?.misc1 ?? 0);
    const misc2 = JSON.parse(Total_result?.misc2 ?? 0);
    const wheat_rra = JSON.parse(Total_result?.wheat_rra ?? 0);
    const frkPlusRRA = JSON.parse(Total_result?.frkPlusRRA ?? 0);
    const misc3 = JSON.parse(Total_result?.misc3 ?? 0);
    const misc4 = JSON.parse(Total_result?.misc4 ?? 0);
    setRiceData(riceData);
    setWheatData(wheatData);
    setCoarseGrain(coarseGrainData);
    setFrk_rra(frk_rraData);
    setFrk_br(frk_brData);
    setFrk(frkData);
    setFrk_cgr(frkcgrData);
    setw_cgr(wcgrData);
    setRrc(rrc);
    setRagi(ragi);
    setBajra(bajra);
    setJowar(jowar);
    setMaize(maize);
    setWheat_faq(wheat_faq);
    setWheat_urs(wheat_urs);
    setMisc1(misc1);
    setMisc2(misc2);
    setWheat_rra(wheat_rra);
    setFkrPlusRRA(frkPlusRRA);
    setMisc3(misc3);
    setMisc4(misc4);
  };

  const exportToExcel1 = () => {
    if (Total_result == null) {
      window.alert("Fetching Result, Please Wait");
      fetchReservationId_Total_result();
    } else {
      const currentDateUTC = new Date();
      const istOffset = 5.5 * 60 * 60 * 1000;
      const currentDateIST = new Date(currentDateUTC.getTime() + istOffset);
      const dateAndTime = currentDateIST
        .toISOString()
        .replace(/[:.]/g, "-")
        .split(".")[0];
      const filenameWithDateTime = `Daily_Movement_Scenario1_${dateAndTime}.xlsx`;

      const workbook = XLSX.utils.book_new();
      const allData = {};
      Object.entries(Total_result).forEach(([column, data]) => {
        const parsedData = JSON.parse(data);
        if (Array.isArray(parsedData) && parsedData.length > 0) {
          allData[column] = parsedData;
        }
      });

      const combinedData = [];
      Object.values(allData).forEach((data) => {
        combinedData.push(...data);
      });

      const selectedColumns = [
        "SourceRailHead",
        "SourceState",
        "DestinationRailHead",
        "DestinationState",
        "Commodity",
        "Rakes",
      ];
      const filteredData = combinedData.map((row) => {
        const filteredRow = {};
        selectedColumns.forEach((column) => {
          filteredRow[column] = row[column];
        });
        return filteredRow;
      });

      const worksheet = XLSX.utils.json_to_sheet(filteredData, {
        header: selectedColumns,
      });
      XLSX.utils.book_append_sheet(workbook, worksheet, "RH_RH_tags");

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
        "Downloaded Raihead detail Plan in excel",
      ]);
    }
  };

  const uploadFile = async () => {
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
    setExcelFileData(excelBlob);
  };

  useEffect(() => {
    if (excelfiledata) {
      const formData = new FormData();
      const fileName = "Daily_Movement_results_Scenario.xlsx";
      formData.append("file", excelfiledata, fileName);

      fetch(
        "https://test.rakeplanner.callippus.co.uk/api/DailyPlannerDataUploadWebApi/uploadDailyPlannerExcelFile",
        {
          method: "POST",
          body: formData,
        }
      )
        .then((response) => {
          if (response.ok) {
            window.alert("File uploaded successfully!");
            setProgress((prev) => [
              ...prev,
              "Successfully exported the plan to portal",
            ]);
          } else {
            window.alert("File upload failed. Please try again.");
          }
        })
        .catch((error) => {
          console.error("An error occurred during file upload:", error);
        });
    }
  }, [excelfiledata]);

  const fetchData = (event) => {
    event.preventDefault();
    fetch(
      `https://test.rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/DailyPlannerNextDayforTool?region=${sessionStorage.getItem(
        "region"
      )}`
    )
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        } else {
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
          setModalValue(
            "The add funtionality will not work when data is imported from portal"
          );
          setShowModal(true);
          if (data.sourceResponse) {
            console.log(data);
            const updatedSurplus = data.sourceResponse.map((item) => ({
              Sno: Math.floor(Math.random() * 500) + 1,
              origin_railhead: item.sourceRailHead.split("_")[0],
              origin_state: item.sourceState,
              Value: item.value,
              Commodity: item.commodity,
              sourceDivision: item.sourceDivision,
              // sourceId : item.sourceId
            }));
            setSurplus(updatedSurplus);
          }

          if (data.destinationResponse) {
            const updatedDeficit = data.destinationResponse.map((item) => ({
              Sno: Math.floor(Math.random() * 500) + 1,
              origin_railhead: item.destinationRailHead.split("_")[0],
              origin_state: item.destinationState,
              Value: item.value,
              Commodity: item.commodity,
              destinationDivision: item.destinationDivision,
              // destinationId: item.destinationId
            }));
            setDeficit(updatedDeficit);
          }

          if (data.inlineSourceResponse) {
            const updatedSurplusInline = data.inlineSourceResponse.map(
              (item) => ({
                Sno: Math.floor(Math.random() * 500) + 1,
                origin_railhead: item.sourceRailHead.split("_")[0],
                origin_state: item.sourceState,
                destination_railhead: item.sourceInlineRailHead.split("_")[0],
                destination_state: item.sourceState,
                Value: 1,
                Commodity: item.commodity,
                sourceDivision: item.sourceDivision,
                inlineSourceDivision: item.inlineSourceDivision,
                // sourceId: item.sourceId
              })
            );
            setSurplusInline(updatedSurplusInline);
          }

          if (data.inlineDestinationResponse) {
            const updatedDeficitInline = data.inlineDestinationResponse.map(
              (item) => ({
                Sno: Math.floor(Math.random() * 500) + 1,
                origin_railhead: item.destinationRailHead.split("_")[0],
                origin_state: item.destinationState,
                destination_railhead:
                  item.destinationInlineRailHead.split("_")[0],
                destination_state: item.destinationState,
                Value: 1,
                Commodity: item.commodity,
                destinationDivision: item.destinationDivision,
                inlineDestinationDivision: item.inlineDestinationDivision,
                // destinationId : item.destinationId
              })
            );
            setDeficitInline(updatedDeficitInline);
          }

          if (data.routeFixing) {
            const updatedRouteFixing = data.routeFixing.map((item) => ({
              origin_railhead: item.sourceRailHead,
              origin_state: item.sourceState,
              destination_railhead: item.destinationRailHead,
              destination_state: item.destinationState,
              Commodity: item.sourceCommodity,
              value: 1,
            }));
            setFixeddata(updatedRouteFixing);
          }

          setDisableAfterImport(true);
        }
      })
      .catch((error) => {
        alert(`Error: ${error.message}`);
      });
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

          {showModal ? (
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
          ) : null}
          <div className="page-content-wrap">
            <div className="row">
              <div className="col-md-12">
                <br />
                {/* <div style={{ marginLeft: "35%" }}>
                  <input type="file" onChange={handleFileChange_} />
                  <button
                    style={{ margin: "5px", padding: "5px" }}
                    onClick={handleFileUpload}
                  >
                    Upload
                  </button>
                </div> */}
                <br />
                <div
                  style={{
                    display: "flex",
                    justifyContent: "end",
                    width: "80%",
                  }}
                >
                  <button
                    style={{ color: "white", display: "flex", flexFlow: 1 }}
                    className="btn btn-danger dropdown-toggle"
                    onClick={fetchData}
                  >
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
                        <option value="TEFD">TEFD</option>
                        <option value="Non_TEFD">Non-TEFD</option>
                        <option value="Non_TEFD_TC">Non-TEFD + TC</option>
                        <option value="TEFD_TC">TEFD + TC</option>
                      </select>
                    </label>
                    <br />
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
                    <div>
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "65vw",
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
                            <option value="">Select Railhead State</option>
                            {railheadData &&
                            railheadData.response.length > 0 ? (
                              [
                                ...new Set(
                                  railheadData.response.map(
                                    (region) => region.region
                                  )
                                ),
                              ].map((region) => (
                                <option key={region} value={region}>
                                  {region}
                                </option>
                              ))
                            ) : (
                              <option value="" disabled>
                                Loading...
                              </option>
                            )}
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
                            <option value="">Select origin railhead</option>
                            {totalSurplusRailhead.map((option) => (
                              <option key={option} value={option}>
                                {option}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Commodity
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            value={surplusCommodity}
                            onChange={(e) => {
                              setSurplusCommodity(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="Wheat(URS)">Wheat(URS)</option>
                            <option value="Wheat(FAQ)">Wheat(FAQ)</option>
                            <option value="Wheat+FRK">Wheat+FRK</option>
                            <option value="Wheat+RRA">Wheat+RRA</option>
                            <option value="FRK+RRA">FRK+RRA</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grains">Coarse Grains</option>
                            <option value="Wheat+CGR">Wheat+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                            <option value="RRC">RRC</option>
                            <option value="Ragi">Ragi</option>
                            <option value="Jowar">Jowar</option>
                            <option value="Bajra">Bajra</option>
                            <option value="Maize">Maize</option>
                            <option value="Misc1">Misc1</option>
                            <option value="Misc2">Misc2</option>
                            <option value="Misc3">Misc3</option>
                            <option value="Misc4">Misc4</option>
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
                        {/* <button
                          onClick={AddSurplus}
                          disabled={
                            surplusState === undefined ||
                            surplusState === "default" ||
                            surplusRailhead === undefined ||
                            surplusRailhead === "" ||
                            surplusCommodity === undefined ||
                            surplusCommodity === "" ||
                            disableAfterImport
                          }
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                        >
                          Add
                        </button> */}
                      </div>
                      <br />
                      {surplus.length !== 0 && (
                        <table style={{ width: "65vw" }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Value</th>
                              <th>Commodity</th>
                              {/* <th>Delete</th> */}
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
                                {/* <td>
                                  <span
                                    style={{
                                      cursor: "pointer",
                                      color: "#ff0000",
                                      fontSize: "1.2rem",
                                    }}
                                    onClick={() =>
                                      handleDeleteRow_surplus__source(
                                        row,
                                        index
                                      )
                                    }
                                    title="Delete"
                                  >
                                    &times;
                                  </span>
                                </td> */}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      )}
                      <p style={{ margin: 2, padding: 0, marginTop: 12 }}>
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
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "65vw",
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
                            <option value="">Select Railhead State</option>
                            {railheadData &&
                            railheadData.response.length > 0 ? (
                              [
                                ...new Set(
                                  railheadData.response.map(
                                    (region) => region.region
                                  )
                                ),
                              ].map((region) => (
                                <option key={region} value={region}>
                                  {region}
                                </option>
                              ))
                            ) : (
                              <option value="" disabled>
                                Loading...
                              </option>
                            )}
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
                            <option value="">
                              Select Destination Railhead
                            </option>
                            {totalDeficitRailhead.map((option) => (
                              <option key={option} value={option}>
                                {option}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Commodity
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            value={deficitCommodity}
                            onChange={(e) => {
                              setDeficitCommodity(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="Wheat(URS)">Wheat(URS)</option>
                            <option value="Wheat(FAQ)">Wheat(FAQ)</option>
                            <option value="Wheat+FRK">Wheat+FRK</option>
                            <option value="Wheat+RRA">Wheat+RRA</option>
                            <option value="FRK+RRA">FRK+RRA</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grains">Coarse Grains</option>
                            <option value="Wheat+CGR">Wheat+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                            <option value="RRC">RRC</option>
                            <option value="Ragi">Ragi</option>
                            <option value="Jowar">Jowar</option>
                            <option value="Bajra">Bajra</option>
                            <option value="Maize">Maize</option>
                            <option value="Misc1">Misc1</option>
                            <option value="Misc2">Misc2</option>
                            <option value="Misc3">Misc3</option>
                            <option value="Misc4">Misc4</option>
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
                        {/* <button
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
                            deficitCommodity === "" ||
                            disableAfterImport
                          }
                        >
                          Add
                        </button> */}
                      </div>
                      <br />
                      {deficit.length !== 0 && (
                        <table style={{ width: "65vw" }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Value</th>
                              <th>Commodity</th>
                              {/* <th>Delete</th> */}
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
                                {/* <td>
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
                                </td> */}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      )}
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
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "65vw",
                        }}
                      >
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            onChange={handleSurplusInlineState1Change}
                            value={surplusInlineState1}
                          >
                            <option value="">Select Railhead State</option>
                            {railheadData &&
                            railheadData.response.length > 0 ? (
                              [
                                ...new Set(
                                  railheadData.response.map(
                                    (region) => region.region
                                  )
                                ),
                              ].map((region) => (
                                <option key={region} value={region}>
                                  {region}
                                </option>
                              ))
                            ) : (
                              <option value="" disabled>
                                Loading...
                              </option>
                            )}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            onChange={(e) =>
                              setSurplusInlineRailhead1(e.target.value)
                            }
                            value={surplusInlineRailhead1}
                          >
                            <option value="">Select Inline Railhead</option>
                            {totalSurplusInlineRailhead1.map((option) => (
                              <option key={option} value={option}>
                                {option}
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
                            style={{ width: "170px", padding: "5px" }}
                            onChange={handleSurplusInlineState2Change}
                            value={surplusInlineState2}
                          >
                            <option value="">Select Railhead State</option>
                            {railheadData &&
                            railheadData.response.length > 0 ? (
                              [
                                ...new Set(
                                  railheadData.response.map(
                                    (region) => region.region
                                  )
                                ),
                              ].map((region) => (
                                <option key={region} value={region}>
                                  {region}
                                </option>
                              ))
                            ) : (
                              <option value="" disabled>
                                Loading...
                              </option>
                            )}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            onChange={(e) =>
                              setSurplusInlineRailhead2(e.target.value)
                            }
                            value={surplusInlineRailhead2}
                          >
                            <option value="">Select Inline Railhead</option>

                            {totalSurplusInlineRailhead2.map((option) => (
                              <option key={option} value={option}>
                                {option}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Commodity
                          </strong>
                          <select
                            value={surplusInlineCommodity1}
                            style={{ width: "170px", padding: "5px" }}
                            onChange={(e) => {
                              setSurplusInlineCommodity1(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="Wheat(URS)">Wheat(URS)</option>
                            <option value="Wheat(FAQ)">Wheat(FAQ)</option>
                            <option value="Wheat+FRK">Wheat+FRK</option>
                            <option value="Wheat+RRA">Wheat+RRA</option>
                            <option value="FRK+RRA">FRK+RRA</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grains">Coarse Grains</option>
                            <option value="Wheat+CGR">Wheat+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                            <option value="RRC">RRC</option>
                            <option value="Jowar">Jowar</option>
                            <option value="Ragi">Ragi</option>
                            <option value="Bajra">Bajra</option>
                            <option value="Maize">Maize</option>
                            <option value="Misc1">Misc1</option>
                            <option value="Misc2">Misc2</option>
                            <option value="Misc3">Misc3</option>
                            <option value="Misc4">Misc4</option>
                          </select>
                        </div>
                        {/* <button
                          onClick={AddSurplusInline}
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                          disabled={
                            surplusInlineState1 === undefined ||
                            surplusInlineState1 === "default" ||
                            surplusInlineState2 === undefined ||
                            surplusInlineState2 === "default" ||
                            surplusInlineRailhead1 === undefined ||
                            surplusInlineRailhead1 === "" ||
                            surplusInlineRailhead2 === undefined ||
                            surplusInlineRailhead2 === "" ||
                            surplusInlineCommodity1 === undefined ||
                            surplusInlineCommodity1 === "" ||
                            disableAfterImport
                          }
                        >
                          Add
                        </button> */}
                      </div>
                      {surplusInline.length > 0 && (
                        <table style={{ width: "65vw", marginTop: 20 }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Value</th>
                              <th>Commodity</th>
                              {/* <th>Delete</th> */}
                            </tr>
                          </thead>
                          <tbody>
                            {surplusInline.map((row, index) => {
                              return (
                                <tr key={index}>
                                  <td>{index}</td>
                                  <td>{row.origin_railhead}</td>
                                  <td>{row.origin_state}</td>
                                  <td>{row.destination_railhead}</td>
                                  <td>{row.destination_state}</td>
                                  <td>{row.Value}</td>
                                  <td>{row.Commodity}</td>
                                  {/* <td>
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
                                  </td> */}
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
                      )}

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
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          width: "65vw",
                        }}
                      >
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline State
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            onChange={handleDeficitInlineState1Change}
                            value={deficitInlineState1}
                          >
                            <option value="">Select Railhead State</option>
                            {railheadData &&
                            railheadData.response.length > 0 ? (
                              [
                                ...new Set(
                                  railheadData.response.map(
                                    (region) => region.region
                                  )
                                ),
                              ].map((region) => (
                                <option key={region} value={region}>
                                  {region}
                                </option>
                              ))
                            ) : (
                              <option value="" disabled>
                                Loading...
                              </option>
                            )}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            onChange={(e) =>
                              setDeficitInlineRailhead1(e.target.value)
                            }
                            value={deficitInlineRailhead1}
                          >
                            <option value="">Select Inline Railhead</option>

                            {totalDeficitInlineRailhead1.map((option) => (
                              <option key={option} value={option}>
                                {option}
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
                            style={{ width: "170px", padding: "5px" }}
                            onChange={handleDeficitInlineState2Change}
                            value={deficitInlineState2}
                          >
                            <option value="">Select Railhead State</option>
                            {railheadData &&
                            railheadData.response.length > 0 ? (
                              [
                                ...new Set(
                                  railheadData.response.map(
                                    (region) => region.region
                                  )
                                ),
                              ].map((region) => (
                                <option key={region} value={region}>
                                  {region}
                                </option>
                              ))
                            ) : (
                              <option value="" disabled>
                                Loading...
                              </option>
                            )}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Inline Railhead
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            onChange={(e) =>
                              setDeficitInlineRailhead2(e.target.value)
                            }
                            value={deficitInlineRailhead2}
                          >
                            <option value="">Select Inline Railhead</option>

                            {totalDeficitInlineRailhead2.map((option) => (
                              <option key={option} value={option}>
                                {option}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div
                          style={{ display: "flex", flexDirection: "column" }}
                        >
                          <strong style={{ fontSize: "16px", padding: "5px" }}>
                            Select Commodity
                          </strong>
                          <select
                            style={{ width: "170px", padding: "5px" }}
                            value={deficitInlineCommodity}
                            onChange={(e) => {
                              setDeficitInlineCommodity(e.target.value);
                            }}
                          >
                            <option value="">Select Commodity</option>
                            <option value="RRA">RRA</option>
                            <option value="Wheat">Wheat</option>
                            <option value="Wheat(URS)">Wheat(URS)</option>
                            <option value="Wheat(FAQ)">Wheat(FAQ)</option>
                            <option value="Wheat+FRK">Wheat+FRK</option>
                            <option value="Wheat+RRA">Wheat+RRA</option>
                            <option value="FRK+RRA">FRK+RRA</option>
                            <option value="FRK RRA">FRK RRA</option>
                            <option value="FRK BR">FRK BR</option>
                            <option value="Coarse Grains">Coarse Grains</option>
                            <option value="Wheat+CGR">Wheat+CGR</option>
                            <option value="FRK+CGR">FRK+CGR</option>
                            <option value="RRC">RRC</option>
                            <option value="Jowar">Jowar</option>
                            <option value="Ragi">Ragi</option>
                            <option value="Bajra">Bajra</option>
                            <option value="Maize">Maize</option>
                            <option value="Misc1">Misc1</option>
                            <option value="Misc2">Misc2</option>
                            <option value="Misc3">Misc3</option>
                            <option value="Misc4">Misc4</option>
                          </select>
                        </div>
                        {/* <button
                          onClick={AddDeficitInline}
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                          disabled={
                            deficitInlineState1 === undefined ||
                            deficitInlineState1 === "default" ||
                            deficitInlineState2 === undefined ||
                            deficitInlineState2 === "default" ||
                            deficitInlineRailhead1 === undefined ||
                            deficitInlineRailhead1 === "" ||
                            deficitInlineRailhead2 === undefined ||
                            deficitInlineRailhead2 === "" ||
                            deficitInlineCommodity === undefined ||
                            deficitInlineCommodity === "" ||
                            disableAfterImport
                          }
                        >
                          Add
                        </button> */}
                      </div>
                      {deficitInline.length > 0 && (
                        <table style={{ width: "65vw", marginTop: 20 }}>
                          <thead>
                            <tr>
                              <th>Sno</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Railhead</th>
                              <th>State</th>
                              <th>Value</th>
                              <th>Commodity</th>
                              {/* <th>Delete</th> */}
                            </tr>
                          </thead>
                          <tbody>
                            {deficitInline.map((row, index) => {
                              return (
                                <tr key={index}>
                                  <td>{index}</td>
                                  <td>{row.origin_railhead}</td>
                                  <td>{row.origin_state}</td>
                                  <td>{row.destination_railhead}</td>
                                  <td>{row.destination_state}</td>
                                  <td>{row.Value}</td>
                                  <td>{row.Commodity}</td>
                                  {/* <td>
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
                                  </td> */}
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
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
                        For Route Fixing:
                      </strong>
                    </p>
                    <br />
                    <div
                      style={{
                        display: "flex",
                        // marginLeft: "20px",
                        width: 1030,
                      }}
                    >
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Origin State
                        </strong>
                        <select
                          style={{ width: "200px", padding: "5px" }}
                          onChange={handleDropdownChange_fixed}
                          value={selectedOption_fixed}
                        >
                          <option value="">Select Railhead State</option>
                          {railheadData && railheadData.response.length > 0 ? (
                            [
                              ...new Set(
                                railheadData.response.map(
                                  (region) => region.region
                                )
                              ),
                            ].map((region) => (
                              <option key={region} value={region}>
                                {region}
                              </option>
                            ))
                          ) : (
                            <option value="" disabled>
                              Loading...
                            </option>
                          )}
                        </select>
                      </div>

                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Origin Railhead
                        </strong>
                        <select
                          style={{ width: "170px", padding: "5px" }}
                          onChange={(e) => setSubOption1_fixed(e.target.value)}
                          value={subOption1_fixed}
                        >
                          <option value="">Select origin railhead</option>
                          {subOptions_fixed.map((option) => (
                            <option key={option} value={option}>
                              {option}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Destination State
                        </strong>
                        <select
                          style={{ width: "170px", padding: "5px" }}
                          onChange={handleDropdownChange2_fixed}
                          value={selectedOption2_fixed}
                        >
                          <option value="">Select Railhead State</option>
                          {railheadData && railheadData.response.length > 0 ? (
                            [
                              ...new Set(
                                railheadData.response.map(
                                  (region) => region.region
                                )
                              ),
                            ].map((region) => (
                              <option key={region} value={region}>
                                {region}
                              </option>
                            ))
                          ) : (
                            <option value="" disabled>
                              Loading...
                            </option>
                          )}
                        </select>
                      </div>
                      <div>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Destination Railhead
                        </strong>
                        <select
                          style={{ width: "170px", padding: "5px" }}
                          onChange={(e) => setSubOption2_fixed(e.target.value)}
                          value={subOption2_fixed}
                        >
                          <option value="">Select origin railhead</option>
                          {subOptions2_fixed.map((option) => (
                            <option key={option} value={option}>
                              {option}
                            </option>
                          ))}
                        </select>
                      </div>
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
                        style={{ width: "170px", padding: "5px" }}
                      >
                        <option value="">Select Commodity</option>
                        <option value="RRA">RRA</option>
                        <option value="Wheat">Wheat</option>
                        <option value="Wheat(URS)">Wheat(URS)</option>
                        <option value="Wheat(FAQ)">Wheat(FAQ)</option>
                        <option value="Wheat+FRK">Wheat+FRK</option>
                        <option value="Wheat+RRA">Wheat+RRA</option>
                        <option value="FRK+RRA">FRK+RRA</option>
                        <option value="FRK RRA">FRK RRA</option>
                        <option value="FRK BR">FRK BR</option>
                        <option value="Coarse Grains">Coarse Grains</option>
                        <option value="Wheat+CGR">Wheat+CGR</option>
                        <option value="FRK+CGR">FRK+CGR</option>
                        <option value="RRC">RRC</option>
                        <option value="Ragi">Ragi</option>
                        <option value="Jowar">Jowar</option>
                        <option value="Bajra">Bajra</option>
                        <option value="Maize">Maize</option>
                        <option value="Misc1">Misc1</option>
                        <option value="Misc2">Misc2</option>
                        <option value="Misc3">Misc3</option>
                        <option value="Misc4">Misc4</option>
                      </select>

                      <div>
                        <button
                          style={{
                            textAlign: "center",
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                            marginLeft: "43.2vw",
                          }}
                          onClick={addConstraint_fixed}
                        >
                          Add
                        </button>
                      </div>
                    </div>
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
                                Commodity
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Value
                              </th>
                              <th style={{ padding: "10px", width: "15%" }}>
                                Delete
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {fixed_data.map((item) => (
                              <tr key={item.id}>
                                <td>{item.origin_state}</td>
                                <td>{item.origin_railhead}</td>
                                <td>{item.destination_state}</td>
                                <td>{item.destination_railhead}</td>
                                <td>{item.Commodity}</td>
                                <td>{item.value}</td>
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

                    <p style={{ margin: 2, padding: 0, marginTop: 2 }}>
                      <strong
                        style={{
                          color: "#9d0921",
                          fontSize: "20px",
                          marginLeft: "15px",
                        }}
                      >
                        For Blocking:
                      </strong>
                    </p>

                    <div
                      style={{
                        display: "flex",
                        justifyContent: "space-between",
                        width: "65vw",
                      }}
                    >
                      <div style={{ display: "flex", flexDirection: "column" }}>
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
                          <option value="">Select Railhead State</option>
                          {railheadData && railheadData.response.length > 0 ? (
                            [
                              ...new Set(
                                railheadData.response.map(
                                  (region) => region.region
                                )
                              ),
                            ].map((region) => (
                              <option key={region} value={region}>
                                {region}
                              </option>
                            ))
                          ) : (
                            <option value="" disabled>
                              Loading...
                            </option>
                          )}
                        </select>
                      </div>
                      <div style={{ display: "flex", flexDirection: "column" }}>
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
                          <option value="">Select origin railhead</option>
                          {totalSurplusRailhead.map((option) => (
                            <option key={option} value={option}>
                              {option}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div style={{ display: "flex", flexDirection: "column" }}>
                        <strong style={{ fontSize: "16px", padding: "5px" }}>
                          Select Commodity
                        </strong>
                        <select
                          style={{ width: "170px", padding: "5px" }}
                          value={surplusCommodity}
                          onChange={(e) => {
                            setSurplusCommodity(e.target.value);
                          }}
                        >
                          <option value="">Select Commodity</option>
                          <option value="RRA">RRA</option>
                          <option value="Wheat">Wheat</option>
                          <option value="Wheat(URS)">Wheat(URS)</option>
                          <option value="Wheat(FAQ)">Wheat(FAQ)</option>
                          <option value="Wheat+FRK">Wheat+FRK</option>
                          <option value="Wheat+RRA">Wheat+RRA</option>
                          <option value="FRK+RRA">FRK+RRA</option>
                          <option value="FRK RRA">FRK RRA</option>
                          <option value="FRK BR">FRK BR</option>
                          <option value="Coarse Grains">Coarse Grains</option>
                          <option value="Wheat+CGR">Wheat+CGR</option>
                          <option value="FRK+CGR">FRK+CGR</option>
                          <option value="RRC">RRC</option>
                          <option value="Ragi">Ragi</option>
                          <option value="Jowar">Jowar</option>
                          <option value="Bajra">Bajra</option>
                          <option value="Maize">Maize</option>
                          <option value="Misc1">Misc1</option>
                          <option value="Misc2">Misc2</option>
                          <option value="Misc3">Misc3</option>
                          <option value="Misc4">Misc4</option>
                        </select>
                      </div>
                      <div style={{ display: "flex", flexDirection: "column" }}>
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
                      {/* <button
                          onClick={AddSurplus}
                          disabled={
                            surplusState === undefined ||
                            surplusState === "default" ||
                            surplusRailhead === undefined ||
                            surplusRailhead === "" ||
                            surplusCommodity === undefined ||
                            surplusCommodity === "" ||
                            disableAfterImport
                          }
                          style={{
                            backgroundColor: "orange",
                            width: 70,
                            height: 40,
                          }}
                        >
                          Add
                        </button> */}
                    </div>

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
                  {solutionSolved && (
                    <div>
                      <div>
                        <button
                          style={{ color: "black", marginLeft: "15px" }}
                          className="btn btn-success dropdown-toggle"
                          onClick={() => exportToExcel1()}
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
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {riceData.map((item, index) => (
                                      <tr key={item["Unnamed: 0"]}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
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
                                      {/* <th
                                        style={{
                                          padding: "10px",
                                          width: "200px",
                                        }}
                                      >
                                        Cost (Rs/MT)
                                      </th> */}
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
                                    {wheatData.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
                                        <td>{item.DestinationRailHead}</td>
                                        <td>{item.DestinationState}</td>
                                        <td>{item.Commodity}</td>
                                        {/* <td>{item.Cost}</td> */}
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {coarseGrain.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk_rra.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk_br.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {frk !== null && frk.length > 0 ? (
                              <div>
                                <div>Wheat+FRK</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frk_cgr.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {w_cgr !== null && w_cgr.length > 0 ? (
                              <div>
                                <div>wheat+cgr</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {w_cgr.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {rrc !== null && rrc.length > 0 ? (
                              <div>
                                <div>RRC</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {rrc.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {ragi !== null && ragi.length > 0 ? (
                              <div>
                                <div>Ragi</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {ragi.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {jowar !== null && jowar.length > 0 ? (
                              <div>
                                <div>Jowar</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {jowar.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {bajra !== null && bajra.length > 0 ? (
                              <div>
                                <div>Bajra</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {bajra.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {maize !== null && maize.length > 0 ? (
                              <div>
                                <div>Maize</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {maize.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {wheat_urs !== null && wheat_urs.length > 0 ? (
                              <div>
                                <div>Wheat(URS)</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {wheat_urs.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {wheat_faq !== null && wheat_faq.length > 0 ? (
                              <div>
                                <div>Wheat(FAQ)</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {wheat_faq.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {misc1 !== null && misc1.length > 0 ? (
                              <div>
                                <div>Misc1</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {misc1.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {misc2 !== null && misc2.length > 0 ? (
                              <div>
                                <div>Misc2</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {misc2.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {wheat_rra !== null && wheat_rra.length > 0 ? (
                              <div>
                                <div>Wheat+RRA</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {wheat_rra.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}
                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {frkPlusRRA !== null && frkPlusRRA.length > 0 ? (
                              <div>
                                <div>FRK+RRA</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {frkPlusRRA.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}

                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {misc3 !== null && misc3.length > 0 ? (
                              <div>
                                <div>Misc3</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {misc3.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
                        )}

                        {showMessage && (
                          <div
                            style={{
                              marginTop: 15,
                              marginLeft: 20,
                              width: "62vw",
                            }}
                          >
                            {misc4 !== null && misc4.length > 0 ? (
                              <div>
                                <div>Misc4</div>
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
                                        Rakes
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    {misc4.map((item, index) => (
                                      <tr key={index}>
                                        <td>{index + 1}</td>
                                        <td>{item.SourceRailHead}</td>
                                        <td>{item.SourceState}</td>
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
              {riceOriginvalue > 0 || riceDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  RRA (S/D) :
                  <p
                    style={{
                      color:
                        riceDestinationValue > riceOriginvalue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {riceOriginvalue}
                  </p>
                  <p>/</p>
                  <p>{riceDestinationValue}</p>
                </div>
              ) : null}

              {wheatOriginValue > 0 || wheatDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Wheat (S/D) :
                  <p
                    style={{
                      color:
                        wheatDestinationValue > wheatOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {wheatOriginValue}
                  </p>
                  <p>/</p>
                  <p>{wheatDestinationValue}</p>
                </div>
              ) : null}

              {coarseGrainOriginValue > 0 || coarseGrainDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Coarse Grain (S/D) :
                  <p
                    style={{
                      color:
                        coarseGrainDestinationValue > coarseGrainOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {coarseGrainOriginValue}
                  </p>
                  <p>/</p>
                  <p>{coarseGrainDestinationValue}</p>
                </div>
              ) : null}

              {frkrraOriginValue > 0 || frkrraDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  FRK RRA (S/D) :
                  <p
                    style={{
                      color:
                        frkrraDestinationValue > frkrraOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {frkrraOriginValue}
                  </p>
                  <p>/</p>
                  <p>{frkrraDestinationValue}</p>
                </div>
              ) : null}

              {frkbrOriginValue > 0 || frkbrDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  FRK BR (S/D) :
                  <p
                    style={{
                      color:
                        frkbrDestinationValue > frkbrOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {frkbrOriginValue}
                  </p>
                  <p>/</p>
                  <p>{frkbrDestinationValue}</p>
                </div>
              ) : null}

              {wcgrOriginValue > 0 || wcgrDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Wheat+CGR (S/D) :
                  <p
                    style={{
                      color:
                        wcgrDestinationValue > wcgrOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {wcgrOriginValue}
                  </p>
                  <p>/</p>
                  <p>{wcgrDestinationValue}</p>
                </div>
              ) : null}

              {frkcgrOriginValue > 0 || frkcgrDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  FRK+CGR (S/D) :
                  <p
                    style={{
                      color:
                        frkcgrDestinationValue > frkcgrOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {frkcgrOriginValue}
                  </p>
                  <p>/</p>
                  <p>{frkcgrDestinationValue}</p>
                </div>
              ) : null}

              {frkOriginValue > 0 || frkDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Wheat+FRK (S/D) :
                  <p
                    style={{
                      color:
                        frkDestinationValue > frkOriginValue ? "red" : "green",
                      marginLeft: 4,
                    }}
                  >
                    {frkOriginValue}
                  </p>
                  <p>/</p>
                  <p>{frkDestinationValue}</p>
                </div>
              ) : null}

              {rrcOriginValue > 0 || rrcDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  RRC (S/D) :
                  <p
                    style={{
                      color:
                        rrcDestinationValue > rrcOriginValue ? "red" : "green",
                      marginLeft: 4,
                    }}
                  >
                    {rrcOriginValue}
                  </p>
                  <p>/</p>
                  <p>{rrcDestinationValue}</p>
                </div>
              ) : null}

              {ragiOriginValue > 0 || ragiDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Ragi (S/D) :
                  <p
                    style={{
                      color:
                        ragiDestinationValue > ragiOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {ragiOriginValue}
                  </p>
                  <p>/</p>
                  <p>{ragiDestinationValue}</p>
                </div>
              ) : null}

              {jowarOriginValue > 0 || jowarDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Jowar (S/D) :
                  <p
                    style={{
                      color:
                        jowarDestinationValue > jowarOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {jowarOriginValue}
                  </p>
                  <p>/</p>
                  <p>{jowarDestinationValue}</p>
                </div>
              ) : null}

              {bajraOriginValue > 0 || bajraDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Bajra (S/D) :
                  <p
                    style={{
                      color:
                        bajraDestinationValue > bajraOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {bajraOriginValue}
                  </p>
                  <p>/</p>
                  <p>{bajraDestinationValue}</p>
                </div>
              ) : null}

              {maizeOriginValue > 0 || maizeDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Maize (S/D) :
                  <p
                    style={{
                      color:
                        maizeDestinationValue > maizeOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {maizeOriginValue}
                  </p>
                  <p>/</p>
                  <p>{maizeDestinationValue}</p>
                </div>
              ) : null}

              {wheatUrsOriginValue > 0 || wheatUrsDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Wheat(URS) (S/D) :
                  <p
                    style={{
                      color:
                        wheatUrsDestinationValue > wheatUrsOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {wheatUrsOriginValue}
                  </p>
                  <p>/</p>
                  <p>{wheatUrsDestinationValue}</p>
                </div>
              ) : null}

              {wheatFaqOriginValue > 0 || wheatFaqDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Wheat(FAQ) (S/D) :
                  <p
                    style={{
                      color:
                        wheatFaqDestinationValue > wheatFaqOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {wheatFaqOriginValue}
                  </p>
                  <p>/</p>
                  <p>{wheatFaqDestinationValue}</p>
                </div>
              ) : null}

              {misc1OriginValue > 0 || misc1DestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Misc 1 (S/D) :
                  <p
                    style={{
                      color:
                        misc1DestinationValue > misc1OriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {misc1OriginValue}
                  </p>
                  <p>/</p>
                  <p>{misc1DestinationValue}</p>
                </div>
              ) : null}

              {misc2OriginValue > 0 || misc2DestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Misc 2 (S/D) :
                  <p
                    style={{
                      color:
                        misc2DestinationValue > misc2OriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {misc2OriginValue}
                  </p>
                  <p>/</p>
                  <p>{misc2DestinationValue}</p>
                </div>
              ) : null}

              {wheat_rraOriginValue > 0 || wheat_rraDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Wheat+RRA (S/D) :
                  <p
                    style={{
                      color:
                        wheat_rraDestinationValue > wheat_rraOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {wheat_rraOriginValue}
                  </p>
                  <p>/</p>
                  <p>{wheat_rraDestinationValue}</p>
                </div>
              ) : null}

              {frk_rraOriginValue > 0 || frk_rraDestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  FRK+RRA (S/D) :
                  <p
                    style={{
                      color:
                        frk_rraDestinationValue > frk_rraOriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {frk_rraOriginValue}
                  </p>
                  <p>/</p>
                  <p>{frk_rraDestinationValue}</p>
                </div>
              ) : null}

              {misc3OriginValue > 0 || misc3DestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Misc 3 (S/D) :
                  <p
                    style={{
                      color:
                        misc3DestinationValue > misc3OriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {misc3OriginValue}
                  </p>
                  <p>/</p>
                  <p>{misc3DestinationValue}</p>
                </div>
              ) : null}

              {misc4OriginValue > 0 || misc4DestinationValue > 0 ? (
                <div style={{ display: "flex" }}>
                  Misc 4 (S/D) :
                  <p
                    style={{
                      color:
                        misc4DestinationValue > misc4OriginValue
                          ? "red"
                          : "green",
                      marginLeft: 4,
                    }}
                  >
                    {misc4OriginValue}
                  </p>
                  <p>/</p>
                  <p>{misc4DestinationValue}</p>
                </div>
              ) : null}

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
