import pyodbc


class SqlService:
    def __init__(self, driver, server, database, user, password, trust):
        self.driver = driver
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.trust = trust

    def __open_connection(self):
        auth = 'Trusted_Connection=yes;' if self.trust is True else f'Uid={self.user};Pwd={self.password};'
        return pyodbc.connect(
            f'Driver={{{self.driver}}};Server={self.server};Database={self.database};{auth}')

    @staticmethod
    def drivers():
        return pyodbc.drivers()

    def test_connection(self):
        conn = self.__open_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        row = cursor.fetchone()
        return row[0] > 0
