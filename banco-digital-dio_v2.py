menu = """
#### OPERAÇÕES DISPONÍVEIS ####

########################        
[d] Depositar
[s] Sacar
[e] Extrato
[v] Ver Dados do Usuário
[a] Alternar Conta Bancária
[c] Cadastrar Usuário
[q] Sair
########################
"""

usuarios = []
conta_bancaria_atual = None  # Variável global para armazenar a conta bancária atualmente selecionada

def cadastra_usuario():
    usuario = {}
    usuario["nome"] = input("Insira o nome: ")
    usuario["idade"] = int(input("Insira a idade: "))
    usuario["data_de_nascimento"] = input("Insira a data de nascimento (DD/MM/AAAA): ")
    usuario["conta_bancaria"] = input("Insira a conta bancária (xxxxx-xx): ")
    usuario["saldo"] = 0
    usuario["extrato"] = ""
    usuario["numero_saques"] = 0
    usuario["numero_depositos"] = 0
    usuarios.append(usuario)
    exibir_menu()

def seleciona_usuario(conta_bancaria):
    for usuario in usuarios:
        if usuario["conta_bancaria"] == conta_bancaria:
            return usuario
    return None

def deposita(usuario):
    global conta_bancaria_atual
    print("----------")
    print("Depósito".center(20, "#"))
    valor = float(input("Insira o valor do depósito (limite máximo 500): \n"))
    if valor >= 0:
        if valor <= 500:
            usuario["saldo"] += valor
            usuario["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            usuario["numero_depositos"] += 1
            print("Depósito realizado com sucesso!\n")
        else:
            print("Limite máximo de depósito por vez é de R$ 500. Tente novamente.\n")
    else:
        print("Por favor, insira um valor positivo\n")

def saca(usuario):
    global conta_bancaria_atual
    LIMITE_SAQUES = 3
    print("----------")
    print("Saque".center(20, "#"))
    valor = float(input("Insira o valor do saque: \n"))
    if usuario["numero_saques"] >= LIMITE_SAQUES:
        print("Você ultrapassou o limite diário de saques!\n")
    elif valor > usuario["saldo"]:
        print("Operação negada!! Saldo insuficiente para realizar o saque\n")
    else:
        usuario["saldo"] -= valor
        usuario["extrato"] += f"Saque: R$ {valor:.2f}\n"
        usuario["numero_saques"] += 1
        print("Saque realizado com sucesso!\n")

def extratoS(usuario):
    global conta_bancaria_atual
    print("----------")
    print("EXTRATO".center(20, "#"))
    print("Não foram realizadas movimentações." if not usuario["extrato"] else usuario["extrato"])
    print(f"\nSaldo: R$ {usuario['saldo']:.2f}")
    print("----------")

def exibir_dados_usuario(conta_bancaria): # exibe os dados por usuário
    global conta_bancaria_atual
    usuario = seleciona_usuario(conta_bancaria) # recebe a função seleciona_usuario e recebe como parâmetro a chave conta_bancaria
    if usuario:
        print("----------")
        print("DADOS DO USUÁRIO".center(20, "#"))
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Data de Nascimento: {usuario['data_de_nascimento']}")
        print(f"Conta Bancária: {usuario['conta_bancaria']}")
        print(f"Saldo: R$ {usuario['saldo']:.2f}")
        print("----------")
    else:
        print("Conta bancária não encontrada.\n")

def alternar_conta_bancaria():
    global conta_bancaria_atual # alterna entre os usuários a partir da conta bancária
    conta_bancaria_atual = input("Insira a conta bancária (xxxxx-xx): ")
    print(f"Operando com a conta bancária {conta_bancaria_atual}\n")

def verificar_usuarios():
    if not usuarios: # Verifica se há usuários cadastrados, caso não, pede para cadastrá-lo
        print("Nenhum usuário cadastrado. Por favor, cadastre pelo menos um usuário.")
        return False
    return True

def exibir_menu():
    global conta_bancaria_atual
    while True:
        if not verificar_usuarios():
            cadastra_usuario()

        if not conta_bancaria_atual:
            alternar_conta_bancaria()

        opcao = input(menu).lower()

        if opcao == "c":
            cadastra_usuario()

        elif opcao in ["d", "s", "e", "v"]:
            if not conta_bancaria_atual:
                print("Nenhuma conta bancária selecionada. Utilize a opção 'a' para alternar a conta bancária.\n")
                continue

            usuario = seleciona_usuario(conta_bancaria_atual)
            if opcao == "d":
                if usuario:
                    deposita(usuario)
                else:
                    print("Conta bancária não encontrada.\n")
            elif opcao == "s":
                if usuario:
                    saca(usuario)
                else:
                    print("Conta bancária não encontrada.\n")
            elif opcao == "e":
                if usuario:
                    extratoS(usuario)
                else:
                    print("Conta bancária não encontrada.\n")
            elif opcao == "v":
                exibir_dados_usuario(conta_bancaria_atual)

        elif opcao == "a":
            alternar_conta_bancaria()

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

exibir_menu()
