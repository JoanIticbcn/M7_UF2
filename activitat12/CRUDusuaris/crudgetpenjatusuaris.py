def getcrudUsuarisPenjat(conn):
    cursor = conn.cursor()
    query = "select * from usuaris"
    cursor.execute(query)
    resultat = cursor.fetchall()
    return resultat