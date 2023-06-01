from banco import Banco


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


def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == 'd':
            agencia = input("Informe o número da agência: ")
            numero_conta = input("Informe o número da conta: ")
            valor = float(input("Informe o valor do depósito: "))

            conta = banco.filtrar_conta(agencia, numero_conta)
            if conta:
                conta.depositar(valor)
                print("\n=== Depósito realizado com sucesso! ===")
            else:
                print("\n@@@ Conta não encontrada! @@@")
        elif opcao == 's':
            agencia = input("Informe o número da agência: ")
            numero_conta = input("Informe o número da conta: ")
            valor = float(input("Informe o valor do saque: "))

            conta = banco.filtrar_conta(agencia, numero_conta)
            if conta:
                if conta.sacar(valor):
                    print("\n=== Saque realizado com sucesso! ===")
                else:
                    print("\n@@@ Operação falhou! Verifique o valor informado e as condições de saque. @@@")
            else:
                print("\n@@@ Conta não encontrada! @@@")
        elif opcao == 'e':
            agencia = input("Informe o número da agência: ")
            numero_conta = input("Informe o número da conta: ")

            conta = banco.filtrar_conta(agencia, numero_conta)
            if conta:
                conta.exibir_extrato()
            else:
                print("\n@@@ Conta não encontrada! @@@")
        elif opcao == 'nc':
            cpf = input("Informe o CPF do usuário: ")
            usuario = banco.filtrar_usuario(cpf)

            if usuario:
                agencia = input("Informe o número da agência: ")
                banco.criar_conta(agencia, usuario)
                print("\n=== Conta criada com sucesso! ===")
            else:
                print("\n@@@ Usuário não encontrado! @@@")
        elif opcao == 'lc':
            banco.listar_contas()
        elif opcao == 'nu':
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            cpf = input("Informe o CPF (somente número): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

            banco.criar_usuario(nome, data_nascimento, cpf, endereco)
            print("\n=== Usuário criado com sucesso! ===")
        elif opcao == 'lu':
            banco.listar_usuarios()
        elif opcao == 'q':
            print("\n=== Sessão encerrada. Até mais! ===")
            break
        else:
            print("\n@@@ Opção inválida! Tente novamente. @@@")


if __name__ == '__main__':
    main()
