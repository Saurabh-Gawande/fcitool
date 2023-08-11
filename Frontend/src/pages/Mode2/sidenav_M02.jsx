function Sidenav_M02() {
  return (
    <div className="page-sidebar">
      <ul className="x-navigation" style={{ backgroundColor: "#00BFBF" }}>
        <li className="xn-logo">
          <a href="#">MODE 2</a>
          <a href="#" className="x-navigation-control"></a>
        </li>
        <li className="xn-profile">
          <a href="#" className="profile-mini">
            <img src="" alt="" />
          </a>
          <div className="profile" style={{ backgroundColor: "#008B8B" }}>
            <div className="profile-image">
              <img src="static/img/FCI.jpg" alt="" />
            </div>
            <div className="profile-data">
              <div className="profile-data-name">Food Corporation of India</div>
              <div className="profile-data-title"></div>
            </div>
          </div>
        </li>
        <li>
          <a href="/home">
            <span className="fa fa-desktop"></span>{" "}
            <span className="xn-text">Home</span>
          </a>
        </li>
        <li>
          <a href="/Monthly_Solution_M02">
            <span className="fa fa-desktop"></span>{" "}
            <span className="xn-text">Monthly Plan</span>
          </a>
        </li>
        {/* <li>
          <a href="/Daily_Scheduler_M02">
            <span className="fa fa-desktop"></span>{" "}
            <span className="xn-text">Daily Scheduler</span>
          </a>
        </li> */}
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        {/* <li>
          <a href="/Alternate_Railhead_M02">
            <span className="fa fa-desktop"></span>{" "}
            <span className="xn-text">Alternate Railheads</span>
          </a>
        </li> */}
        <li>
          <a href="/logout">
            <span className="fa fa-sign-out"></span>{" "}
            <span className="xn-text">Logout</span>
          </a>
        </li>
      </ul>
    </div>
  );
}

export default Sidenav_M02;
