# Variáveis globais
usuarios = []
contas = []

# Função de criação de usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Remover pontuações do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verificar se o usuário já existe
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado.")
            return

    # Criar o usuário
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

# Função de criação de conta corrente
def criar_conta(cpf_usuario):
    agencia = "0001"
    
    # Filtrar o usuário pelo CPF
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf_usuario), None)
    
    if not usuario:
        print("Usuário não encontrado. Verifique o CPF.")
        return

    # Número da conta será sequencial
    numero_conta = len(contas) + 1
    
    # Criar a conta
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(nova_conta)
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}.")

# Função para sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

# Função para depositar
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

# Função para exibir extrato
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função principal (menu)
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Usuário
    [n] Cadastrar Conta
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
            numero_saques += 1

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "c":
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF (apenas números): ")
            endereco = input("Informe o endereço (logradouro - número - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "n":
            cpf_usuario = input("Informe o CPF do usuário para criar uma conta: ")
            criar_conta(cpf_usuario)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executar o sistema
main()
