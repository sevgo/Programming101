#!/usr/bin/env python3
import sqlite3

DB_NAME="company.db"
LIST_EMPLOYEES = '''SELECT name, position FROM users'''
MONTHLY_SALARY = '''SELECT monthly_salary FROM users'''
YEARLY_SPENDING = '''SELECT monthly_salary, yearly_bonus FROM users'''
INSERT_EMPLOYEE = '''INSERT INTO users(id, name, monthly_salary, yearly_bonus,
                    position) VALUES(?, ?, ?, ?, ?)'''
USER_ID = '''SELECT id FROM users'''
LAST_ID = 0

def fetch_result(database, sql):
    db = sqlite3.connect(database, detect_types=True)
    cursor = db.cursor()
    result = cursor.execute(sql)
    db.close()
    return result

def list_employees(database):
    result = fetch_result(database, LIST_EMPLOYEES)
    for row in result:
        print("%s - %s" % row)

def monthly_spending(database):
    result = fetch_result(database, MONTHLY_SALARY)
    total_salaries = 0
    for row in result:
        total_salaries += row[0]

    return total_salaries

def yearly_spending(database):
    result = fetch_result(database, YEARLY_SPENDING)
    money = [row for row in result]
    return sum([sum(el) for el in zip(*money)])

def last_user_id(database, sql):
    result = fetch_result(database, USER_ID)
    ids = [row for row in zip(*result)]
    return max(ids.pop())

def add_employee(database):
    id = last_user_id(database, USER_ID) + 1
    name = input("Name Family: ")
    monthly_salary = int(input("Monthly Salary: "))
    yearly_bonus = int(input("Yearly Bobys: "))
    position = input("position in company: ")

def manage(DB_NAME):
    """

    """
