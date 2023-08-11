import React, { useEffect, useState } from "react";
import "./Login.css";

function Login() {
  const [currentImage, setCurrentImage] = useState(0);
  const images = [
    "static/img/slider1.jpg",
    "static/img/slider6.jpg",
    // Add more image paths here as needed
  ];
  const ProjectIp = "http://localhost:5000"
  const totalImages = images.length;
  const autoSlideInterval = 3000; // Interval in milliseconds (5 seconds in this example)

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentImage((prevImage) => (prevImage + 1) % totalImages);
    }, autoSlideInterval);

    return () => {
      clearInterval(timer);
    };
  }, [totalImages]);

  const handleLogin = async () => {
    try {
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;

      const form = new FormData();
      form.append("username", username);
      form.append("password", password);

      const response = await fetch(ProjectIp+"/login", {
        method: "POST",
        credentials: "include",
        body: form,
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();

      if (data.status === 1) {
        window.location.assign("/home");
        window.alert("Login Successful! Click Ok to Continue");
      } else {
        window.alert("Incorrect Credentials");
        window.location.reload();
      }
    } catch (error) {
      console.error("Error during login:", error);
      window.alert("An error occurred during login. Please try again later.");
    }
  };

  return (
    <div
      className="login-container login_container"
      style={{ backgroundImage: `url(${images[currentImage]})` }}
    >
      <div className="content">
        <div className="login-box animated fadeInDown">
          <div className="img-responsive">
            <center>
              <img src="static/img/FCI.jpg" width="300" alt="" />
            </center>
          </div>
          <br />
          <div className="login-body">
            <div className="login-title" style={{ color: "white" }}>
              <strong>Welcome</strong>, Please login
            </div>
            <form className="form-horizontal">
              <div className="form-group">
                <div className="col-md-12">
                  <input
                    type="text"
                    id="username"
                    name="username"
                    className="form-control"
                    placeholder="Username"
                    style={{ backgroundColor: "white" }}
                  />
                </div>
              </div>
              <div className="form-group">
                <div className="col-md-12">
                  <input
                    style={{ backgroundColor: "white" }}
                    type="password"
                    id="password"
                    name="password"
                    className="form-control"
                    placeholder="Password"
                  />
                </div>
              </div>
              <div className="form-group">
                <center>
                  <input
                    type="button"
                    className="btn btn-primary"
                    value="login"
                    onClick={handleLogin}
                    style={{ borderRadius: "5px" }}
                  ></input>
                </center>
              </div>
            </form>
          </div>
          <div className="login-footer">
            <div className="pull-left" style={{ color: "white" }}>
              &copy; DEVELOPED BY IIT-DELHI
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
