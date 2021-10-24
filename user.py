class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
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



diana = User('Diana', 'dianka759@gmailcom', 0)
kiwi = User('Kiwi', 'kiwi@theGreenChicken.com', 0)
angelika = User('Angelika','andzia@wp.pl', 0)

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
print("The updated balances after transfer:")
diana.transfer_money(angelika, 5)
diana.display_user_balance()
angelika.display_user_balance()