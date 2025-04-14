
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. El Saldo Actual es {self.balance}")
        else:
            print("No se puede depositar, Cuenta INACTIVA")

    def withDraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. El Saldo Actual de {self.account_holder} es {self.balance}")
        else:
            print("No se pudo RETIRAR! CUENTA INACTIVA")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido DESACTIVADA")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido DESACTIVADA")


account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

# Llamada a los metodos
account1.deposit(200)
account2.deposit(100)

account1.deactivate_account()
account1.deposit(50)
account1.withDraw(200)

account2.withDraw(600)
