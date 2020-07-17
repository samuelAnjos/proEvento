from pathlib import Path # verifica o caminho para ver se o arquivo existe
import time
import os #biblioteca que tem funçoes limpar tela
# 1º verificacao de CPF
def subMenu():
    print()
    print('-----------------------    ------------------    -------- ')
    print('1- Cadastro de Cliente|    2- Mostrar Perfil|    3- Sair|')
    print('-----------------------    ------------------    -------- ')
    escolhar = int(input('Escolha uma opção: '))
    return escolhar
#-----------------------------------
def agenda():
    os.system('clear')
    print('----------------------------')
    print('|  AGENDA SEU NOVO EVENTO  |')
    print('----------------------------')
    print()
    agendar = open('agendaEventos', 'a')
    nome = input('Informe qual é o seu evento: ')
    data = input('Digite uma data[dd/mm/aa]: ')
    # aqui pode Criar, algo para verificar se ja tem uma data cadastrada
    agendar.write(nome + ' ' + data + '\n')

    agendar.close()
#------------------------------------------

def listarClientes():
    cadastros = open('cadastro.txt', 'r')
    print('  Lista de clientes cadastrados  ')
    print('---------------------------------')
    print()
    for linhas in cadastros:
                linhas = linhas.rstrip()
                print(linhas)
    cadastros.close()
    

    #  vamos ver se conseguer tirar esse idea de verificar se o Aruivo exist

#---------------------------------------

def confirmacaoDeInscricao():
    os.system('clear')
    print('-------------------------------')
    print('Clienta Cadastrado Com Sucesso.')
    print('-------------------------------')
    time.sleep(3)
#-------------------------------------
#--------------------------------------cpf
def validarcpf(cpfs):
    
    cpf_c = cpfs
    if len(cpf_c) < 11 or len(cpf_c) > 11:
        return 0
    cpf = int(cpf_c)
    somas = []
    cont = 9
    aux = cpf
    verificador2 = cpf % 10
    aux //= 10
    verificador1 = aux % 10
    aux //= 10
    for i in range(9):
        somas.append((aux % 10) * cont)
        aux //= 10
        cont -= 1
        aux = sum(somas) % 11
        if aux == 10:
            aux = 0
#proximo digito verificador#
    if aux == verificador1:
        aux = cpf
        aux //= 10
        cont = 9
        somas = []
        for i in range(10):
            somas.append((aux % 10) * cont)
            aux //= 10
            cont -= 1
        
        aux = sum(somas) % 11
        if aux == 10:
            aux = 0
        if aux == verificador2:
            return 1
        else:
            return 0
    else:
        return 0
#-------------------------------------    
def cadastroDeCliente():
    cadastros = open('cadastro.txt', 'a')
    os.system('clear')
    print('  Cadastro de novos clientes  ')
    print('------------------------------')
    print()
    nome = input('Informe seu nome completo: ')
    idade = input('Digite sua idade: ')
    cpfs = input('Informe seu CPF: ')
    valido = validarcpf(cpfs)
    time.sleep(3)

    if valido == 1:
        localidade = input('Informe Cidade onde mora e, Estado: ')
        cadastros.write(nome + ' ' + idade + ' '+ cpfs +' '+ localidade + '\n')
        agenda()
        confirmacaoDeInscricao()
        cadastros.close()
    else:
        # Rigido kkkkk
        print('CPF Inválido!!! :)')
        print("Voltaremos ao Menu")
        time.sleep(7)
    

# inicio de execucao

escolhar = subMenu()
if escolhar == 1:
    cadastroDeCliente()
    os.system('clear')  
    subMenu()  # depoiss trocar pelo Menu Principal  

elif escolhar == 2:
    verificarCaminho = Path('./cadastro.txt') # ver sem existe esse arquivo

    if verificarCaminho.is_file():

        with open(verificarCaminho, 'r') as f:
            os.system('clear')
            listarClientes()
            time.sleep(5)
            respp = input("Quer mostrar a lista de clientas novamente? ")
            if respp == 's':
                os.system('clear')
                listarClientes()
                time.sleep(5)
                os.system('clear')
                subMenu()

            else:
                os.system('clear')    
                subMenu()
            time.sleep(5) # agenda con
            os.system('clear')
            
    else:
        print('Arquivo inexistente :(')
        time.sleep(2)
    #====================================  
    os.system('clear')    
    subMenu()  
elif escolhar == 3:
    print('Saindoo...')
    time.sleep(1)
    os.system('clear')
else:
    print('Ops! Opção inválida. Escolha entre [1, 2, 3]')
    time.sleep(5)
    os.system('clear')
    subMenu()
    



    