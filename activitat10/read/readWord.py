def readWord(conn,tema):
    cursor = conn.cursor()
    sqlWord = "SELECT word FROM act10 WHERE theme = %s ORDER BY RANDOM() LIMIT 1;"
    cursor.execute(sqlWord,tema)
    result = cursor.fetchone()
    return result