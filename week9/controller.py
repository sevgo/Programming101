import sqlite3
from Client import Client

class Controller:

    LOGIN_SQL = """
    SELECT id, username, balance, message
    FROM clients
    WHERE username=? AND password=?
    LIMIT 1 """

    CHANGE_PASS_SQL = """
    UPDATE clients
    SET password=?
    WHERE id=? """

    UPDATE_MSG_SQL = """
    UPDATE clients
    SET message=?
    WHERE id=? """

    INSERT_CLIENT_SQL = """
    INSERT INTO clients(username, password) VALUES(?, ?)
    """

    def __init__(self, conn):
        self.conn = conn
        self.curr = self.conn.cursor()

    def change_message(self, new_message, logged_user):
        self.curr.execute(Controller.UPDATE_MSG_SQL,
                          (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        self.curr.execute(Controller.CHANGE_PASS_SQL,
                          (new_pass, logged_user.get_id()))
        self.conn.commit()

    def register(self, username, password):
        self.curr.execute(Controller.REGISTER_CLIENT_SQL,
                          (username, password))
        self.conn.commit()

    def login(self, username, password):
        self.curr.execute(Controller.LOGIN_SQL,
                          (username, password))
        user = self.curr.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
