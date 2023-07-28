
menu = """
##### BEM VINDO!!####
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
LIMITE = 500
numero_saque = 0
LIMITE_SAQUE = 3
deposito= 0
saque=0
extrato=""

while True:
    opcao = input(menu)
    #DEPOSITO
    if opcao == "d":
        print('Você selecionou Depósito')
        deposito=float(input("Me Informe o valor do deposito:"))
        if deposito >0:
            saldo = saldo + deposito
            print(f"Você depositou R$ {deposito :.2f}, agora seu saldo é R$ {saldo:1.2f} ")
            extrato+= f"Depósito : R$ {deposito:.2f}\n"
        else: print("operação  falho, valor inválido.Tente novamente")

    #Saque
    elif opcao == "s":
        print('Você selecionou Saque')
        saque=float(input("Me Informe o valor do saque:"))
        numero_saque=numero_saque+1
        saldo= saldo-saque

        #limite de 500
        if saque >= 500:
            print("OPAAAAAA!!! saque limite é de R$ 500. Tente novamente!")
            saldo = saldo +saque
            numero_saque = numero_saque -1

        #saldo negativo
        elif saldo < 0:
            print("OPAAAAAA!!! Saldo esta negativo.Tente novamente")
            print(saldo)
            saldo = saldo + saque
            numero_saque = numero_saque - 1

        # MAIS DE 3 VEZES
        elif numero_saque >= LIMITE_SAQUE:
            print(f"OPAAAAAA!!! Exedeu o numero de saques que é 3 vezes e vc fez {numero_saque} vezes. Tente novamente!")
            saldo = saldo + saque

        else:
            print(f"Saque feito de  R${saque :1.2f}, Seu saldo esta para R$ {saldo:1.2f} ,vc tem ainda {3-numero_saque} ")
            extrato += f"Saque : R$ - {saque:.2f}\n"

    elif opcao == "e":
        print('Você selecionou Extrato')
        print("\n========== Extrato ==========")
        print(("não forão realizadas movimentações" if not extrato else extrato))
        print(f" TOTAL R$ {saldo:.2f}")
        print("=============================")
        #print(f' Seu saldo é:R${saldo:1.2f}')

    elif opcao == "q":
        print('Você selecionou para SAIR')
        break

    else:
        print("Opção inválida, por favor selecione navamente a operação desejada")
