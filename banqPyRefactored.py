'''
Criar um sistema bancário com as operações: sacar, depositar
e visualizar extrato.
'''

import textwrap


def menu():
    # Define as opções do menu
    menu_options = {
        'd': 'Depositar',
        's': 'Sacar',
        'e': 'Extrato',
        'nc': 'Nova conta',
        'lc': 'Listar contas',
        'nu': 'Novo usuário',
        'lu': 'Listar usuários',
        'q': 'Sair'
    }

    # Constrói a string do menu
    menu = (
        "\n=============== MENU ================\n"
        + "\n".join(f"[{key}]    {value}" for key, value in menu_options.items())
        + "\n=> "
    )

    return input(menu).strip()


def depositar(contas):
    numero_conta = input("Informe o número da conta: ")

    # Verifica se a conta existe
    if numero_conta in contas:
        valor = float(input("Informe o valor do depósito: "))
        conta = contas[numero_conta]
        saldo_anterior = conta['saldo']

        # Atualiza o saldo da conta e adiciona o depósito ao extrato
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito:\tR$ {valor:.2f}\n"

        print("\n=== Depósito realizado com sucesso! ===")
        print(f"Saldo anterior:\tR$ {saldo_anterior:.2f}")
        print(f"Novo saldo:\tR$ {conta['saldo']:.2f}")
    else:
        print("\n@@@ Conta não encontrada! Verifique o número da conta informado. @@@")


def sacar(contas):
    numero_conta = input("Informe o número da conta: ")

    # Verifica se a conta existe
    if numero_conta in contas:
        valor = float(input("Informe o valor do saque: "))
        conta = contas[numero_conta]

        saldo = conta['saldo']
        extrato = conta['extrato']
        limite = conta['limite']
        numero_saques = conta['numero_saques']
        limite_saques = conta['limite_saques']

        # Verifica as condições de saque
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        # Atualiza os dados da conta
        conta['saldo'] = saldo
        conta['extrato'] = extrato
        conta['numero_saques'] = numero_saques
    else:
        print("\n@@@ Conta não encontrada! @@@")
        

def exibir_extrato(contas):
    numero_conta = input("Informe o número da conta: ")

    # Verifica se a conta existe
    if numero_conta in contas:
        conta = contas[numero_conta]

        saldo = conta['saldo']
        extrato = conta['extrato']

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==========================================")
    else:
        print("\n@@@ Conta não encontrada! @@@")
        

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    
    # Verifica se já existe um usuário com o CPF informado
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")


def listar_usuarios(usuarios):
    if not usuarios:
        print("\n@@@ Não existem usuários cadastrados! @@@")
        return
    else:
        print("\n================ USUÁRIOS ================")
        for usuario in usuarios:
            linha = f"""
                Nome:\t\t{usuario['nome']}
                Data Nasc.:\t{usuario['data_nascimento']}
                CPF:\t\t{usuario['cpf']}
                Endereço:\t{usuario['endereco']}
            """
            print(textwrap.dedent(linha))


def filtrar_usuario(cpf, usuarios):
    # Filtra os usuários pelo CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    # Verifica se o usuário existe
    if usuario:
        numero_conta = str(len(contas) + 1)
        saldo = 0
        extrato = ""
        limite = 5000
        numero_saques = 0
        limite_saques = 5

        conta = {
            'agencia': "0001",
            'numero_conta': numero_conta,
            'usuario': usuario,
            'saldo': saldo,
            'extrato': extrato,
            'limite': limite,
            'numero_saques': numero_saques,
            'limite_saques': limite_saques
        }

        # Armazena a conta no dicionário contas usando o número da conta como chave
        contas[numero_conta] = conta
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    if not contas:
        print("\n@@@ Não existem contas cadastradas! @@@")
        return
    else:
        print("\n================ CONTAS ================")
        for conta in contas.values():
            linha = f"""
                Agência:\t\t{conta['agencia']}
                Número Conta:\t{conta['numero_conta']}
                CPF:\t\t{conta['usuario']['cpf']}
                Nome:\t\t{conta['usuario']['nome']}
                Saldo:\t\tR$ {conta['saldo']:.2f}
            """
            print(textwrap.dedent(linha))


def main():
    # Dicionário para armazenar as contas bancárias
    contas = {}

    # Lista para armazenar os usuários
    usuarios = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(contas)
        elif opcao == 's':
            sacar(contas)
        elif opcao == 'e':
            exibir_extrato(contas)
        elif opcao == 'nc':
            criar_conta(contas, usuarios)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'lu':
            listar_usuarios(usuarios)
        elif opcao == 'q':
            print("\n=== Sessão encerrada. Até mais! ===")
            break
        else:
            print("\n@@@ Opção inválida! Tente novamente. @@@")


if __name__ == '__main__':
    main()
