def crudparauladelete(conn,idjugador):
    cursor = conn.cursor()
    query = "DELETE FROM paraules where idjugador=%s"
    cursor.execute(query,(int(idjugador),))
    conn.commit()
    return "Delete succesfull"