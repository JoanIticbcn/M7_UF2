def readWord(conn,tema : str):
    cursor = conn.cursor()
    sqlword = "SELECT word FROM act10 WHERE theme = %s ORDER BY RANDOM() LIMIT 1;"
    cursor.execute(sqlword,(tema,))
    result = cursor.fetchone()
    return result