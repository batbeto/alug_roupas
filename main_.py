import matplotlib.pyplot as plt
from datetime import datetime, date
import menus
import valida_cpf
import funcoes
import pickle
import email_send
import re


listaFan=[]


try:
  arqAluguel = open("aluguel.dat", "rb")
  aluguel = pickle.load(arqAluguel)
  arqAluguel.close()
except IOError:
  aluguel={}
try:
  arqClientes = open("clientes.dat", "rb")
  clientes = pickle.load(arqClientes)
  arqClientes.close()
except IOError:
  clientes={}
try:
  arqFantasias = open("fantasias.dat", "rb")
  fantasias = pickle.load(arqFantasias)
  arqFantasias.close()
except IOError:
  fantasias={}

try:
  arqCaixa = open("caixa.dat", "rb")
  caixa = pickle.load(arqCaixa)
  arqCaixa.close()
except IOError:
  caixa = {}




menu = True

while menu:
  #####MENU PRINCIPAL
  opcao = menus.menuP()

  if (opcao == "1"):
    alug = True
    while alug:
      opcaoAlug = menus.opcaoAlug()
      if opcaoAlug == '1':
        cpf = input('Digite o CPF do cliente: ')
        isCont = not valida_cpf.validar_cpf(cpf)
        while isCont:
          cpf = input('''
         CPF invalido!
        TENTE NOVAMENTE
  Obs. :Se não deseja continuar digite "Sair": ''')
          if cpf.upper() == 'SAIR':
            isCont = False
          else:
            isCont = not valida_cpf.validar_cpf(cpf)
        if cpf not in clientes:
          cpf = input('''
  CPF não encontrado!
  Tente novamente
       ou
  digite "SAIR" para sair: ''')
          if cpf.upper() == 'SAIR':
            alug=False
        else:
          print(f'Cliente: {clientes[cpf][0]}')
          conta=True
          total = 0
          while conta:
            numFan = input('Digite o numero da fantasia: ')
            if numFan not in fantasias:
              test = input('''
  Fantasia não encontrada!
  Deseja continuar? S ou N: ''')
              conta = funcoes.testeSaida(test)
            else:
              print('''
  = = = = = = = = = = = = = =
    F  A  N  T  A  S  I  A
  = = = = = = = = = = = = = =''')
              print(f'Fantasia numero: {numFan} ')
              print(f'Fantasia nome: {fantasias[numFan][0]} ')
              print(f'Fantasia tamanho: {fantasias[numFan][1]} ')
              print(f'Fantasia categoria: {fantasias[numFan][2]} ')
              print(f'Fantasia descrição: {fantasias[numFan][4]} ')

              if fantasias[numFan][6] == '1':
                test=input('''
    Fantasia ocupada!
    Deseja continuar? S ou N: ''')
                conta = funcoes.testeSaida(test)
              else:
                valorFan = float(input('Digite o valor da fantasia: '))
                fantasias[numFan][7]+=valorFan
                total += valorFan
                fantasias[numFan][5]+=1
                fantasias[numFan][6] = '1'
                funcoes.arqFantasias(fantasias)
                listaFan.append(numFan)
                test = input('Deseja continuar? S ou N: ')
                conta = funcoes.testeSaida(test)
            if conta == False:
              print(f'Cliente: {clientes[cpf][0]}')
              print(f'Seu total foi: {total}')
              datahoje = date.today()
              hoje = datahoje.strftime('%d-%m-%Y')
              print(f'Hoje é: {hoje}')
              saida = date.fromordinal(datahoje.toordinal()+3)
              futuro = saida.strftime('%d-%m-%Y')
              print(f'Previsão de entrega é: {futuro}')
              datahoje = datetime.strptime(hoje, '%d-%m-%Y')

          pag = input('''
  = = = = = = = = = = = = = =
  M E N U   P A G A M E N T O
  = = = = = = = = = = = = = =
  0- À vista
  1- Na entrega
  Efetuar pagamento À vista ou na entrega? ''')
          if pag == '0':
            aluguel[cpf]= pag
          elif pag == '1':
            aluguel[cpf]=pag
          else:
            pag=input('Digite apenas 0 ou 1: ')
          aluguel[cpf] = [listaFan, total, datahoje, pag, saida]
          periodoCaixa = hoje.split('-')
          mesCaixa = periodoCaixa[1]
          anoCaixa = periodoCaixa[2]
          chaveCaixa = (mesCaixa + '-' + anoCaixa)
          if chaveCaixa in caixa:
            pass
          else:
            totalMes = 0
            caixa[chaveCaixa] = [mesCaixa, anoCaixa, totalMes]
            arqCaixa = open("caixa.dat", "wb")
            pickle.dump(caixa, arqCaixa)
            arqCaixa.close()
          funcoes.funcaoCaixa(total,caixa)
          funcoes.arqAluguel(aluguel)
          funcoes.arqCaixa(caixa)
          emailsend = input('Deseja enviar para email? S ou N: ')
          if emailsend.upper() == 'S':
            email_send.email_send(clientes,cpf,futuro)
            isCont = False
          else:
            isCont = False


      elif opcaoAlug =='2':

        cpf = input('Digite o CPF do cliente: ')
        isCont = not valida_cpf.validar_cpf(cpf)
        while isCont:
          cpf = input('''
        CPF invalido!
      Tente novamente!
  obs.: Se não deseja continuar digite "Sair": ''')

          if cpf.upper() == 'SAIR':

            isCont = False
          else:
            isCont = not valida_cpf.validar_cpf(cpf)
        if cpf not in aluguel:
          test= input("CPF não encontrado, deseja continuar? S ou N ")
          test = funcoes.testeSaida(test)
        else:
          dia_agora = date.today()
          data_agora = dia_agora.strftime('%d-%m-%Y')
          d2 = datetime.strptime(data_agora,'%d-%m-%Y')
          dias = abs((d2-aluguel[cpf][2]).days)
          if dias > 3 and aluguel[cpf][3] == '1':
            multa = abs(dias - 3)
            multaTotal = (aluguel[cpf][1]*(0.2*multa))
            print(f'O cliente tem uma multa de 20% por dia de atraso {multa}dias, o total é: {aluguel[cpf][1]+multaTotal}')
            con = input('Confirma pagamento? S ou N')
            confir = funcoes.testeSaida(con)
          elif dias > 3 and aluguel[cpf][3] == '0':
            print(f'O cliente tem uma multa de 20% por dia de atraso {multa}dias, o total é: {multaTotal}')
            con= input('Confirma pagamento? S ou N')
            confir = funcoes.testeSaida(con)
          else:
            if aluguel[cpf][3] == '1':
              print(f'O debito do cliente é {aluguel[cpf][1]}')
            else:
              print(f'O cliente já pagou seus debitos!')
            confir = True
          if confir:

            listaFan = aluguel[cpf][0]
            for i in range(len(listaFan)):
              numFan=listaFan[i]
              fantasias[numFan][6] = '0'
            funcoes.arqFantasias(fantasias)
            del aluguel[cpf]
            funcoes.arqAluguel(aluguel)

      elif opcaoAlug == '3':
        alug=False
  elif (opcao == "2"):
    a= True
    while a:
      menuCliente = menus.opcaoCliente()
      if menuCliente == '1':
        funcoes.cadastroCliente(clientes)
      elif menuCliente == '2':
          funcoes.editCliente(clientes)
      elif menuCliente == '3':
        ##### EXIBIR CLIENTE!
        cpf = input('Digite um CPF: ')
        isCont = not valida_cpf.validar_cpf(cpf)
        while isCont:
          cpf = input('''
        CPF invalido!
      Tente novamente!
  Obs.: Se não deseja continuar digite "Sair": ''')
          if cpf.upper() == 'SAIR':
            isCont = False
          else:
            isCont = not valida_cpf.validar_cpf(cpf)
        if cpf not in clientes:
          print("CPF não cadastrado...")
          test = input('Deseja continuar? Digite S ou N: ')
          comp = funcoes.testeSaida(test)
        else:
          print(f'CPF:{cpf} encontrado!')
          print(f'O nome é:{clientes[cpf][0]}')
          print(f'O e-mail é:{clientes[cpf][1]}')
          print(f'O telefone é:{clientes[cpf][2]}')
      elif menuCliente == '4':
        funcoes.apagarCliente(clientes)
      elif menuCliente == '5':
        for cpf in clientes:
          print(f'Chave:{cpf}, {clientes[cpf]}')
      elif menuCliente == '0':
        a=False
  elif (opcao=="3"):
    a=True
    while a:
      opcaoFantasia = menus.opcaoFantasia()
      if opcaoFantasia == '1':
        funcoes.cadastroFantasia(fantasias)
      elif opcaoFantasia == '2':
        funcoes.editFantasia(fantasias)
      elif opcaoFantasia == '3':
        comp = True
        while comp:
          numFan = input('Digite o numero da fantasia: ')
          if numFan not in fantasias:
            numFan = input('''
    Fantasia não encontrada!
        Tente novamente
 Obs.: Se não deseja continuar digite "Sair":  ''')
            if numFan.upper() == 'SAIR':
              comp = False
          else:
            print(f'Fantasia encontrada! {numFan}')
            print(f'O nome é: {fantasias[numFan][0]}')
            print(f'O tamanho é: {fantasias[numFan][1]}')
            print(f'A categoria é: {fantasias[numFan][2]}')
            print(f'O custo foi: {fantasias[numFan][3]}')
            print(f'Descrição: {fantasias[numFan][4]}')
      elif opcaoFantasia == '4':
        funcoes.apagarFantasia(fantasias)
      elif opcaoFantasia == '5':
        for numFan in fantasias:
          print(f'Chave: {numFan}, {fantasias[numFan]}')
      elif opcaoFantasia == '0':
        a=False
  elif opcao == '4':
    relat = True
    while relat:
      opcaoRelat = input('''

  = = = = = = = = = = = = = =
  M E N U  R E L A T O R I O
  = = = = = = = = = = = = = =

  1 - Receita Fantasia
  2 - Receita Mês
  3 - Receita anual
  0 - Sair
  Qual opção você deseja? ''')
      if opcaoRelat == '1':
        try:
          grafico_lucro=[]
          grafico_nome=[]
          for i in fantasias:
            grafico_nome.append(fantasias[i][0])
            grafico_lucro.append(fantasias[i][7])
          plt.subplot(131)
          plt.bar(grafico_nome,grafico_lucro)
          plt.xlabel('Nome da Fantasia')
          plt.ylabel('R. Fantasia')
          plt.suptitle('Receita Fantasias')
          plt.show()
        except:
          print('\nNão tem dados')
      elif opcaoRelat == '2':
        mesAno = input('''
  Digite o mês/ano que você deseja:
  Obs.: Lembrar que o formato é (mm-AAAA)''')

        if not re.match(r'\d{2}-\d{4}', mesAno):
          test = True
          while test:
            mesAno = input('Digite no formato valido mm/AAAA')
            if re.match(r'\d{2}-\d{4}', mesAno):
              test = False
        try:
          mesAnoLista = caixa.get(mesAno,'Dados não encontrados')
          grafico_mes=mesAnoLista[0]
          grafico_lucro_mesTotal=mesAnoLista[2]
          plt.subplot(131)
          plt.bar(grafico_mes, grafico_lucro_mesTotal)
          plt.xlabel('Mês do ano')
          plt.ylabel('R. do Mês')
          plt.suptitle('Receita por mês')
          plt.show()
        except:
          print('\nNão tem dados')
      elif opcaoRelat == '3':
        ano = input(f'''
          Digite o ano que você deseja:
          {list(caixa)}
          Obs.: Lembrar que o formato é (AAAA)''')

        if not re.match(r'\d{4}', ano):
          test = True
          while test:
            mesAno = input('Digite no formato valido AAAA')
            if re.match(r'\d{4}', ano):
              test = False
        grafico_ano = []

        for chaveCaixa in caixa:
          grafico_ano = caixa[chaveCaixa][1]
        if ano in grafico_ano:
          try:
            grafico_mes = []
            grafico_lucro_mesTotal = []
            for chaveCaixa in caixa:
              grafico_mes.append(caixa[chaveCaixa][0])
              grafico_lucro_mesTotal.append(caixa[chaveCaixa][2])

            plt.subplot(131)
            plt.bar(grafico_mes, grafico_lucro_mesTotal)
            plt.xlabel('Mês')
            plt.ylabel('Volume Financeiro')
            plt.suptitle('Lucro por mês/ANO')
            plt.show()
          except:
            print('\nNão tem dados')
        else:
          print('Não existe dados sobre o periodo!')
      elif opcaoRelat == '0':
        relat=False
      else:
        opcaoRelat = input('Digite uma opção valida! ')

  elif (opcao=='0'):
    menu=False

  else:
    print("Digite uma opção valida!")



