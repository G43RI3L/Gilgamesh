import React from "react";
import StockTable from "./components/StockTable";
import QRScanner from "./components/QRScanner";
import api from "./services/api";

function App() {
  const handleScan = (qrData) => {
    const [product_id, site_id, qty] = qrData.split("-");
    api.post("/movements/", {
      product_id: parseInt(product_id),
      site_id: parseInt(site_id),
      quantity: parseFloat(qty),
      movement_type: "entrada"
    }).then(() => alert("Movimento registrado!"));
  };

  return (
    <div>
      <h1>Gerenciador de Estoque - Construção Civil</h1>
      <QRScanner onScan={handleScan} />
      <StockTable />
    </div>
  );
}

export default App;
