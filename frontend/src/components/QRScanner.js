import { QrReader } from 'react-qr-reader';
import React, { useState } from 'react';

export default function QRScanner({ onScan }) {
  return (
    <div>
      <h3>Escanear QR Code</h3>
      <QrReader
        onResult={(result) => {
          if (result) onScan(result?.text);
        }}
        style={{ width: '300px' }}
      />
    </div>
  );
}
