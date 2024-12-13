def pantallaschema(pnt):
    return {"idioma":pnt[0],
            "comencarpartidabutton":pnt[1],
            "lletrasabecedari":pnt[2],}

def pantallaprincipalschemas(pantalles) -> list[dict]:
    return [pantallaschema(pnt) for pnt in pantalles]