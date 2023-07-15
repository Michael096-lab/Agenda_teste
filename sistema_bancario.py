menu = """ 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input(" Informe o valor do déposito: "))

        if valor > 0:
            saldo += valor
            extrato += f" Déposito: R$ {valor:.2f}\n"

        else:
            print(" Operação falhou: O valor informado é inválido. ")

    elif opcao == 2:
        valor = float(input(" Informe o valor do saque: "))

        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saques = numero_saque >= LIMITE_SAQUES

        if execedeu_saldo:
            print(" Operação falhou ! Você não tem saldo suficiente.")
        elif execedeu_limite:
            print(" Operação falhou ! O valor de saque excede o limite.")
        elif execedeu_saques:
            print(" Operação falhou ! Número maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print(" Operação falhou: O valor informado é inválido. ")

    elif opcao == 3:
        print("\n************EXTRATO************")
        print(" Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n*******************************")


    elif opcao == 4:
        break

    else:
        print(" Operação falhou, por favor selecione novamente a operação desejada. ")




print(saldo)
print(limite)
print(extrato)
print(numero_saque )
print(LIMITE_SAQUES)