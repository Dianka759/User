class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Account balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("The updated balances after transfer:")
        self.display_user_balance()
        other_user.display_user_balance()


#  defining users
diana = User('Diana')
kiwi = User('Kiwi')
angelika = User('Angelika')

# calling on methods
diana.make_deposit(100).make_deposit(5).make_deposit(10).make_withdrawal(110).display_user_balance()
kiwi.make_deposit(100).make_deposit(50).make_withdrawal(20).make_withdrawal(40).display_user_balance()
angelika.make_deposit(1000).make_withdrawal(500).make_withdrawal(300).make_withdrawal(199).display_user_balance()

# priting a space between previous outputs, transfering money between two users.
print("")
diana.transfer_money(angelika, 5)