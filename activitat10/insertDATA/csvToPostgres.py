import pandas as pd
import psycopg2

from conn import getConn

df = pd.read_csv('../paraules_penjat.csv')
list_of_dicts = df.to_dict(orient="records")

conn = getConn()
cursor = conn.cursor()
for i in list_of_dicts:
    sql = "INSERT INTO act10 VALUES(%s,%s)"
    valors = (i["word"],i["theme"])
    cursor.execute(sql,valors)
conn.commit()