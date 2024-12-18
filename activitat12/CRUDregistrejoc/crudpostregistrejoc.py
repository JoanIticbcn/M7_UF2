def postregistredeljoccrud(conn,numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador):
    cursor = conn.cursor()
    query = "INSERT INTO registrejoc VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador))
    conn.commit()
    return "Post succesfull"