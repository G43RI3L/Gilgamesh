--Para rodar localmente com FastAPI + SQLModel, o próprio init_db() cria as tabelas para você. Se for usar migrations, configure Alembic.
CREATE TABLE sites (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  location TEXT
);

CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  unit TEXT,
  qr_code TEXT UNIQUE
);

CREATE TABLE stock_movements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER,
  site_id INTEGER,
  quantity REAL,
  movement_type TEXT,
  date DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(product_id) REFERENCES products(id),
  FOREIGN KEY(site_id) REFERENCES sites(id)
);
