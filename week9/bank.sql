DROP TABLE IF EXISTS clients;

CREATE TABLE IF NOT EXISTS
clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT,                                                   
balance REAL DEFAULT 0,                                          
message TEXT)
