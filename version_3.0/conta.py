class Conta:
    def __init__(self, agencia, numero_conta, usuario, saldo=0, extrato="", limite=5000, numero_saques=0, limite_saques=5):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = saldo
        self.extrato = extrato
        self.limite = limite
        self.numero_saques = numero_saques
        self.limite_saques = limite_saques

    def depositar(self, valor):
        self.saldo += valor
        self.extrato += f"Depósito:\tR$ {valor:.2f}\n"

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo or excedeu_limite or excedeu_saques or valor <= 0:
            return False

        self.saldo -= valor
        self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        self.numero_saques += 1

        return True

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")
