def validate_tinyInt(val):
    return val >=0 and val <= 255

def validate_value(val):
    try:
        return isinstance(int(val), int)
    except ValueError as error:
        return False
