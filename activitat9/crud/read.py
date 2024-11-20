# Funció que llegeix tots els registres de la taula users i els retorna
def read_usuaris(connexioR):
    # Defineix la query del select
    select_query = "SELECT * FROM users;"
    # Executa la query
    cursor = connexioR.cursor()
    cursor.execute(select_query)
    # Fetch de totes les columnes del resultat
    rows = cursor.fetchall()
    #Tanquem la connexio
    connexioR.close()
    return rows