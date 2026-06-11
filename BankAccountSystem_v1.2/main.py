from account import Account
from bank import Bank

if __name__ == "__main__":
    bank = Bank("My Bank")
    
    # Create accounts
    acc1 = Account("12345", "Alice", 1000)
    acc2 = Account("67890", "Bob", 2000)
    
    # Add accounts to the bank
    bank.create_account(acc1)
    bank.create_account(acc2)
    # View all accounts
    bank.view_all_accounts()