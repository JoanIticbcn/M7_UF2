def paraulesgetchema(paraula):
    return {"parauladisplayinicial":paraula[0],
            "parauladisplayactual":paraula[1],
            "paraulasecreta":paraula[2],
            "idjugador":paraula[3],
            "idioma":paraula[4]}

def paraulesgetschemas(paraules) -> list[dict]:
    return [paraulesgetchema(paraula) for paraula in paraules]