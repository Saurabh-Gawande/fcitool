import React, { useEffect, useState } from "react";
import UserContext from "./userContext";

function UserState(props) {
  return (
    <UserContext.Provider value={{}}>{props.children}</UserContext.Provider>
  );
}

export default UserState;
