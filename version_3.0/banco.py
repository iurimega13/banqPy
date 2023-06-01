from conta import Conta
from usuario import Usuario


class Banco:
    def __init__(self):
        self.contas = []
        self.usuarios = []

    def criar_conta(self, agencia, usuario):
        numero_conta = str(len(self.contas) + 1)
        conta = Conta(agencia, numero_conta, usuario)
        self.contas.append(conta)

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)

    def listar_contas(self):
        for conta in self.contas:
            print(f"""
                Agência:\t\t{conta.agencia}
                Número Conta:\t{conta.numero_conta}
                CPF:\t\t{conta.usuario.cpf}
                Nome:\t\t{conta.usuario.nome}
                Saldo:\t\tR$ {conta.saldo:.2f}
            """)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"""
                Nome:\t\t{usuario.nome}
                Data Nasc.:\t{usuario.data_nascimento}
                CPF:\t\t{usuario.cpf}
                Endereço:\t{usuario.endereco}
            """)

    def filtrar_usuario(self, cpf):
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario.cpf == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def filtrar_conta(self, agencia, numero_conta):
        contas_filtradas = [conta for conta in self.contas if conta.agencia == agencia and conta.numero_conta == numero_conta]
        return contas_filtradas[0] if contas_filtradas else None
