
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loan_feature = False

    def create_account(self, user):
        user.create_account()

    def check_total_balance(self,bank):
        total_balance = bank.get_total_balance()
        print("Total Bank balance:", total_balance)

    def check_total_loan_amount(self, bank):
        total_loan_amount = bank.get_total_loan_amount()
        print("Total loan amount:", total_loan_amount)

    def enable_loan_feature(self, bank):
        bank.enable_loan_feature()
        print("Loan feature is enabled.")

    def disable_loan_feature(self, bank):
        bank.disable_loan_feature()
        print("Loan feature is disabled.")
