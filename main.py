from BankAccount import BankAccount

account = BankAccount("John's Account", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
