menu = """

            #### OPERAÇÕES DISPONíVEIS ####

  ########################        
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
  ########################   

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        print("----------")
        print("Depósito".center(20,"#"))
        valor = float(input("Insira o valor do depósito: \n"))
        if valor >= 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            numero_depositos += 1
        else:
            print("Por favor, insira um valor positivo \n")
            continue
   
    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Você ultrapassou o limite diário de saques!\n")
            continue
        else:
            print("----------")
            print("Saque".center(20,"#"))
            valor = float(input("Insira o valor do saque: \n"))

            if valor > saldo: 
                print("Operação negada!! Saldo insuficiente para realizar o saque \n")
                continue
            else: 
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

    elif opcao == "e":
        print("----------")
        print("EXTRATO".center(20,"#"))
        print("Não foram realizadas movimentaçãoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------")
    
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

