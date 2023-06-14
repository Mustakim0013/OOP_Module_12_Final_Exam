from bank import Bank
bank = Bank()
class User:
    Account = []
    History = {}

    def __init__(self, name, email, password, nid):
        self.name = name
        self.email = email
        self.password = password
        self.nid = nid
        self.current_balance = 0
        self.loanable_balance = 0

    def create_account(self):
        self.Account.append(self)
        self.History[self.name] = []  # Initialize empty history list for the user
        self.History[self.name] = []  # Initialize empty history list for the recipient

    def deposit(self, amount):
        self.current_balance += amount
        print("Deposit: ",amount)
        

    def withdraw(self, amount):
        if(amount >= bank.total_balance):
            print("Bank is Bankrupt")
        elif(self.current_balance >= amount):
            self.current_balance -= amount
            print("Withdraw: ",amount)
        else:
            print("Insufficient funds")
        
            

    def available_balance(self):
        bank.total_balance=+self.current_balance
        print('Balance:', self.current_balance)
        print('Loanable balance:', self.current_balance * 2)

    def transfer(self, amount, recipient):
        if self.current_balance >= amount:
            self.current_balance -= amount
            recipient.current_balance += amount
            self.History[self.name].append(f"{self.name} Transfer: -{amount} to {recipient.name}")
            recipient.History[recipient.name].append(f"Transfer: +{amount} from {self.name}")
            print(self.name,"transfer ",amount,"to ",recipient.name)

        else:
            print("Insufficient funds")
