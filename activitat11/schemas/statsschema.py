def statschema(stat):
    return {"Nomjugador":stat[0],
            "PuntsPactual":stat[1],
            "TotalPartides":stat[2],
            "PartidesGuanyades":stat[3],
            "Partidaambméspunts":stat[4]}

def statsschemas(statics) -> list[dict]:
    return [statschema(stat) for stat in statics]