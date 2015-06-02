from sql_manager import DBManager


class Controller:
    def __init__(self, connection):
        self.conn = connection
        self.curr = connection.cursor()

    def get_username(self):
        pass
