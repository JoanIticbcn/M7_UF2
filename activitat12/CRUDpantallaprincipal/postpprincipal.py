def postpantallaprincipalcrud(conn,idioma,comencarpartidabutton,lletrasabecedari):
    cursor = conn.cursor()
    query = "INSERT INTO pantallaprincipal VALUES(%s,%s,%s)"
    cursor.execute(query,(idioma,comencarpartidabutton,lletrasabecedari))
    conn.commit()
    return "Post succesfull"