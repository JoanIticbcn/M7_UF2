def getabecedaris(idioma,conn):
    cursor = conn.cursor()
    sqlabc = "SELECT lletrasabecedari FROM pantallaprincipal WHERE idioma=%s"
    cursor.execute(sqlabc,(idioma,))
    resultat = cursor.fetchall()
    return resultat