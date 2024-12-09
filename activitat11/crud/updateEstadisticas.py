def updateestadisticasdeljoc(conn,nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts):
    cursor = conn.cursor()
    sqlupdate = "UPDATE usuaris SET (puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts) VALUES (%s,%s,%s,%s) WHERE nomjugador=%s"
    valors = (int(puntspartidaactual),int(totalpartides),int(partidesguanyades),str(partidaambmespunts),str(nomjugador))
    cursor.execute(sqlupdate, valors)
    conn.commit()
    return "Update succesful"