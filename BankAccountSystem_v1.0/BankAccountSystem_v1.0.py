class Account:
    def __init__(self, acc_no, holder_name, bal):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = bal
        
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit Amount can't be negative.")
            self.__balance += amount
            print(f"Amount {amount} has been deposited into your account number: {self.acc_no}.")            
        except ValueError as e:
            print("Transaction Failed!", e)
                
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdraw Amount can't be negative.")
            elif amount > self.__balance:
                raise ValueError("Insufficient balance!.")
            self.__balance -= amount
            print(f"Amount {amount} has been credited from your account number: {self.acc_no}.")            
        except ValueError as e:
            print("Transaction Failed!", e)
    def check_balance(self):
        return self.__balance

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, account):
        if account.acc_no not in self.accounts.keys():
            self.accounts[account.acc_no] = account
        else:
            print("Account already exists!")

    def delete_account(self, account):
        if account.acc_no in self.accounts.keys():
            del self.accounts[account.acc_no]
        else:
            print("Account doesn't exists!")
        
    def search_account(self, account):
        if account.acc_no in self.accounts.keys():
            print("Account Found!")
        else:
            print("Account doesn't exists!")
    def view_all_accounts(self):
        return self.accounts