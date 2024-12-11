def statschema(stat):
    return {"Lletra":stat}

def statsschemas(statics) -> list[dict]:
    return [statschema(stat) for stat in statics]