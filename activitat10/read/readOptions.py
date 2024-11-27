def readOptions(conn):
    cursor = conn.cursor()
    sqlTheme = "SELECT DISTINCT theme FROM act10"
    cursor.execute(sqlTheme)
    result = cursor.fetchall()
    return result