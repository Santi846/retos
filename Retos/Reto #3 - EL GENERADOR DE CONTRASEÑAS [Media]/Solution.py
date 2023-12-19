import secrets
# import string

def generatePass():
    
    # alphabet = string.ascii_letters + string.digits
    # password = ''.join(secrets.choice(alphabet) for i in range(16))
    # return password
    token = secrets.token_urlsafe(32)
    return token

generatePass()