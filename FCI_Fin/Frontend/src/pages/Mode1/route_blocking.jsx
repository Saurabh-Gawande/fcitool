import React, { useState } from 'react';

const DynamicTable = () => {
  const dropdownOptions = [
    { value: 'Andhra Pradesh', label: 'Andhra Pradesh' },
    { value: 'Bihar', label: 'Bihar' },
    { value: 'Chattisgarh', label: 'Chattisgarh' },
    { value: 'Goa', label: 'Goa' },
    { value: 'Gujarat', label: 'Gujarat' },
    { value: 'Haryana', label: 'Haryana' },
    { value: 'Jammu & Kashmir', label: 'Jammu & Kashmir' },
    { value: 'Jharkhand', label: 'Jharkhand' },
    { value: 'Karnataka', label: 'Karnataka' },
    { value: 'Kerala', label: 'Kerala' },
    { value: 'MP', label: 'Madhya Pradesh' },
    { value: 'Maharashtra', label: 'Maharashtra' },
    { value: 'NE', label: 'North East' },
    { value: 'Odisha', label: 'Odisha' },
    { value: 'Punjab', label: 'Punjab' },
    { value: 'Rajasthan', label: 'Rajasthan' },
    { value: 'Tamil Nadu', label: 'Tamil Nadu' },
    { value: 'Telangana', label: 'Telangana' },
    { value: 'UP', label: 'UP' },
    { value: 'Uttarakhand', label: 'Uttarakhand' },
    { value: 'West Bengal', label: 'West Bengal' },
  ];

  const [data, setData] = useState([]);

  const handleAddRow = () => {
    setData((prevData) => [
      ...prevData,
      {
        id: Date.now(),
        origin_state: '',
        dependentOption: '',
        origin_railhead: '',
        destination_state: '',
        destination_railhead: ''
      },
    ]);
  };

  const handleInputChange = (id, field, value) => {
    const updatedData = data.map((item) => {
      if (item.id === id) {
        return { ...item, [field]: value };
      }
      return item;
    });
    setData(updatedData);
  };

  const handleDropdownChange = (id, origin_state) => {
    const updatedData = data.map((item) => {
      if (item.id === id) {
        return { ...item, origin_state, dependentOption: '' };
      }
      return item;
    });
    setData(updatedData);
  };

  const handleDropdownChange2 = (id, destination_state) => {
    const updatedData = data.map((item) => {
      if (item.id === id) {
        return { ...item, destination_state, dependentOption: '' };
      }
      return item;
    });
    setData(updatedData);
  };

  const handleDeleteRow = (id) => {
    setData((prevData) => prevData.filter((item) => item.id !== id));
  };

  return (
    <div>
      <table>
        <thead>
          <tr style={{margin:'auto'}}>
            <th style={{padding:'10px'}}>Origin State</th>
            <th style={{padding:'10px'}}>Origin Railhead</th>
            <th style={{padding:'10px'}}>Destination State</th>
            <th style={{padding:'10px'}}>Destination Railhead</th>
            <th style={{padding:'10px'}}>Action</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td style={{display:'none'}}>{item.id}</td>
              <td>
                <select
                  value={item.origin_state}
                  onChange={(e) => handleDropdownChange(item.id, e.target.value)}
                >
                  <option value="">Select Origin State</option>
                  {dropdownOptions.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </td>
              <td>
                <select
                  value={item.dependentOption}
                  onChange={(e) => handleInputChange(item.id, 'dependentOption', e.target.value)}
                >
                  <option value="">Select an option</option>
                  {item.origin_state === 'NE' && (
                    <>
                      <option value="option1-1">Option 1-1</option>
                      <option value="option1-2">Option 1-2</option>
                    </>
                  )}
                  {item.origin_state === 'option2' && (
                    <>
                      <option value="option2-1">Option 2-1</option>
                      <option value="option2-2">Option 2-2</option>
                    </>
                  )}
                  {item.origin_state === 'option3' && (
                    <option value="option3-1">Option 3-1</option>
                  )}
                </select>
              </td>
              <td>
                <select
                  value={item.destination_state}
                  onChange={(e) => handleDropdownChange2(item.id, e.target.value)}
                >
                  <option value="">Select Origin Railhead</option>
                  {dropdownOptions.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </td>
              <td>
                <span
                  style={{
                    cursor: 'pointer',
                    color: '#ff0000',
                    fontSize: '1.2rem',
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
      <button type="button" onClick={handleAddRow}>
        Add Row
      </button>
    </div>
  );
};

export default DynamicTable;


// import React, { useState } from 'react';

// const DynamicTable = () => {
//   const dropdownOptions = [
//     { value: 'option1', label: 'Option 1' },
//     { value: 'option2', label: 'Option 2' },
//     { value: 'option3', label: 'Option 3' },
//     // Add more options as needed
//   ];

//   const [data, setData] = useState([]);

//   const handleAddRow = () => {
//     setData((prevData) => [
//       ...prevData,
//       {
//         id: Date.now(),
//         name: '',
//         age: '',
//         email: '',
//         selectedOption: '',
//         dependentOption: '',
//       },
//     ]);
//   };

//   const handleInputChange = (id, field, value) => {
//     const updatedData = data.map((item) => {
//       if (item.id === id) {
//         return { ...item, [field]: value };
//       }
//       return item;
//     });
//     setData(updatedData);
//   };

//   const handleDropdownChange = (id, selectedOption) => {
//     const updatedData = data.map((item) => {
//       if (item.id === id) {
//         return { ...item, selectedOption, dependentOption: '' };
//       }
//       return item;
//     });
//     setData(updatedData);
//   };

//   return (
//     <div>
//       <table>
//         <thead>
//           <tr>
//             <th>ID</th>
//             <th>Name</th>
//             <th>Age</th>
//             <th>Email</th>
//             <th>Dropdown 1</th>
//             <th>Dropdown 2</th>
//           </tr>
//         </thead>
//         <tbody>
//           {data.map((item) => (
//             <tr key={item.id}>
//               <td>{item.id}</td>
//               <td>
//                 <input
//                   type="text"
//                   value={item.name}
//                   onChange={(e) => handleInputChange(item.id, 'name', e.target.value)}
//                 />
//               </td>
//               <td>
//                 <input
//                   type="number"
//                   value={item.age}
//                   onChange={(e) => handleInputChange(item.id, 'age', parseInt(e.target.value, 10))}
//                 />
//               </td>
//               <td>
//                 <input
//                   type="email"
//                   value={item.email}
//                   onChange={(e) => handleInputChange(item.id, 'email', e.target.value)}
//                 />
//               </td>
//               <td>
//                 <select
//                   value={item.selectedOption}
//                   onChange={(e) => handleDropdownChange(item.id, e.target.value)}
//                 >
//                   <option value="">Select an option</option>
//                   {dropdownOptions.map((option) => (
//                     <option key={option.value} value={option.value}>
//                       {option.label}
//                     </option>
//                   ))}
//                 </select>
//               </td>
//               <td>
//                 <select
//                   value={item.dependentOption}
//                   onChange={(e) => handleInputChange(item.id, 'dependentOption', e.target.value)}
//                 >
//                   <option value="">Select an option</option>
//                   {item.selectedOption === 'option1' && (
//                     <>
//                       <option value="option1-1">Option 1-1</option>
//                       <option value="option1-2">Option 1-2</option>
//                     </>
//                   )}
//                   {item.selectedOption === 'option2' && (
//                     <>
//                       <option value="option2-1">Option 2-1</option>
//                       <option value="option2-2">Option 2-2</option>
//                     </>
//                   )}
//                   {item.selectedOption === 'option3' && (
//                     <option value="option3-1">Option 3-1</option>
//                   )}
//                 </select>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//       <button type="button" onClick={handleAddRow}>
//         Add Row
//       </button>
//     </div>
//   );
// };

// export default DynamicTable;
