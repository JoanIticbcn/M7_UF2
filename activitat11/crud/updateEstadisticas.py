def updateestadisticasdeljoc(conn,nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts):
    cursor = conn.cursor()
    sqlupdate = "UPDATE usuaris SET (puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts) VALUES (%s,%s,%s,%s,%s) WHERE nomjugador=%s"
    valors = (puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts,nomjugador)
    cursor.execute(sqlupdate, valors)
    conn.commit()
    return "Update succesful"