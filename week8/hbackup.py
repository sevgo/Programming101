#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import os.path


class Database:

    @staticmethod
    def create_db_file(fpath):
        if os.path.exists(fpath):
            raise Exception("DB already exists")
        else:
            db = sqlite3.connect(fpath)
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY,
                            name TEXT(64), github TEXT ''')

            cursor.execute('''CREATE TABLE courses(id INTEGER PRIMARY KEY,
                            name TEXT(32)) ''')

            cursor.execute('''CREATE TABLE students_to_cources(
                            id INTEGER PRIMARY KEY, sid INTEGER,
                            cid INTEGER, group INTEGER,
                            FOREIGN KEY(sid) REFERENCES users(id),
                            FOREIGN KEY(cid) REFERENCES courses(id)) ''')

            db.close()

        return Database(fpath)

    def __init__(self, dbfile):
        self.db = dbfile
