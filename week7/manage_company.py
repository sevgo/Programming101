#!/usr/bin/env python3
import sqlite3

DB_NAME = "company.db"
LIST_EMPLOYEES = '''SELECT id, name, position FROM users'''
MONTHLY_SALARY = '''SELECT monthly_salary FROM users'''
YEARLY_SPENDING = '''SELECT monthly_salary, yearly_bonus FROM users'''
INSERT_EMPLOYEE = '''INSERT INTO users(id, name, monthly_salary, yearly_bonus,
                    position) VALUES(?, ?, ?, ?, ?)'''
USER_ID = '''SELECT id FROM users'''
UPDATE_EMPLOYEE = '''UPDATE users SET name = ?, monthly_salary = ?,
                    yearly_bonus = ?, position = ? WHERE id = ? '''


def fetch_result(sql):
    db = sqlite3.connect(DB_NAME, detect_types=True)
    cursor = db.cursor()
    results = cursor.execute(sql)
    result = [el for el in results]
    db.close()
    return result


def list_employees():
    result = fetch_result(LIST_EMPLOYEES)
    for row in result:
        print("%d - %s - %s" % row)


def monthly_spending():
    result = fetch_result(MONTHLY_SALARY)
    total_salaries = 0
    for row in result:
        total_salaries += row[0]

    return total_salaries


def yearly_spending():
    result = fetch_result(YEARLY_SPENDING)
    money = [row for row in result]
    return sum([sum(el) for el in zip(*money)])


def last_user_id(sql):
    result = fetch_result(USER_ID)
    ids = [row for row in zip(*result)]
    return max(ids.pop())


def add_employee():
    uid = last_user_id(USER_ID) + 1
    name = input("Name Family: ")
    monthly_salary = int(input("Monthly Salary: "))
    yearly_bonus = int(input("Yearly Bobys: "))
    position = input("Position in company: ")
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(INSERT_EMPLOYEE, (uid, name, monthly_salary, yearly_bonus,
                                     position))

    db.commit()
    db.close()


def del_employee(uid):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (uid, ))
    db.commit()
    db.close()


def update_employee(uid):
    name = input("Name: ")
    monthly_salary = int(input("monthly_salary: "))
    yearly_bonus = int(input("yearly_bonus: "))
    position = input("Position: ")
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(UPDATE_EMPLOYEE, (name, monthly_salary, yearly_bonus,
                                     position, uid))
    db.commit()
    db.close()


def help():
    print(''' Available commands:
          list_employees        :    list all employees
          monthly_spending      :    print how much company spend every month
          yearly_spending       :    print how much company spend every year
          add_employee          :    add a new employee
          update_employee       :    update all information about an employee
          del_employee          :    delete an employee by given id
          help                  :    print this help
          quit                  :    exit
          ''')


def main():
    cmd = 'help'
    while cmd != 'quit':
        cmd = input("command> ")
        if cmd == 'list_employees':
            list_employees()
        elif cmd == 'monthly_spending':
            print(monthly_spending())
        elif cmd == 'yearly_spending':
            print(yearly_spending())
        elif cmd == 'add_employee':
            add_employee()
        elif cmd == 'del_employee':
            uid = int(input("ID: "))
            del_employee(uid)
        elif cmd == 'update_employee':
            uid = int(input("ID: "))
            update_employee(uid)
        elif cmd == 'help':
            help()
        else:
            help()
            continue


if __name__ == "__main__":
    main()
