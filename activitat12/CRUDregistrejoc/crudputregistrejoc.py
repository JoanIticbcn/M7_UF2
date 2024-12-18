def putcrudregistrejoc(conn,numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador):
    cursor = conn.cursor()
    query = "UPDATE paraules SET parauladisplayactual=%s WHERE idjugador=%s"
    cursor.execute(query,(numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador))
    conn.commit()
    return "Update succesfull"