class BankAccount:
    def __init__(self, IBAN, AccNum, funds):
        self.IBAN = IBAN
        self.AccNum = AccNum
        self.funds = funds
        self.transactions = []

    def withdraw(self, withdraw):
        self.funds -=  withdraw
        self.add_transaction("${} : Withdrew".format(self.funds))


    def deposit(self, deposit):
        self.funds += deposit
        self.add_transaction("${} : Deposited".format(self.funds))

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if len(self.transactions) > 5:
            self.transactions.pop(0)



    def __str__(self):
        return "{} : IBAN\n{} : Account Number\n${} : Funds\n{} : Transactions".format(self.IBAN, self.AccNum, self.funds, self.transactions)



acc1 = BankAccount("BIO101", 101, 100)
acc1.withdraw(50)
acc1.deposit(100)
acc1.deposit(2000)
acc1.withdraw(10)
acc1.withdraw(100)
acc1.deposit(10)
acc1.withdraw(1000)


print(acc1)


