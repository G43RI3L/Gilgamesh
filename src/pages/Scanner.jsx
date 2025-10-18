import React, {useEffect, useRef} from "react";
import { Html5Qrcode } from "html5-qrcode";
import { createMovement } from "../services/api";

export default function Scanner({tenant_id, site_id}) {
  const scannerRef = useRef();

  useEffect(() => {
    const html5QrCode = new Html5Qrcode("reader");
    Html5Qrcode.getCameras().then(cameras => {
      const cameraId = cameras[0].id;
      html5QrCode.start(
        cameraId,
        { fps: 10, qrbox: 250 },
        qrCodeMessage => {
          try {
            const payload = JSON.parse(qrCodeMessage);
            // montar movimento de entrada simples
            const mov = {
              tenant_id: payload.tenant,
              product_id: payload.product_id,
              instance_id: payload.id,
              type: "entrada",
              qty: 1,
              to_site_id: site_id,
              user: "operador-mvp",
              client_timestamp: new Date().toISOString()
            };
            createMovement(mov).then(res => {
              console.log(res);
              alert("Movimento registrado!");
            }).catch(err => console.error(err));
            // opcional: parar scan por um curto periodo para evitar dupla leitura
            // html5QrCode.stop();
          } catch (e){
            console.error("QR inválido", e);
          }
        },
        errorMessage => {
          // ignorar erros de leitura contínua
        }
      ).catch(err => console.error(err));
    }).catch(err => console.error(err));

    return () => {
      if (Html5Qrcode.getCameras) {
        // não obrigatório parar aqui (depende da lib)
      }
    };
  }, [site_id, tenant_id]);

  return <div>
    <h3>Scanner</h3>
    <div id="reader" style={{width:"500px"}}/>
  </div>;
}
