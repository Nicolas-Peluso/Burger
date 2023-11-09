import re
def validar_senha(senha):
    if len(senha) < 8:
        return False;
    
    if not re.search(r'[a-z]', senha):
        return False;
    
    if not re.search(r'[A-Z]', senha):
        return False;
    
    return True;