def cruddelteregistredeljoc(conn,idjugador):
    cursor = conn.cursor()
    query = "DELETE FROM registredeljoc where idjugador=%s"
    cursor.execute(query,(idjugador,))
    conn.commit()
    return "Delete succesfull"