def gettextinicial(idioma,conn) -> str:
    cursor = conn.cursor()
    sqlquery = "SELECT parauladisplayinicial FROM paraules WHERE idioma=%s"
    cursor.execute(sqlquery,(idioma,))
    resultat = cursor.fetchone()
    return resultat