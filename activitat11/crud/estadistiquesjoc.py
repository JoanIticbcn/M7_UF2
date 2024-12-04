def getEstadistiquesdeljoc(conn,nom):
    cursor = conn.cursor()
    sqlquery = "SELECT nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts FROM usuaris WHERE nomjugador=%s"
    valors = (nom,)
    cursor.execute(sqlquery,valors)
    resultat = cursor.fetchall()
    return resultat