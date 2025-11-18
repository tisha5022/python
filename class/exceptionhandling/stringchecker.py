class InvalidStringException(Exception):
    pass


def check(str):
    if str.isalpha():
        print("Valid")
    else:
        raise InvalidStringException()
    

check("adfdfs")