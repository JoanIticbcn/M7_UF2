def putcrudparaula(conn,parauladisplayactual,idjugador):
    cursor = conn.cursor()
    query = "UPDATE paraules SET parauladisplayactual=%s WHERE idjugador=%s"
    cursor.execute(query,(parauladisplayactual,int(idjugador)))
    conn.commit()
    return "Update succesfull"