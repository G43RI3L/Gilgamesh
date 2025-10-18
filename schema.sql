--Para rodar localmente com FastAPI + SQLModel, o próprio init_db() cria as tabelas para você. Se for usar migrations, configure Alembic.

CREATE TABLE tenants (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE sites (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  name TEXT NOT NULL,
  address TEXT
);

CREATE TABLE products (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  sku TEXT,
  name TEXT,
  unit TEXT,
  default_min_stock INTEGER DEFAULT 0,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_instances (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  product_id TEXT NOT NULL,
  lot TEXT,
  manufacture_date DATE,
  arrival_date TIMESTAMP,
  current_site_id TEXT,
  quantity REAL DEFAULT 1.0,
  status TEXT DEFAULT 'active',
  metadata TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stock_movements (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  product_id TEXT NOT NULL,
  instance_id TEXT,
  type TEXT NOT NULL,
  qty REAL NOT NULL,
  from_site_id TEXT,
  to_site_id TEXT,
  user TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  proof_url TEXT,
  reference TEXT,
  client_timestamp TIMESTAMP
);

CREATE TABLE alerts (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  product_id TEXT NOT NULL,
  site_id TEXT NOT NULL,
  threshold_qty REAL,
  active INTEGER DEFAULT 1
);

CREATE TABLE audit_logs (
  id TEXT PRIMARY KEY,
  tenant_id TEXT,
  "user" TEXT,
  action TEXT,
  resource TEXT,
  payload TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


