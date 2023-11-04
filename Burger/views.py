from django.shortcuts import render
from Burger.models import Pedidos;
from Burger.senhasValidador import validar_senha
from Burger.emailvalidate import ValidarEmail
from Burger.hashDeSenhas import Hashing

def Index(req):
    return render(req, 'Burger/index.html') 

def Cadastro(req):
        senha = req.POST.get('senha')
        email = req.POST.get('email')

        #valida por expressão regular
        verificaSenha = validar_senha(senha);
        verificaEmail =  ValidarEmail(email);

        #verificação caso erro na validação
        if not verificaSenha == True and not verificaEmail != True:
            print(verificaEmail)
            print(verificaSenha)
            return render(req, 'Burger/index.html')
        
        else:
            users = Pedidos();

            #hash da senha
            hashed = Hashing(senha)
            
            users.SenhaCliente = hashed;
            users.NomeCliente = email;
            users.save();   
            dados = {
            'usuario': email
            }
            return render(req, 'formularioLoginBurger/login.html', dados);
