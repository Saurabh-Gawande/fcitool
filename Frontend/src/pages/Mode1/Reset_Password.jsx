import React, { useRef, useState } from "react";
import Sidenav from "./sidenav";

function Reset_Password() {
  const [showModal, setShowModal] = useState(false);
  const [modalValue, setModalValue] = useState("");
  const [credential, setCredential] = useState({
    username: "",
    oldpassword: "",
    newpassword: "",
    cnewpassword: "",
  });

  function onchange(e) {
    setCredential({ ...credential, [e.target.name]: e.target.value });
  }

  const closeModal = () => {
    setShowModal(false);
  };

  const handleCloseModal = (e) => {
    if (e.target.className === "modal-overlay") {
      closeModal();
    }
  };

  const handleSubmit = () => {
    const { username, oldpassword, newpassword, cnewpassword } = credential;

    if (newpassword.length < 6) {
      setShowModal(true);
      setModalValue("New password must be at least 6 characters long.");
      return;
    }

    if (newpassword !== cnewpassword) {
      setShowModal(true);
      setModalValue("New Password does not match");
      return;
    }

    const specialCharactersRegex = /[!@#$%^&*(),.?":{}|<>]/;
    if (!specialCharactersRegex.test(newpassword)) {
      setShowModal(true);
      setModalValue(
        "New password must contain at least one special character."
      );
      return;
    }

    fetch(
      `https://rakeplanner.callippus.co.uk/api/ToolOptimizerWebApi/UpdateToolUserPassword?username=${username}&oldpassword=${oldpassword}&newpassword=${newpassword}`,
      {
        method: "POST",
      }
    )
      .then((response) => response.json())
      .then((data) => {
        setShowModal(true);
        setModalValue(data.msg);
        setCredential({ username: "", oldpassword: "", newpassword: "" });
      })
      .catch((error) => {
        console.error("Error updating password:", error);
        setShowModal(true);
        setModalValue("Internal server error");
      });
  };

  return (
    <div className="page-container" style={{ backgroundColor: "#ebab44b0" }}>
      <Sidenav />
      <div
        className="page-content"
        style={{
          backgroundImage: "url('static/img/bg8.jpg')",
          height: "100vh",
        }}
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
              CHANGE PASSWORD
            </span>
            <a className="x-navigation-control"></a>
          </li>
        </ul>

        <ul className="breadcrumb">
          <li>
            <a href="/home">Home</a>
          </li>
          <li className="active">change password</li>
        </ul>

        <div className="page-content-wrap">
          <div className="row">
            <div className="vh-93 vw-100" style={{ marginTop: "10vh" }}>
              <div className="container h-100">
                <div className="row d-flex justify-content-center align-items-center h-100">
                  <div className="col-lg-12 col-xl-11">
                    <div className="card text-black">
                      <div className="card-body p-md-5">
                        <div className="row justify-content-center">
                          <div className="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                            <form
                              className="mx-1 mx-md-4"
                              style={{
                                display: "flex",
                                flexDirection: "column",
                                gap: 15,
                              }}
                            >
                              <div className="d-flex flex-row align-items-center mb-4">
                                <i
                                  className="fa fa-user-circle"
                                  aria-hidden="true"
                                ></i>
                                <div className="form-outline flex-fill mb-0">
                                  <input
                                    type="text"
                                    className="form-control"
                                    id="name"
                                    name="username"
                                    aria-describedby="emailHelp"
                                    placeholder="Enter Username"
                                    onChange={onchange}
                                    value={credential.username}
                                    required
                                  />
                                  <label className="form-label" htmlFor="name">
                                    Username
                                  </label>
                                </div>
                              </div>

                              <div className="d-flex flex-row align-items-center mb-4">
                                <i
                                  className="fa fa-unlock"
                                  aria-hidden="true"
                                ></i>
                                <div className="form-outline flex-fill mb-0">
                                  <input
                                    type="password"
                                    value={credential.oldpassword}
                                    className="form-control "
                                    id="password"
                                    name="oldpassword"
                                    placeholder="Enter your old Password"
                                    onChange={onchange}
                                    required
                                  />
                                  <label className="form-label" htmlFor="email">
                                    Old Password
                                  </label>
                                </div>
                              </div>

                              <div className="d-flex flex-row align-items-center mb-4">
                                <i className="fa fa-key" aria-hidden="true"></i>
                                <div className="form-outline flex-fill mb-0">
                                  <input
                                    type="password"
                                    className="form-control "
                                    id="cpassword"
                                    value={credential.newpassword}
                                    name="newpassword"
                                    placeholder="Enter your new Password"
                                    onChange={onchange}
                                    required
                                  />
                                  <label
                                    className="form-label"
                                    htmlFor="password"
                                  >
                                    New Password
                                  </label>
                                </div>
                              </div>

                              <div className="d-flex flex-row align-items-center mb-4">
                                <i
                                  class="fa fa-check-square"
                                  aria-hidden="true"
                                ></i>
                                <div className="form-outline flex-fill mb-0">
                                  <input
                                    type="password"
                                    className="form-control "
                                    id="cpassword"
                                    value={credential.cnewpassword}
                                    name="cnewpassword"
                                    placeholder="Enter your new Password"
                                    onChange={onchange}
                                    required
                                  />
                                  <label
                                    className="form-label"
                                    htmlFor="password"
                                  >
                                    Confirm New Password
                                  </label>
                                </div>
                              </div>

                              <div className="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                                <button
                                  type="button"
                                  className="btn btn-primary btn-lg"
                                  onClick={handleSubmit}
                                  disabled={
                                    credential.username === "" ||
                                    credential.oldpassword === "" ||
                                    credential.newpassword === ""
                                  }
                                  style={{
                                    backgroundColor: "orange",
                                    borderRadius: "5px",
                                  }}
                                >
                                  Reset
                                </button>
                              </div>
                            </form>
                          </div>
                          {showModal ? (
                            <div
                              className="modal-overlay"
                              onClick={handleCloseModal}
                            >
                              <div className="modal-content">
                                <span
                                  className="close-btn"
                                  onClick={closeModal}
                                >
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
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Reset_Password;
