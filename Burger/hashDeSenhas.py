import hashlib
#essa função sera usada tanto para cadastro quanto para a comparação no login
def Hashing(stri):
    value = hashlib.sha256(stri.encode()).hexdigest()
    return value