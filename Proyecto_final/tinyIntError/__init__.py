from .error import TinyIntError
from .validates import validate_tinyInt, validate_value
def tiny_int(val):
    try:
        if validate_value(val) and validate_tinyInt(val):
            return True
        else:
            raise TinyIntError
    except TinyIntError as error:
        print(error)