from user import User
from admin import Admin
from bank import Bank

# Create instances
user1 = User("Bill", "Bill@example.com", "password123", "1234567890")
user1.create_account()

# Create user account
admin = Admin("admin", "admin123")
bank = Bank()
bank.create_account(user1)
admin.create_account(user1)

# Deposit and withdraw

user1.deposit(500)
user1.available_balance()
print("---------------------")
bank.get_total_balance()
admin.check_total_balance(bank)
user1.withdraw(100)
user1.available_balance()
print("---------------------")
# Transfer
user2 = User("Elon", "Elon@example.com", "password123", "1234567890")
user2.create_account()
admin.create_account(user2)
bank.create_account(user2)

user1.transfer(200,user2)
user1.available_balance()

# Check total balance and total loan amount
admin.check_total_balance(bank)
admin.check_total_loan_amount(bank)

# Enable/disable loan feature
admin.enable_loan_feature(bank)
admin.disable_loan_feature(bank)

print(Bank.get_total_balance(bank))

# Deposit and withdraw
user1.transfer(100,user2)
user1.available_balance()
admin.check_total_balance(bank)
user1.withdraw(600)

# Check total balance 
bank.get_total_balance()
admin.check_total_balance(bank)
user2.withdraw(50)
user2.available_balance()
bank.get_total_balance()
admin.check_total_balance(bank)
