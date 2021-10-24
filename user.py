class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Account balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("The updated balances after transfer:")
        self.display_user_balance()
        other_user.display_user_balance()



diana = User('Diana')
kiwi = User('Kiwi')
angelika = User('Angelika')

diana.make_deposit(100)
diana.make_deposit(5)
diana.make_deposit(10)
diana.make_withdrawal(110)
diana.display_user_balance()

kiwi.make_deposit(100)
kiwi.make_deposit(50)
kiwi.make_withdrawal(20)
kiwi.make_withdrawal(40)
kiwi.display_user_balance()

angelika.make_deposit(1000)
angelika.make_withdrawal(500)
angelika.make_withdrawal(300)
angelika.make_withdrawal(199)
angelika.display_user_balance()


print("")
diana.transfer_money(angelika, 5)