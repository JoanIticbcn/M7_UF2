import pandas as pd
import psycopg2

df = pd.read_csv('../paraules_penjat.csv')
list_of_dicts = df.to_dict(orient="records")

try:
    conn = psycopg2.connect(
        database="postgres",
        user='user_postgres',
        password='pass_postgres',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    for i in list_of_dicts:
        sql = "INSERT INTO act10 VALUES(%s,%s)"
        valors = (i["WORD"],i["THEME"])
        cursor.execute(sql,valors)
    conn.commit()
except(Exception,psycopg2.Error) as error:
    print("Error ",error)