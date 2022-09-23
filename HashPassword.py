from encodings import utf_8
import hashlib
import string
import secrets

def Hashpassword(password:str):
    """Generates a salt and appends it to a password and returns the hash and salt value
    Uses Password+salt formula. 

    Args:
       User submitted password

    Returns:
       Salt value and hashed value of password+salt
    """

    saltGen = secrets.token_hex(32)
    as_bytes = bytes(password, "utf8")
    saltGen_as_bytes = bytes(saltGen, "utf8")
    m = hashlib.sha256()
    m.update(as_bytes)
    m.update(saltGen_as_bytes)
    print("Salt: ", saltGen)
    print("Hashed password+salt: ", m.hexdigest())

if __name__ == "__main__":
    import sys
    Hashpassword(sys.argv[1])