def postusuari(conn,idjugador,nomjugador,numerojugades,puntspartidaactual,totalpartides,partidaambmespunts):
    cursor = conn.cursor()
    query = "INSERT INTO paraules VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(idjugador,nomjugador,numerojugades,puntspartidaactual,totalpartides,partidaambmespunts))
    conn.commit()
    return "Post succesfull"