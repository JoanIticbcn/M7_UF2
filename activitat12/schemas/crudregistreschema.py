def registreschema(regi):
    return {"numerointent":regi[0],
            "estatpartida":regi[1],
            "encertada":regi[2],
            "fallada":regi[3],
            "lletrautilitzada":regi[4],
            "idjugador":regi[5]}

def registreschemas(registres) -> list[dict]:
    return [registreschema(reg) for reg in registres]