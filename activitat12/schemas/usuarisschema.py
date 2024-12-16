def usuarischema2(user):
    return {"idjugador":user[0],
            "nomjugador":user[1],
            "numerojugades":user[2],
            "puntspartidaactual":user[3],
            "totalpartides":user[4],
            "partidaambmespunts":user[5]}

def usuarisschemas1(users) -> list[dict]:
    return [usuarischema2(usuari) for usuari in users]