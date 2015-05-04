#!/usr/bin/env python3

import sqlite3

DB_NAME= "company.db"
EMPLOYEES=[(1, "Ivan Ivanov", 5000, 10000, "Software Developer"),
           (2, "Rado Rado", 500, 0, "Technical Support Intern"),
           (3, "Ivo Ivo", 10000, 100000, "CEO"),
           (4, "Petar Petrov", 3000, 1000, "Marketing Manager"),
           (5, "Maria Georgieva", 8000, 10000, "COO"),
    ]

create_table_query = """
CREATE TABLE users(id INTEGER PRIMARY KEY,
                    name TEXT,
                    monthly_salary INTEGER,
                    yearly_bonus INTEGER,
                    position TEXT)
"""

db = sqlite3.connect(DB_NAME)
cursor = db.cursor()

cursor.execute(create_table_query)
db.commit()

cursor.executemany('''INSERT INTO users(id, name, monthly_salary,
                   yearly_bonus, position) VALUES(?,?,?,?,?)''', EMPLOYEES)
db.commit()

db.close()
