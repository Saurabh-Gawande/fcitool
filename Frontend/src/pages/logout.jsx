import React, { useEffect } from "react";

function Logout() {
  useEffect(() => {
    window.location = "/";
  });
  return <div></div>;
}

export default Logout;
