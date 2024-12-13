def getPantallaprincipalcrud(conn):
    cursor = conn.cursor()
    query = "select * from pantallaprincipal"
    cursor.execute(query)
    resultat = cursor.fetchall()
    return resultat