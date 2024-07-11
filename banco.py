class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Limite de saques diários atingido.")
            return
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de saque inválido ou saldo insuficiente!")

    def verificar_extrato(self):
        print(f"Extrato de {self.nome}:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

    def resetar_saques_diarios(self):
        self.saques_diarios = 0
        print("Saques diários resetados.")


class Banco:
    def __init__(self):
        self.clientes = {}

    def adicionar_cliente(self, nome):
        if nome not in self.clientes:
            self.clientes[nome] = Cliente(nome)
            print(f"Cliente {nome} adicionado com sucesso.")
        else:
            print("Cliente já existente.")

    def encontrar_cliente(self, nome):
        if nome in self.clientes:
            return self.clientes[nome]
        else:
            print("Cliente não encontrado.")
            return None

# Exemplo de uso
banco = Banco()
banco.adicionar_cliente("Alice")

cliente = banco.encontrar_cliente("Alice")
if cliente:
    cliente.depositar(1000)
    cliente.sacar(100)
    cliente.sacar(200)
    cliente.sacar(50)
    cliente.sacar(10)  # Este saque deve falhar porque o limite de 3 saques foi atingido
    cliente.verificar_extrato()

    cliente.resetar_saques_diarios()
    cliente.sacar(10)  # Agora o saque deve ser permitido
    cliente.verificar_extrato()
