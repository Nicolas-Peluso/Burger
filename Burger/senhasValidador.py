import re
def validar_senha(senha):
    if len(senha) < 8:
        return 'senha deve ter mais que 8 caracteres'
    
    if not re.search(r'[a-z]', senha):
        return 'senha deve ter uma letra minuscula'
    
    if not re.search(r'[A-Z]', senha):
        return 'senha deve ter uma letra maiuscula'

    return True