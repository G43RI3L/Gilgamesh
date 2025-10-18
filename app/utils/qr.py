import qrcode
import base64
from io import BytesIO

def generate_qr_base64(payload_text: str) -> str:
    img = qrcode.make(payload_text)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    b64 = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{b64}"
