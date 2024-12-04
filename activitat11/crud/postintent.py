def postintentmethod(conn,numerointent,estatpartida,encertada,fallada,lletrautilitzada):
    cursor = conn.cursor()
    sqlpost = "INSERT INTO registrejoc (numerointent,estatpartida,encertada,fallada,lletrautilitzada) VALUES (%s,%s,%s,%s,%s)"
    valors = (numerointent,estatpartida,encertada,fallada,lletrautilitzada)
    cursor.execute(sqlpost,valors)
    conn.commit()
    return "Insert successful"
