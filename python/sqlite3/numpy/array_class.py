import io
import numpy as np
import sqlite3

class SQLNumpy():
    """This will insert a numpy array into a sqlite3 instance"""
    def __init__(self, db_name):
        # Converts np.array to TEXT when inserting
        sqlite3.register_adapter(np.ndarray, self.adapt_array)
        # Converts TEXT to np.array when selecting
        sqlite3.register_converter("array", self.convert_array)

        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        arr ARRAY);""")

    def adapt_array(arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def insert(self, arr):
        self.cursor.execute("INSERT INTO data (arr) values (?)", (arr, ))


x = np.arange(12).reshape(2,6)

x_sql = SQLNumpy("test.db")
x_sql.insert(x)
