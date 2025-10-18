const API = process.env.VITE_API_URL || "http://localhost:8000";

export async function createMovement(payload){
  const res = await fetch(`${API}/movements/`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(payload)
  });
  return res.json();
}

export async function generateQr(productId){
  const res = await fetch(`${API}/products/${productId}/generate-qr`, {method:"POST"});
  return res.json();
}

export async function chatQuery(q, tenant_id){
  const res = await fetch(`${API}/chat/query?q=${encodeURIComponent(q)}&tenant_id=${tenant_id}`);
  return res.json();
}
