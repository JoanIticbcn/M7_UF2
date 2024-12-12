def postcrudparaula(conn,parauladisplayinicial,parauladisplayactual,paraulasecreta,idjugador,idioma):
    cursor = conn.cursor()
    query = "INSERT INTO paraules VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(parauladisplayinicial,parauladisplayactual,paraulasecreta,int(idjugador),idioma))
    conn.commit()
    return "Post succesfull"