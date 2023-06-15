menu = """ 
    Bem vindo!

    Aproveite as funcionalidades do nosso sistema.

    [1] - Saque
    [2] - Depósito
    [3] - Extrato
    [4] - Sair

"""

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor desejado: "))

        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_limite:
            print("Operação inválida. Você ultrapassou o limite de saque.")

        elif excedeu_saldo:
            print("Operação inválida. Você ultrapassou seu saldo atual.")

        elif excedeu_saques:
            print("Operação inválida. Você ultrapassou o limite de saques diário. Tente novamente amanhã.")

        elif valor > 0:
            print(f"Saque no valor de {valor:.2f} realizado com sucesso.")
            saldo -= valor
            extrato += f"Saque: R${valor:.2f} \n"
            numero_saques += 1

        else:
            print("Digite um valor válido.")


    elif opcao == 2:
        deposito = int(input("Informe o valor que deseja depositar: "))
        saldo_total = deposito + saldo

        print("Depósito realizado com sucesso!")
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f} \n"

    elif opcao == 3:
        print("=" * 50)
        print("Sua conta não foi movimentada" if not extrato else extrato)
        print(f"Saldo: R${saldo}")
        print("=" * 50)

    elif opcao == 4:
        print("Obrigado por utilizar nossos sistemas!")
        break

    else:
        print("Opção inválida")




