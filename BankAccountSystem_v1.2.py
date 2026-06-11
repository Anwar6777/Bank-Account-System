import json
from datetime import datetime
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
                {
                    "type": "deposit",
                    "amount": amount,
                    "timestamp": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }
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
                {
                    "type": "withdraw",
                    "amount": amount,
                    "timestamp": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }
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
            receiver.transactions.append(
                {
                    "type": "received",
                    "amount": amount,
                    "from": self.acc_no,
                    "timestamp": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }
            )
            return True
        return False
        
    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "holder_name": self.holder_name,
            "balance": self.__balance,
            "transactions": self.transactions
        }
        
    @classmethod
    def from_dict(cls, data):
        account = cls(
            data["acc_no"],
            data["holder_name"],
            data["balance"]
        )
        account.transactions = data["transactions"]
        return account



class Bank:
    def __init__(self, bank_name):
        self.bank_name  = bank_name
        self.accounts = {}
        self.load_data()

    def create_account(self, account):
        if account.acc_no not in self.accounts:
            self.accounts[account.acc_no] = account
            self.save_data()
        else:
            print("Account already exists!")

    def delete_account(self, acc_no):
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            self.save_data()
        else:
            print("Account doesn't exists!")
        
        
    def search_account(self, acc_no):
        account = self.accounts.get(acc_no)
        if not account:
            print("Account doesn't exist!")
        return account
    def view_all_accounts(self):
        for account in self.accounts.values():
            print(account)
            
    def save_data(self):
        data = {}
        for acc_no, account in self.accounts.items():
            data[acc_no] = account.to_dict()
        with open("accounts.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("accounts.json", "r") as f:
                data = json.load(f)
                for acc_no, acc_data in data.items():
                    self.accounts[int(acc_no)] = (
                        Account.from_dict(acc_data)
                    )
        except FileNotFoundError:
            print("File not found!")
        except json.JSONDecodeError:
            print("Invalid JSON file.")
            
    def deposit(self, acc_no, amount):
        account = self.search_account(acc_no)

        if account:
            if account.deposit(amount):
                self.save_data()
                
    def withdraw(self, acc_no, amount):
        account = self.search_account(acc_no)

        if account:
            if account.withdraw(amount):
                self.save_data()
                
    def transfer(self, sender_acc_no, receiver_acc_no, amount):
        sender = self.search_account(sender_acc_no)
        receiver = self.search_account(receiver_acc_no)
        if sender and receiver:
            if sender.transfer(receiver, amount):
                self.save_data()
                
