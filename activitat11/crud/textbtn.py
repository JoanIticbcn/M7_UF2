def getbuttontext(conn,idioma) -> str:
    cursor = conn.cursor()
    sqlquery = "SELECT comencarpartidabutton FROM pantallaprincipal WHERE idioma=%s"
    cursor.execute(sqlquery,(idioma,))
    resultat = cursor.fetchone()
    print(idioma)
    return str(resultat)