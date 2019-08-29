import os
def menuP():
  if os == 'nt':
    clear = 'cls'
  elif os == 'posix':
    clear = 'clear'
  if os == 'posix' or os == 'nt':
    os.system(clear)
  print('''
  = = = = = = = = = = = = = =
  M E N U   P R I N C I P A L
  = = = = = = = = = = = = = =

  1 - Menu Aluguel
  2 - Menu Cliente
  3 - Menu Fantasia
  4 - Menu Relatorio
  0 - Encerrar Programa''')
  opcao = input("Informe sua opção: ")
  return (opcao)
#####MENU DO EDITAR
def opcaoCliente():
  if os == 'nt':
    clear = 'cls'
  elif os == 'posix':
    clear = 'clear'
  if os == 'posix' or os == 'nt':
    os.system(clear)

  opcaoCliente = input('''
  EDITOR DE CLIENTES!!!!

  1- Cadastrar Cliente
  2- Editar Cliente
  3- Exibir Clientes
  4- Deletar Cliente
  5- Exibir todos os Clientes (Flavius)
  0- Sair

  Escolha uma das opções: ''')
  return opcaoCliente

def opcaoFantasia():
  if os == 'nt':
    clear = 'cls'
  elif os == 'posix':
    clear = 'clear'
  if os == 'posix' or os == 'nt':
    os.system(clear)
  opcaoFantasia = input('''
  EDITOR DE FANTASIAS!!!!

  1- Cadastrar fantasia
  2- Editar fantasia
  3- Exibir fantasia
  4- Deletar fantasia
  5- Exibir todas as fantasias(Flavius)
  0- Sair

  Escolha uma das opções: ''')
  return opcaoFantasia

def opcaoRelatorio():
  if os == 'nt':
    clear = 'cls'
  elif os == 'posix':
    clear = 'clear'
  if os == 'posix' or os == 'nt':
    os.system(clear)
  opcaoRelatorio = input('''
    RELATORIO!!!!

    1- Lucro-Fantasia
    2- Lucro-Total
    0- Sair

    Escolha uma das opções: ''')
  return opcaoRelatorio

def opcaoAlug():
  if os == 'nt':
    clear = 'cls'
  elif os == 'posix':
    clear = 'clear'
  if os == 'posix' or os == 'nt':
    os.system(clear)
  opcaoAlug = input('''
  1- Alugar Fantasia
  2- Devolver Fantasia
  3- Sair
  Escolha, por favor: ''')
  return opcaoAlug