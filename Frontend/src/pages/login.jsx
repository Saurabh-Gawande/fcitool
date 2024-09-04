// import React, { useEffect, useState, useContext } from "react";
// import "./Login.css";
// import config from "../config";
// import { useNavigate } from "react-router-dom";

// function Login() {
//   const portalUrl = config.portalUrl;

//   const navigate = useNavigate();
//   const [username, setUsername] = useState();
//   const [password, setPassword] = useState();
//   const [currentImage, setCurrentImage] = useState(0);
//   const [showModal, setShowModal] = useState(false);
//   const [modalValue, setModalValue] = useState("");

//   const images = ["static/img/slider1.jpg", "static/img/slider6.jpg"];

//   const totalImages = images.length;
//   const autoSlideInterval = 3000;

//   const closeModal = () => {
//     setShowModal(false);
//   };
//   const handleCloseModal = (e) => {
//     if (e.target.className === "modal-overlay") {
//       closeModal();
//     }
//   };

//   useEffect(() => {
//     const timer = setInterval(() => {
//       setCurrentImage((prevImage) => (prevImage + 1) % totalImages);
//     }, autoSlideInterval);

//     return () => {
//       clearInterval(timer);
//     };
//   }, [totalImages]);

//   const handleLogin = async () => {
//     try {
//       fetch(
//         `${portalUrl}/ToolOptimizerWebApi/LoginforTool?username=${username}&password=${password}`
//       )
//         .then((response) => {
//           if (response.status === 200) {
//             return response.json();
//           }
//         })
//         .then((data) => {
//           if (data && data.response && data.response.region) {
//             localStorage.getItem("region", data.response.region);
//             if (data.response.region === "H.P.") {
//               navigate("/Monthly_Solution");
//             } else {
//               navigate("/Daily_Planner");
//             }
//           } else {
//             setShowModal(true);
//             setModalValue("Invalid credentials!");
//             navigate("/");
//           }
//         });
//     } catch (error) {
//       console.error("Error during login:", error);
//       window.alert("An error occurred during login. Please try again later.");
//     }
//   };

//   return (
//     <div
//       className="login-container login_container"
//       style={{
//         backgroundImage: `url(${images[currentImage]})`,
//         height: "100vh",
//       }}
//     >
//       <div className="content">
//         <div className="login-box animated fadeInDown">
//           <div className="img-responsive">
//             <center>
//               <img src="static/img/FCI.jpg" width="300" alt="" />
//             </center>
//           </div>
//           <br />
//           <div className="login-body">
//             <div className="login-title" style={{ color: "white" }}>
//               <strong>Welcome</strong>, Please login
//             </div>
//             <form className="form-horizontal">
//               <div className="form-group">
//                 <div className="col-md-12">
//                   <input
//                     type="text"
//                     id="username"
//                     name="username"
//                     className="form-control"
//                     placeholder="Username"
//                     style={{ backgroundColor: "white", color: "black" }}
//                     onChange={(e) => setUsername(e.target.value)}
//                   />
//                 </div>
//               </div>
//               <div className="form-group">
//                 <div className="col-md-12">
//                   <input
//                     style={{ backgroundColor: "white" }}
//                     type="password"
//                     id="password"
//                     name="password"
//                     className="form-control"
//                     placeholder="Password"
//                     onChange={(e) => setPassword(e.target.value)}
//                   />
//                 </div>
//               </div>
//               <div className="form-group">
//                 <center>
//                   <input
//                     type="button"
//                     className="btn btn-primary"
//                     value="login"
//                     onClick={handleLogin}
//                     style={{ borderRadius: "5px" }}
//                   ></input>
//                 </center>
//               </div>
//             </form>
//           </div>
//           <div className="login-footer">
//             {/* <div className="pull-left" style={{ color: "white" }}>
//               &copy; DEVELOPED BY IIT-DELHI v4.0
//             </div> */}
//           </div>
//         </div>
//       </div>
//       {showModal ? (
//         <div
//           className="modal-overlay"
//           onClick={handleCloseModal}
//           style={{ padding: "2px" }}
//         >
//           <div className="modal-content">
//             <span className="close-btn" onClick={closeModal}>
//               &times;
//             </span>
//             <div
//               style={{
//                 display: "flex",
//                 justifyContent: "center",
//                 alignItems: "center",
//                 flexDirection: "column",
//               }}
//             >
//               <h2>Alert</h2>
//               <h6
//                 style={{
//                   display: "flex",
//                   justifyContent: "center",
//                   textAlign: "center",
//                   padding: "5px",
//                 }}
//               >
//                 {modalValue}
//               </h6>
//             </div>
//             <div
//               style={{
//                 display: "flex",
//                 justifyContent: "end",
//                 padding: "5px 2px",
//               }}
//             >
//               <button onClick={closeModal} type="button" class="btn btn-danger">
//                 Close
//               </button>
//             </div>
//           </div>
//         </div>
//       ) : null}
//     </div>
//   );
// }

// export default Login;

import React from "react";

function login() {
  return (
    <h3
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "90vh",
      }}
    >
      Page Not Found
    </h3>
  );
}

export default login;
