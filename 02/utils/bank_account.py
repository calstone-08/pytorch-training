class BankAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest_rate = 0.01

    def deposit( self, money ): # 預金を追加する
        self.balance += money
    
    def withdraw( self, money ): # 預金を減らす
        self.balance -= money

    def get_balance(self): # 現在の預金を返す
        return self.balance

    def set_interest_rate( self, rate ): # 金利を設定する
        self.interest_rate = rate

    def apply_interest(self): # 金利を適用して預金を増やす
        self.balance = round(self.balance * ( 1 + self.interest_rate), 1)