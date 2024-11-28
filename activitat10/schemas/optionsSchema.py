def optionSchema(option):
    return {
        "option":option
    }

def optionsSchema(options) -> list[dict]:
    return [optionSchema(option) for option in options]