
import textwrap
print("DESAFIO 2".center(50,"#"))

# ele quer só possicional
def deposito(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
def saque(*,saldo,valor,extrato,numero_saques,LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def extratos(saldo,/,*,extrato):

    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"\n{extrato}\n")

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo,extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf=input("informe o cpf do usuário")
    usuario=filtrar_usuario(cpf,usuarios)

    if usuario:
       print("\n=== Conta criada com sucesso! ===")
       return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))




menu = """
MENU
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar conta
[nu] novo usuário
[q] Sair

=> """
AGENCIA="0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios=[] # lista criada
contas=[]

while True:

    opcao = input(menu)
#depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo,extrato =deposito(saldo,valor, extrato)
#saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo,extrato = saque(
            saldo=saldo,valor=valor,
            extrato=extrato,
            numero_saques=numero_saques
            ,LIMITE_SAQUES=LIMITE_SAQUES,
        )

#Extrato
    elif opcao == "e":
        extratos(saldo, extrato=extrato)
# nova conta
    elif opcao == "nu":
        print("vc selecionou em adicionar nova conta")
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas)+1
        conta= criar_conta(AGENCIA,numero_conta,usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")