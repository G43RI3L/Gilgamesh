import React, { useEffect, useState } from "react";
import api from "../services/api";

export default function StockTable() {
  const [movements, setMovements] = useState([]);

  useEffect(() => {
    api.get("/movements/").then(res => setMovements(res.data));
  }, []);

  return (
    <table border="1">
      <thead>
        <tr>
          <th>ID</th><th>Produto</th><th>Site</th><th>Quantidade</th><th>Tipo</th><th>Data</th>
        </tr>
      </thead>
      <tbody>
        {movements.map(m => (
          <tr key={m.id}>
            <td>{m.id}</td>
            <td>{m.product_id}</td>
            <td>{m.site_id}</td>
            <td>{m.quantity}</td>
            <td>{m.movement_type}</td>
            <td>{new Date(m.date).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
