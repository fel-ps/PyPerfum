import os
import pickle
from re import match, sub
from datetime import datetime

# MENUS

def menu_principal():
    os.system('clear || cls')
    print('######################')
    print('###### PyPerfum ######')
    print('######################\n')
    print('#1 - Menu de Produtos')
    print('#2 - Menu de Clientes')
    print('#3 - Menu de Vendas')
    print('#4 - Sobre')
    print('#0 - Sair')
    acao = input("Digite o que deseja fazer: ")
    return acao

def menu_produto():
    os.system('clear || cls')
    print('########################')
    print('### Menu de Produtos ###')
    print('########################\n')
    print("#1 - Cadastrar Produto")
    print("#2 - Listar Produtos")
    print("#3 - Deletar Produto")
    print("#4 - Atualizar Produto")
    print("#0 - Sair")
    acao = input("Digite o que deseja fazer: ")
    return acao

def menu_cliente():
    os.system('clear || cls')
    print('########################')
    print('### Menu de Clientes ###')
    print('########################\n')
    print("#1 - Cadastrar Cliente")
    print("#2 - Listar Clientes")
    print("#3 - Deletar Cliente")
    print("#4 - Atualizar Cliente")
    print("#5 - Buscar Cliente")
    print("#0 - Sair")
    acao = input("Digite o que deseja fazer: ")
    return acao

def menu_venda():
    os.system('clear || cls')
    print('######################')
    print('### Menu de Vendas ###')
    print('######################\n')
    print("#1 - Cadastrar Venda")
    print("#2 - Listar Vendas")
    print("#0 - Sair")
    acao = input("Digite o que deseja fazer: ")
    return acao

def sobre():
   print('\nPrograma produzido pelo Discente: Felipe Augusto Araújo da Cunha')
   print('Doscente: Flavius Gorgônio')
   print()
   print('''Objetivo: Um sistema de gestão para uma loja de perfumes, este sistema está incluso no computador do caixa da loja,
em que apenas funcionários possui o acesso, o cliente não 
está em contato direto com o programa.''')
   print()
   print('''Descubra a PyPerfum: Elegância em cada fragrância! 
Encontre perfumes importados de alta qualidade para expressar sua personalidade. 
Visite-nos hoje mesmo! #PyPerfum #FragrânciasExclusivas''')
   input("\nTecle ENTER para continuar")

# PROGRAMAS 

#PRODUTOS
def cadastrar_produto():
    print()
    cadastramento = 0
    while cadastramento == 0:
      np = str(input('Digite o código do novo produto: '))
      if validarCódigo(np):
        if np in produtoss:
          cadastramento = 4
          print('\nProduto já existente!')
          input("Tecle ENTER para continuar")
        else:
          cadastramento = 1
          produtoss[np] = []
          while cadastramento == 1:
            nomeproduto = str(input('Digite o nome do produto: '))
            produtoss[np] += [nomeproduto]
            cadastramento = 2
            while cadastramento == 2:
              preco = input('Digite o valor desse produto($): ')
              if valida_preco(preco):
                preco = float(preco)
                produtoss[np] += [preco]
                cadastramento = 3
                while cadastramento == 3:
                  ml = input('Digite a quantidade de (ml) que esse produto possui: ')
                  if validarQuantidadePerfume(ml):
                    ml = str(ml)
                    produtoss[np] += [ml]
                    cadastramento = 4
                    print('\nNovo produto adcionado!')
                    input("Tecle ENTER para continuar")
                  else:
                    print('\nDigite uma quantidade de (ml) válida!')
              else:
                print('\nDigite um preço válido!')
      else:
        print('\nDigite um código válido!')

def listar_produtos():
    print()
    if len(produtoss) == 0:
      print('\nNenhum produto cadastrado!')
      input("Tecle ENTER para continuar")
    else:
      for x in produtoss:
        print('%s(%sml): %.2f$' % (produtoss[x][0], produtoss[x][2], produtoss[x][1]))
        print("------------------------------")
      input("Tecle ENTER para continuar")

def deletar_produto():
    deletar = str(input('\nDigite o código do produto o qual deseja deletar: '))
    if deletar in produtoss:
      deletarmesmo = str(input('Deseja deletar %s?(S/N): ' % (produtoss[deletar][0])))
      if deletarmesmo.upper() == 'S':
        del produtoss[deletar]
        print('\nProduto deletado!')
        input("Tecle ENTER para continuar")
      elif deletarmesmo.upper() == 'N':
        print('\nCancelado!')
        input("Tecle ENTER para continuar")
      else:
        print('\nResposta inválida!')
        input("Tecle ENTER para continuar")
    else:
      print('\nProduto inexistente!')
      input("Tecle ENTER para continuar")

def atualizar_produto():
    att = str(input('\nDigite o código do produto o qual deseja atualizar: '))
    if att in produtoss:
      atualizacao = 0
      print('\nNome antigo:', produtoss[att][0])
      nomeproduto = str(input('Digite o novo nome do produto: '))
      produtoss[att][0] = nomeproduto
      print('Valor antigo:', produtoss[att][1])
      while atualizacao == 0:
        preco = input('Digite o novo valor desse produto($): ')
        if valida_preco(preco):
          preco = float(preco)
          produtoss[att][1] = preco
          atualizacao = 1
          print('Quantidade(ml) antiga:', produtoss[att][2])
          while atualizacao == 1:
            ml = str(input('Digite a quantidade de (ml) que esse produto possui: '))
            if validarQuantidadePerfume(ml):
              produtoss[att][2] = ml
              atualizacao = 2
              print('\nProduto atualizado!')
              input("Tecle ENTER para continuar")
            else:
              print('\nDigite uma quantidade de (ml) válida!')
        else:
          print('\nDigite um preço válido!')
    else:
      print('\nProduto inexistente!')
      input("Tecle ENTER para continuar")

#CLIENTES
def cadastrar_cliente():
    cadastramento = 0
    while cadastramento == 0:
      cpf = input('\nDigite o CPF: ').replace('.', '').replace('-', '')
      if validaCPF(cpf):
        if cpf not in clientess:
          cadastramento = 1
          while cadastramento == 1:
            nome = input('Digite nome completo: ')
            if validarNomeCompleto(nome):
              cadastramento = 2
              while cadastramento == 2:
                email = input('Digite o email: ')
                if validarEmail(email):
                  cadastramento = 3
                  while cadastramento == 3:
                    telefone = str(input('Digite o telefone: '))
                    if validarTelefone(telefone):
                      telefone = telefone.replace('.', '').replace('-', '').replace('(', '').replace(')', '')
                      clientess[cpf] = [nome, email, telefone]
                      cadastramento = 4
                      print('\nNovo cliente cadastrado!')
                      input("Tecle ENTER para continuar")
                    else:
                      print('\nDigite um número de telefone válido!')
                else:
                  print('\nDigite um email válido!')
            else:
              print('\nDigite um nome válido!')
        else:
          cadastramento = 4
          print('\nEste CPF já foi cadastrado!')
          input("Tecle ENTER para continuar")
      else:
        print('\nDigite um CPF válido!')

def listar_clientes():
    if len(clientess) == 0:
      print('\nNão há cadastros.')
      input("Tecle ENTER para continuar")
    else:
      print()
      for cl in clientess:
        print('Nome: %s' % (clientess[cl][0]))
        print('Email: %s' % (clientess[cl][1]))
        print('Telefone: %s' % (clientess[cl][2]))
        print('CPF: %s' % cl)
        print("--------------------")
      input("Tecle ENTER para continuar")

def deletar_cliente():
    deletar = str(input('\nInforme o CPF do cliente o qual deseja deletar: ')).replace('.', '').replace('-', '')
    if deletar in clientess:
      confirmacao = input('Deseja deletar %s?(S/N): ' % (clientess[deletar][0])).upper()
      if confirmacao == 'S':
        del clientess[deletar]
        print('\nCLIENTE REMOVIDO!')
        input("Tecle ENTER para continuar")
      else:
        print('\nCancelado!')
        input("Tecle ENTER para continuar")
    else:
      print('CPF inválido ou inexistente!')
      input("Tecle ENTER para continuar")

def atualizar_cliente():
    cpf = str(input('Digite o CPF do cliente o qual deseja atualizar as informações: ')).replace('.', '').replace('-', '')
    if cpf in clientess:
      att = str(input('Deseja atualizar as informações de(%s)?(S/N): ' % (clientess[cpf][0]))).upper()
      if att == 'S':
        atualizacao = 0
        print('\nNome Antigo:', clientess[cpf][0])
        while atualizacao == 0:
          clientess[cpf][0] = str(input('Digite o nome completo: '))
          if validarNomeCompleto(clientess[cpf][0]):
            atualizacao = 1
            print('\nEmail antigo:', clientess[cpf][1])
            while atualizacao == 1:
              clientess[cpf][1] = str(input('Digite o novo email: '))
              if validarEmail(clientess[cpf][1]):
                atualizacao = 2
                print('\nTelefone antigo:', clientess[cpf][2])
                while atualizacao == 2:
                  clientess[cpf][2] = str(input('Digite o novo telefone: '))
                  clientess[cpf][2] = clientess[cpf][2].replace('.', '').replace('-', '').replace('(', '').replace(')', '')
                  if validarTelefone(clientess[cpf][2]):
                    atualizacao = 3
                    print('\nInformações atualizadas!')
                    input("Tecle ENTER para continuar")
                  else:
                    print('\nDigite um número de telefone válido!')
              else:
                print('\nDigite um email válido!')
          else:
            print('\nDigite um nome válido!')
      else:
        print('\nCancelado!')
        input("Tecle ENTER para continuar")
    else:
      print('\nCPF inválido ou inexistente!')
      input("Tecle ENTER para continuar")

def buscar_cliente():
    busc = str(input('Digite o primeiro nome do cliente: '))
    for chave in clientess:
      if busc in clientess[chave][0]:
        print('\nNome: %s' % (clientess[chave][0]))
        print('Email: %s' % (clientess[chave][1]))
        print('Telefone: %s' % (clientess[chave][2]))
        print('CPF: %s' % chave)
        print("--------------------")
    input("Tecle ENTER para continuar")

#VENDAS
def cadastrar_venda():
    dataatual = str(obter_data_atual()).replace('/', '')
    if dataatual not in vendass:
      vendass[dataatual] = []
    dataehora = obter_data_hora_atual()
    produto = str(input('\nDigite o código do produto: '))
    if produto in produtoss:
      confirm = input('Produto(%s), está correto?(S/N): ' % produtoss[produto][0]).upper()
      if confirm == 'S':
        cadastramento = 0
        while cadastramento == 0:
          quantidade = input('Digite a quantidade vendida: ')
          if valida_quantidade(quantidade):
            quantidade = int(quantidade)
            cadastramento = 1
            while cadastramento == 1:
              cpf = input('Digite o CPF do cliente: ').replace('.', '').replace('-', '')
              if cpf in clientess:
                preco = quantidade * produtoss[produto][1]
                vendac = {
                'produto': produtoss[produto][0],
                'quantidade': quantidade,
                'preco': preco,
                'cliente': clientess[cpf][0],
                'dh': dataehora
                }
                vendass[dataatual] += [vendac]
                cadastramento = 2
                print('\nVenda cadastrada com sucesso!')
                input("Tecle ENTER para continuar")
              else:
                print('\nDigito inválido ou cliente ainda não cadastrado no sistema!')
                input("Tecle ENTER para continuar")
          else:
            print('\nDigite uma quantidade válida!')
      else:
        print('\nCancelado!')
        input("Tecle ENTER para continuar")
    else:
      print('\nProduto inexistente ou inválido!')
      input("Tecle ENTER para continuar")

def listar_vendas():
    if len(vendass) == 0:
      print('\nNão há vendas!')
      input("Tecle ENTER para continuar")
    else:
      datainformada = str(input('Informe a data das vendas que deseja ver(Ex: dia/mês/ano): ')).replace('/', '')
      if datainformada in vendass:
        print()
        for x in vendass[datainformada]:
          print('Produto: %s' % (x['produto']))
          print('Quantidade: %d' % (x['quantidade']))
          print('Preço Final: %.2f$' % (x['preco']))
          print('Cliente: %s' % (x['cliente']))
          print('Data e Hora: %s' % (x['dh']))
          print("---------------------------------------")
        input("Tecle ENTER para continuar")
      else:
        print('Data inválida ou vendas inexistentes nesta data!')
        input("Tecle ENTER para continuar")

#OUTROS
def parar_execucao():
    global continuar
    continuar = False

def obter_data_hora_atual():
    agora = datetime.now()
    agora = agora.strftime("%d/%m/%Y | %H:%M:%S")
    return agora

def obter_data_atual():
    agora = datetime.now()
    data_atual = agora.date()
    data_atual = data_atual.strftime("%d/%m/%Y")
    return data_atual

def salvar():
    arq = open("arquivo.dat", "wb")
    ##unindo todos os dicionarios em um só, como num banco de dados
    dados = {1: clientess, 2: produtoss, 3: vendass}
    pickle.dump(dados, arq)
    arq.close()

def recuperar():
  try:
    arq = open("arquivo.dat", "rb")
    dados = pickle.load(arq)
    clientess = dados[1]
    produtoss = dados[2]
    vendass = dados[3]
    arq.close()
    return clientess, produtoss, vendass
  except:
    arq = open("arquivo.dat", "wb")
    arq.close()
    return {},{},{}
  
# VALIDAÇÕES

# VALIDAR CPF (FLAVIUS GORGÔNIO)
def validaCPF(cpf):
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0
    if tam != 11:
        return False
    for i in range(11):
        if (cpf[i] < '0') or (cpf[i] > '9'):
            return False
    for i in range(9):
        soma += (int(cpf[i]) * (10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += (int(cpf[i]) * (11 - i))
    d2 = 11 - (soma%11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False
    return True

# VALIDAR NOME(Matheus Diniz e GPT)
def validarNomeCompleto(nome):
    if len(nome) == 0:
        return False
    partes_nome = nome.split()
    if len(partes_nome) < 2:
        return False
    for parte in partes_nome:
        if not parte.isalpha():
            return False
    return True

# VALIDAR EMAIL(GPT)
def validarEmail(email):
    # Verifica se o email corresponde ao padrão de endereço de email válido
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not match(padrao, email):
        return False
    # Verifica se o email tem pelo menos um caractere antes do @ e pelo menos um caractere depois do @
    partes = email.split('@')
    if len(partes) != 2 or len(partes[0]) == 0 or len(partes[1]) == 0:
        return False
    # Verifica se o domínio do email é válido (exemplo: gmail.com, yahoo.com)
    dominio = partes[1]
    dominio_valido = match(r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', dominio)
    if not dominio_valido:
        return False
    return True

# VALIDAR TELEFONE(GPT)
def validarTelefone(telefone):
    # Remove caracteres especiais do número de telefone
    telefone = sub(r'\D', '', telefone)
    # Verifica se o número de telefone tem 10 ou 11 dígitos
    if len(telefone) != 10 and len(telefone) != 11:
        return False
    # Verifica se o número de telefone começa com 9 (para números de celular) ou 2 a 9 (para números fixos)
    if telefone[2] != '9' and not (2 <= int(telefone[2]) <= 9):
        return False
    return True

# VALIDAR PREÇO (MARIA ELOISA)
def valida_preco(preco):
    try:
        preco = float(preco)
        if preco >= 0:
            return True
        else:
            return False
    except:
        return False

# VALIDAR ML(GPT)
def validarQuantidadePerfume(ml):
    try:
        ml = float(ml)
        if ml <= 0:
            return False
    except ValueError:
        return False
    return True

# VALIDAR QUANTIDADE (GPT)
def valida_quantidade(quantidade):
    try:
        quantidade = int(quantidade)
        if quantidade > 0:
            return True
        else:
            return False
    except:
        return False

# VALIDAR CÓDIGO (EU)
def validarCódigo(np):
    try:
        np = int(np)
        if np <= 0:
            return False
    except:
        return False
    return True

# Programa Principal
produtoss = {}
clientess = {}
vendass = {}

clientess, produtoss, vendass = recuperar()

start = True
while start:
  continuar = True
  sy = menu_principal()
  if sy == "1":
    while continuar:
      prod = menu_produto()
      if prod == '1':
        cadastrar_produto()
      elif prod == '2':
        listar_produtos()
      elif prod == '3':
        deletar_produto()
      elif prod == '4':
        atualizar_produto()
      elif prod == '0':
        parar_execucao()
      else:
        print('\nAção inválida!')
        input("Tecle ENTER para continuar")
  elif sy == "2":
    while continuar:
      clie = menu_cliente()
      if clie == '1':
        cadastrar_cliente()
      elif clie == '2':
        listar_clientes()
      elif clie == '3':
        deletar_cliente()
      elif clie == '4':
        atualizar_cliente()
      elif clie == '5':
        buscar_cliente()
      elif clie == '0':
        parar_execucao()
      else:
        print('\nAção inválida!')
        input("Tecle ENTER para continuar")
  elif sy == "3":
    while continuar:
      vend = menu_venda()
      if vend == '1':
        cadastrar_venda()
      elif vend == '2':
        listar_vendas()
      elif vend == '0':
        parar_execucao()
      else:
        print('\nAção inválida!')
        input("Tecle ENTER para continuar")
  elif sy == "4":
     sobre()
  elif sy == "0":
    start = False
  else:
    print('\nAção inválida!')
    input("Tecle ENTER para continuar")

salvar()

print('\nFIM DO PROGRAMA!')
