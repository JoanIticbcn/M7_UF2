def putpantallap(conn,idioma,comencarpartidabutton):
    cursor = conn.cursor()
    query = "UPDATE pantallaprincipal SET comencarpartidabutton=%s WHERE idioma=%s"
    cursor.execute(query,(comencarpartidabutton,idioma))
    conn.commit()
    return "Update successfull"