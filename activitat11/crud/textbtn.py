def getbuttontext(idioma,conn) -> str:
    cursor = conn.cursor()
    sqlquery = "SELECT %s FROM %s WHERE idioma=%s"
    valors = ("comencarpartidabutton","pantallaprincipal",idioma,)
    cursor.execute(sqlquery,valors)
    resultat = cursor.fetchone()
    return resultat