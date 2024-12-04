def getabecedari(idioma,conn):
    cursor = conn.cursor()
    sqlabc = "SELECT %s FROM %s WHERE idioma=%s"
    valors = ("lletrasabecedari","pantallaprincipal",idioma)
    cursor.execute(sqlabc,valors)
    resultat = cursor.fetchall()
    return resultat