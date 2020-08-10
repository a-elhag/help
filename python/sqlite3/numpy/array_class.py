import sqlite3
import numpy as np
import io

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

# Converts np.array to TEXT when inserting
sqlite3.register_adapter(np.ndarray, adapt_array)

# Converts TEXT to np.array when selecting
sqlite3.register_converter("array", convert_array)

x = np.arange(12).reshape(2,6)

conn = sqlite3.connect("numpy.db", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()
# cur.execute("create table test (arr array)")

cursor.execute("insert into test (arr) values (?)", (x, ))

cursor.execute("select * from test")
data = cursor.fetchall()

conn.commit()
conn.close()
print(data)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]
print(type(data))
# <type 'numpy.ndarray'>
