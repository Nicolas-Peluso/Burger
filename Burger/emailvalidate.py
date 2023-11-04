import re
def ValidarEmail(email):
    if len(email) == 0:
        return 'email não pode estar vazio'
    else:
        return True
    #aqui usar uma expressão regular não é a melhors das ideias visto que um email pode ser algo dos mais diversos
    #apenas vou verificar se o email não esta vazio outras vericficações incluem: enviar um código para o email 