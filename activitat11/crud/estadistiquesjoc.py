def getEstadistiquesdeljoc(conn,nom):
    cursor = conn.cursor()
    sqlquery = "SELECT nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts FROM usuaris WHERE nomjugador=%s"
    cursor.execute(sqlquery,(nom,))
    resultat = cursor.fetchall()
    return resultat