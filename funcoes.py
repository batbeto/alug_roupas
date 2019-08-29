from datetime import date
import valida_cpf
import pickle

#####TESTE PARA SAIDA DE TODOS OS WHILES
def testeSaida(test):
    a=True
    while a:
        if test.upper() == 'N':
            return False
            a=False
        elif test.upper() == 'S':
            return True
            a=False
        else:
            test=input("Digite qpenas S ou N, por favor!")

def arqClientes(clientes):
    arqClientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arqClientes)
    arqClientes.close()
    return print("Cliente cadastrado com sucesso!!!")


def cadastroFantasia(fantasias):
    cadf = True
    while cadf:
        numFan = input("Digite o numero da fantasia: ")
        if numFan.isnumeric():
            if numFan not in fantasias:
                print(f'O numero de sua fantasia é {numFan}')
                nomeFan = input("Digite o nome da fantasia: ")
                a=True
                while a:
                    tamFan = input("Digite o tamanho da fantasia(P,M,G ou GG):")
                    a = autenticaTam(tamFan)
                catFan = input("Em que categoria esta incluida a fantasia?")
                custoFan = input("Qual foi o custo de compra da fantasia: ")
                descFan = input("Faça uma breve descrição sobre a fantasia: ")
                quantFan = 0
                statusFan = '0'
                lucroFan = 0
                fantasias[numFan] = [nomeFan, tamFan, catFan, custoFan, descFan, quantFan, statusFan, lucroFan]
                arqFantasias(fantasias)
                test = input('Deseja continuar? Digite S ou N: ')
                cadf = testeSaida(test)
            else:
                test = input("Numero já existe, deseja continuar S ou N?")
                cadf = testeSaida(test)
        else:
            print('Tente novamente apenas com numeros')
    return fantasias


def arqFantasias(fantasias):
    arqFantasias = open("fantasias.dat", "wb")
    pickle.dump(fantasias, arqFantasias)
    arqFantasias.close()
    return print("Fantasia cadastrada com sucesso!!!")


def arqAluguel(aluguel):
    arqAluguel = open("aluguel.dat", "wb")
    pickle.dump(aluguel, arqAluguel)
    arqAluguel.close()
    return print("Aluguel cadastrado com sucesso!!!")

def cadastroCliente(clientes):
    menuc = True
    while menuc:
        cad = True
        while cad:
            cpf = input('Digite o CPF do cliente a ser cadastrado: ')
            isCont = not valida_cpf.validar_cpf(cpf)
            while isCont:
                cpf = input('CPF invalido, tente novamente ou digite "Sair": ')
                if cpf.upper() == 'SAIR':
                    isCont = False
                else:
                    isCont = not valida_cpf.validar_cpf(cpf)

            if cpf not in clientes:
                nome = input('Digite o nome do cliente a ser inserido na lista: ')
                email = input('Digite o e-mail do cliente a ser inserido na lista: ')
                telefone = input('Digite o telefone do cliente a ser inserido na lista: ')
                clientes[cpf] = [nome, email, telefone]
                arqClientes(clientes)
                test = input('Deseja continuar? Digite S ou N: ')
                cad = testeSaida(test)
                menuc = testeSaida(test)
            else:
                print("Cliente já cadastrado! ")
                test = input('Deseja continuar? Digite S ou N: ')
                cad = testeSaida(test)
                menuc = testeSaida(test)
    return clientes



def editCliente(clientes):
    comp=True
    while comp:
        cpf = input('Digite o CPF do cliente: ')
        isCont = not valida_cpf.validar_cpf(cpf)
        while isCont:
            cpf = input('CPF invalido, tente novamente ou digite "Sair": ')
            if cpf.upper() == 'SAIR':
                isCont = False
            else:
                isCont = not valida_cpf.validar_cpf(cpf)
        if cpf not in clientes:
            print("CPF não cadastrado...")
            test = input('Deseja continuar? Digite S ou N: ')
            comp = testeSaida(test)
        else:
            print(f'CPF:{cpf} encontrado!')
            print(f'O nome é:{clientes[cpf][0]}')
            print(f'O e-mail é:{clientes[cpf][1]}')
            print(f'O telefone é:{clientes[cpf][2]}')
            editor = input('Qual você quer editar:\n1-Nome\n2-Telefone\n3-E-mail\n4-Sair\nEscolha: ')
            if editor == '1':
                nome = input("Digite o novo nome: ")
                clientes[cpf][0] = nome
                arqClientes(clientes)
            elif editor == '2':
                telefone = input('Digite o novo telefone: ')
                clientes[cpf][2] = telefone
                arqClientes(clientes)
            elif editor == '3':
                email = input("Digite o novo e-mail: ")
                clientes[cpf][1] = email
                arqClientes(clientes)
            elif editor == '4':
                comp = False
            else:
                editor = input('Digite um numero valido:\n1-Nome\n2-Telefone\n3-E-mail\n4-Sair\nEscolha: ')



def apagarCliente(clientes):
    obliterador = True
    while obliterador:
        cpf = input('Digite o CPF do cliente a ser deletado: ')
        isCont = not valida_cpf.validar_cpf(cpf)
        while isCont:
            cpf = input('CPF invalido, tente novamente ou digite "Sair": ')
            if cpf.upper() == 'SAIR':
                isCont = False
            else:
                isCont = not valida_cpf.validar_cpf(cpf)
        print(clientes.pop(cpf, 'Não encontrado!'))
        arqClientes(clientes)
        print('Cliente obliterado!!!')
        test = input('Deseja continuar? S ou N: ')
        obliterador = testeSaida(test)

def editFantasia(fantasias):
    comp = True

    while comp:
        numFan = input('Digite o numero da fantasia: ')
        if numFan not in fantasias:
            numFan = input("Fantasia não encontrada, tente novamente ou digite S para sair: ")
            if numFan.upper()== 'S':
                comp = False
        else:
            print(f'Fantasia encontrada! {numFan}')
            print(f'O nome é: {fantasias[numFan][0]}')
            print(f'O tamanho é: {fantasias[numFan][1]}')
            print(f'A categoria é: {fantasias[numFan][2]}')
            print(f'O custo foi: {fantasias[numFan][3]}')
            print(f'Descrição: {fantasias[numFan][4]}')
            editorFan = input('''
                  1- Editar Nome
                  2- Editar Tamanho
                  3- Editar Categoria
                  4- Editar Custo
                  5- Editar Descrição
                  6- Sair
                  Qual você deseja editar? ''')
            if editorFan == '1':
                nome = input('Digite o novo nome: ')
                fantasias[numFan][0] = nome
                arqFantasias(fantasias)
            elif editorFan == '2':
                a = True
                while a:
                    tamFan = input("Digite o tamanho da fantasia(P,M,G ou GG):")
                    a = autenticaTam(tamFan)
                fantasias[numFan][1] = tamFan
                arqFantasias(fantasias)
            elif editorFan == '3':
                categoria = input('Digite a nova categoria: ')
                fantasias[numFan][2] = categoria
                arqFantasias(fantasias)
            elif editorFan == '4':
                custo = input('Digite o novo custo: ')
                fantasias[numFan][3] = custo
                arqFantasias(fantasias)
            elif editorFan == '5':
                descricao = input('Digite a nova descrição: ')
                fantasias[numFan][4] = descricao
                arqFantasias(fantasias)
            elif editorFan == '6':
                comp = False
            else:
                test = input('Opção errada, deseja continuar? S ou N')
                testeSaida(test)

def apagarFantasia(fantasias):
    comp=True
    while comp:
        numFan = input('Digite o numero da fantasia a ser deletado: ')
        print(fantasias.pop(numFan, 'Fantasia não encontrada!'))
        arqFantasias(fantasias)
        test = input('Deseja continuar? S ou N: ')
        comp = testeSaida(test)


def autenticaTam(tamFan):
  if tamFan.upper() == 'GG':
    return False
  elif tamFan.upper() == 'G':
    return False
  elif tamFan.upper() == 'M':
    return False
  elif tamFan.upper() == 'P':
    return False
  else:
    return True

def arqCaixa(caixa):
    arqCaixa = open("caixa.dat", "wb")
    pickle.dump(caixa, arqCaixa)
    arqCaixa.close()
    return print("Registado em caixa!!!")


def funcaoCaixa(total,caixa):
    hoje=date.today()
    hoje = hoje.strftime('%d-%m-%Y')
    periodoCaixa = hoje.split('-')
    mesCaixa = periodoCaixa[1]
    anoCaixa = periodoCaixa[2]
    chaveCaixa = (mesCaixa+'-'+anoCaixa)
    totalMes = (caixa[chaveCaixa][2]+total)
    caixa[chaveCaixa] = [mesCaixa, anoCaixa, totalMes]
    return caixa