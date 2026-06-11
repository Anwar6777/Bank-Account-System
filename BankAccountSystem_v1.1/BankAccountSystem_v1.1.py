class Account:
    def __init__(self, acc_no, holder_name, bal):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = bal
        self.transactions = []
        
    def __str__(self):
        return f"""Account Number: {self.acc_no}
Account Holder Name: {self.holder_name}
Balance: {self.__balance}"""

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit Amount can't be negative.")
            self.__balance += amount
            self.transactions.append(
                f"Deposited ₹{amount}"
            )
            return True
        except ValueError as e:
            print("Transaction Failed!", e)
            return False
                
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdraw Amount can't be negative.")
            elif amount > self.__balance:
                raise ValueError("Insufficient balance!.")
            self.__balance -= amount
            self.transactions.append(
                f"Withdrawn ₹{amount}"
            )
            return True
        except ValueError as e:
            print("Transaction Failed!", e)
            return False

    def check_balance(self):
        return self.__balance
    
    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)
            
    def transfer(self, receiver, amount):
        if not isinstance(receiver, Account):
            print("Invalid receiver account")
            return False
        if self.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False
        

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, account):
        if account.acc_no not in self.accounts.keys():
            self.accounts[account.acc_no] = account
        else:
            print("Account already exists!")

    def delete_account(self, acc_no):
        if acc_no in self.accounts.keys():
            del self.accounts[acc_no]
        else:
            print("Account doesn't exists!")
        
    def search_account(self, acc_no):
        if acc_no in self.accounts.keys():
            return self.accounts[acc_no]
        else:
            print("Account doesn't exists!")
    def view_all_accounts(self):
        for account in self.accounts.values():
            print(account)