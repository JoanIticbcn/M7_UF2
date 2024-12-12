def getParaulesss(conn):
    cursor = conn.cursor()
    query = "select * from paraules"
    cursor.execute(query)
    resultat = cursor.fetchall()
    return resultat