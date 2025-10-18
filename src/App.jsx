import React from "react";
import Dashboard from "./pages/Dashboard";
import Scanner from "./pages/Scanner";

function App(){
  const tenant_id = "tenant-mvp"; // trocar para real
  const site_id = "site-mvp";

  return <div style={{padding:20}}>
    <h1>MVP Estoque - Cantereiro (React)</h1>
    <Scanner tenant_id={tenant_id} site_id={site_id}/>
    <hr/>
    <Dashboard tenant_id={tenant_id}/>
  </div>;
}

export default App;
