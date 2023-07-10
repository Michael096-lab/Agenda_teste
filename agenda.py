agenda = []

def pede_nome():
     return(str(input("Nome: "))).strip().upper()

def pede_telefone(): 
     return(input("Telefone: ")).strip()

def pede_cidade():
     return(str(input("Cidade: "))).strip().upper()

def pede_estado():
     return(str(input("Estado: "))).strip().upper()

def pede_status():
     status = str(input("Status: P-> Pessoal ou C-> Comercial:")).strip().upper()
     while (status!='P')and(status!='p')and(status!='C')and(status!='c'):
          status = input(" Você deve entar com 'P,p' ou 'C,c': ").strip().upper()
     return(status)

def mostra_dados(nome, telefone, cidade, estado, status):
     print("Nome: %s - Telefone: %s - Cidade: %s - Estado: %s - Status: %s" % (nome, telefone, cidade, estado, status))

def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None


def novo():
     global agenda
     nome = pede_nome()
     telefone = pede_telefone()
     cidade = pede_cidade()
     estado = pede_estado()
     status = pede_status()
     agenda.append([nome, telefone, cidade, estado, status])
     print("\n\nCadastro realizado com sucesso! \n")

def apaga():
     global agenda
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
         del agenda[p]  
         print("\n\nCadastro deletado com sucesso! \n")       
     else:
         print("Nome não encontrado.")

def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0]
         telefone = agenda[p][1]
         cidade = agenda[p][2]
         estado = agenda[p][3]
         status = agenda[p][4]
         print("Encontrado:")
         mostra_dados(nome, telefone, cidade, estado, status)
         nome = pede_nome()
         telefone = pede_telefone()
         cidade = pede_cidade()
         estado = pede_estado()
         status = pede_status()
         agenda[p] = [nome, telefone, cidade, estado, status]
         print("\n\nCadastro alterado com sucesso! \n")
     else:
         print("Nome não encontrado.")

def lista():
     print("\n->-> Dados da Agenda <-<-\n\n","------"*15)
     if len(agenda) == 0:
             print("\nAgenda Vazia !")
     for e in agenda:
         mostra_dados(e[0], e[1], e[2], e[3], e[4])
     print("------"*15,"\n")

def mostra():
     p = pesquisa(pede_nome())
     if p != None:
          nome = agenda[p][0]
          telefone = agenda[p][1]
          cidade = agenda[p][2]
          estado = agenda[p][3]
          status = agenda[p][4]
          agenda[p] = [nome, telefone, cidade, estado, status]
          print("Nome: %s - Telefone: %s - Cidade: %s - Estado: %s - Status: %s" % (nome, telefone, cidade, estado, status))
     else:
         print("Nome não encontrado.")

def valida_opcao_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""\n-----------------------------------
#     Bem-vindo a sua agenda!     #
-----------------------------------   
|  1 - Cadastrar Pessoa na Agenda |
|  2 - Alterar dados da Pessoa    |
|  3 - Listar Agenda              |
|  4 - Procurar pessoa na Agenda  |
|  5 - Excluir Pessoa da Agenda   |
|  6 - Sair do sistema            |
-----------------------------------
""")
     return valida_opcao_inteiro("O que deseja fazer?:",1,6)

while True:
     opção = menu()
     if opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         lista()
     elif opção == 4:
         mostra()
     elif opção == 5:
         apaga()
     elif opção == 6:
          print('''\nEncerrando o Sistema!\n\nObrigado por utilizar um de nossos serviços.\n
                ''')
          break
     