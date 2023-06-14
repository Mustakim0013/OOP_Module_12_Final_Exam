
class Bank:
    
    fuser = []
    total_balance = 0
    loan_feature = False

    def create_account(self, user):
        self.fuser.append(user)

    def get_total_balance(self):
        total_balance = sum(user.current_balance for user in self.fuser)
        return total_balance
        

    def get_total_loan_amount(self):
        total_loan_amount = sum(user.current_balance * 2 for user in self.fuser)
        return total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature = True

    def disable_loan_feature(self):
        self.loan_feature = False
