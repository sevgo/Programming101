#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect("polyglot.db")
cursor = conn.cursor()

result = cursor.execute("SELECT id FROM languages")

for row in result:
    print(row)
