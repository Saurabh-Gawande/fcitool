 const addConstraint2 = async () => {
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

        var data = block_data2;
        var data1 = block_dataWheat2;
        data.push({
          origin_state: selectedOption5,
          origin_railhead: subOption5,
          destination_state: selectedOption6,
          destination_railhead: subOption6,
          id: Date.now(),
        });
        console.log(data);

        setSelectedOption5("default");
        setSelectedOption6("default");
        setSubOptions5([]);
        setSubOptions6([]);

        console.log(block_data2);

        try {
          const payload1 = {
            rice_inline: data,
            rice_inline_value: inline_value_rice,
            wheat_inline: data1,
            wheat_inline_value: inline_value_wheat,
          };

          console.log(
            block_data2,
            inline_value_rice,
            inline_value_wheat,
            block_dataWheat2
          );

          const response2 = await fetch(ProjectIp + "/Daily_Planner_Check", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(payload1),
          });

          const responseData1 = await response2.json(); // Parse response JSON
          console.log(responseData1); // Log the response data

          if (responseData1.status === "YES") {
            alert("Distance is not within range. Please check again.");
          }
        } catch (error) {
          console.error("Error sending inputs:", error);
        }
      }
      document.getElementById("console_").style.display = "block";
      // document.getElementById("console_").innerHTML+="Destination railhead "+subOption3+" under state"+selectedOption3+" has been added for rice"+'<br/>';
      document.getElementById("console_").innerHTML +=
        "New Inline details has been added for rice" + "<br/>";
    };