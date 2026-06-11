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
