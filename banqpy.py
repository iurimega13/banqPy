'''
Criar um sistema bancário com as operações: sacar, depositar
e visualizar extrato.
'''

usuario_saldo = 0
quantidade_saques = 0
extrato = []
while True:
    print ('1 - Sacar')
    print ('2 - Depositar')
    print ('3 - Visualizar extrato')
    print ('4 - Sair')
    
    input_usuario = int(input('Escolha uma opção: '))
    # Sacar
    if input_usuario == 1:
        if quantidade_saques < 3:
            if usuario_saldo == 0:
                print('Não será possível sacar, pois seu saldo é de R$ 0,00')
            else:
                valor_saque = float(input('Digite o valor do saque: '))
                if valor_saque > 500:
                    print('Valor máximo por saque é de R$ 500,00')
                else:
                    if valor_saque > usuario_saldo:
                        print(f'Saldo insuficiente, seu saldo é de R$ {usuario_saldo:.2f}')
                    else:
                        print('Saque realizado com sucesso')
                        usuario_saldo -= valor_saque
                        extrato.append(f'Saque de R$ {valor_saque:.2f} realizado com sucesso')
                        quantidade_saques += 1
        else:
            print('Limite de saques diários atingido')
    # Depositar
    elif input_usuario == 2:
        input_usuario = float(input('Digite o valor do depósito: '))
        if input_usuario <= 0:
            print('Valor inválido')
        else:
            print('Depósito realizado com sucesso')
            usuario_saldo += input_usuario
            extrato.append(f'Depósito de R$ {input_usuario:.2f} realizado com sucesso')
    # Extrato
    elif input_usuario == 3:
        print('===================EXTRATO=====================')
        for i in extrato:
            print(i)
        print('===================EXTRATO=====================')
        print(f'Seu saldo atual: R$ {usuario_saldo:.2f}')
    # Sair
    elif input_usuario == 4:
        break
    # Opção inválida
    else:
        print('Opção inválida')
        continue