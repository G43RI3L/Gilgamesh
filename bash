backend/
├─ app/
│  ├─ main.py
│  ├─ db.py
│  ├─ models.py
│  ├─ crud.py
│  ├─ schemas.py
│  ├─ api/
│  │   ├─ products.py
│  │   ├─ movements.py
│  │   └─ chat.py
│  └─ utils/
│      ├─ qr.py
│      └─ sse.py
├─ .env
├─ requirements.txt
└─ alembic/  (opcional se usar migrations)

frontend/
├─ package.json
├─ index.html
├─ src/
│  ├─ main.jsx
│  ├─ App.jsx
│  ├─ pages/
│  │   ├─ Dashboard.jsx
│  │   └─ Scanner.jsx
│  └─ services/
│      └─ api.js
