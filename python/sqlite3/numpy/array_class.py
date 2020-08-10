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

    def adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def insert(self, arr):
        self.cursor.execute("INSERT INTO data (arr) values (?)", (arr, ))

    def first_select(self):
        self.cursor.execute("SELECT arr FROM data LIMIT 1")
        self.data = self.cursor.fetchall()

    def first_delete(self):
        self.cursor.execute("""DELETE FROM data WHERE id in (
            SELECT id FROM data LIMIT 1)""")

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

x = np.random.rand(8760)

x_sql = SQLNumpy("test.db")
# x_sql.insert(x)

x_sql.first_select()
print(x_sql.data)
x_sql.first_delete()
x_sql.commit()
x_sql.close()

