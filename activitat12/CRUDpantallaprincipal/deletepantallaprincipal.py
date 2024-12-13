def deletepantallap(conn,idioma):
    cursor = conn.cursor()
    query = "DELETE FROM pantallaprincipal where idioma=%s"
    cursor.execute(query,(idioma,))
    conn.commit()
    return "Delete succesfull"