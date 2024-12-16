def getregistredeljoc(conn):
    cursor = conn.cursor()
    query = "select * from registrejoc"
    cursor.execute(query)
    resultat = cursor.fetchall()
    return resultat