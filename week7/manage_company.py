#!/usr/bin/env python3
import sqlite3

DB_NAME = "company.db"
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
    results = cursor.execute(sql)
    result = [el for el in results]
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
    position = input("Position in company: ")
    db = sqlite3.connect(database)
    cursor = db.cursor()
    cursor.execute(INSERT_EMPLOYEE, (id, name, monthly_salary, yearly_bonus,
                                     position))

    db.commit()
    db.close()


def del_employee(database, uid):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (uid, ))
    db.commit()
    db.close()


def main():
    cmd = ''
    while cmd != 'quit':
        cmd = input("command> ")
        if cmd == 'list_employees':
            list_employees(DB_NAME)
        elif cmd == 'monthly_spending':
            print(monthly_spending(DB_NAME))
        elif cmd == 'yearly_spending':
            print(yearly_spending(DB_NAME))
        elif cmd == 'add_employee':
            add_employee(DB_NAME)
        elif cmd == 'del_employee':
            uid = int(input("ID: "))
            del_employee(DB_NAME, uid)
        else:
            continue


if __name__ == "__main__":
    main()
