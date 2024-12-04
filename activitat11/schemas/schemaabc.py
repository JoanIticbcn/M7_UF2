def abcschema(abc):
    return {"Lletra":abc}

def abcsSchema(abcs) -> list[dict]:
    return [abcschema(abc) for abc in abcs]