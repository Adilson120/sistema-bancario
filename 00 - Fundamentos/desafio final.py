import getpass

# Definição do menu principal
menu_principal = """
[1] Criar nova conta
[2] Acessar conta
[3] Sair
=> """

menu_conta = """
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> """

# Banco de dados simples para armazenar contas
contas = []

# Limite de saques por conta
LIMITE_SAQUES = 3

# Função para criar uma nova conta
def criar_conta():
    nome = input("Informe o seu nome: ")
    senha = getpass.getpass("Informe uma senha para a conta: ")
    saldo = 0
    extrato = ""
    numero_saques = 0
    conta = {
        "nome": nome,
        "senha": senha,
        "saldo": saldo,
        "extrato": extrato,
        "numero_saques": numero_saques,
        "limite": 500,
        "limite_saques": LIMITE_SAQUES
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Bem-vindo(a), {nome}.")

# Função para autenticar o acesso à conta
def autenticar():
    nome = input("Informe seu nome: ")
    senha = getpass.getpass("Informe sua senha: ")
    
    for conta in contas:
        if conta['nome'] == nome and conta['senha'] == senha:
            print(f"Bem-vindo(a), {nome}!")
            return conta
    print("Nome ou senha incorretos. Tente novamente.")
    return None

# Função de depósito
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função de saque
def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta['saldo']
    excedeu_limite = valor > conta['limite']
    excedeu_saques = conta['numero_saques'] >= conta['limite_saques']

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
        conta['numero_saques'] += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função de transferência
def transferir(conta_origem):
    nome_destino = input("Informe o nome da conta de destino: ")
    valor = float(input("Informe o valor a ser transferido: "))
    
    conta_destino = None
    for conta in contas:
        if conta['nome'] == nome_destino:
            conta_destino = conta
            break
    
    if conta_destino is None:
        print("Conta de destino não encontrada.")
        return

    if valor > conta_origem['saldo']:
        print("Operação falhou! Saldo insuficiente.")
        return
    
    conta_origem['saldo'] -= valor
    conta_origem['extrato'] += f"Transferência para {nome_destino}: R$ {valor:.2f}\n"
    conta_destino['saldo'] += valor
    conta_destino['extrato'] += f"Transferência recebida de {conta_origem['nome']}: R$ {valor:.2f}\n"
    print(f"Transferência de R$ {valor:.2f} para {nome_destino} realizada com sucesso!")

# Função para exibir o extrato
def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Função principal que gerencia o menu
def menu_conta_logada(conta):
    while True:
        opcao = input(menu_conta)
        if opcao == "d":
            depositar(conta)
        elif opcao == "s":
            sacar(conta)
        elif opcao == "t":
            transferir(conta)
        elif opcao == "e":
            exibir_extrato(conta)
        elif opcao == "q":
            print(f"Saindo da conta de {conta['nome']}...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função principal que gerencia o sistema bancário
def sistema_bancario():
    while True:
        opcao = input(menu_principal)
        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            conta = autenticar()
            if conta:
                menu_conta_logada(conta)
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema bancário
sistema_bancario()
