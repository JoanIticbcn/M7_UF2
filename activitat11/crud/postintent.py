def postintentmethod(conn,numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador):
    cursor = conn.cursor()
    sqlpost = "INSERT INTO registrejoc (numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador) VALUES (%s,%s,%s,%s,%s,%s)"
    valors = (numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador)
    cursor.execute(sqlpost,valors)
    conn.commit()
    return "Insert successful"
