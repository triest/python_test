class Account:
    name = '';
    Balance = dict()

    def __init__(self) -> None:
        self.Balance['USD'] = 0
        self.Balance['GBP'] = 0
        self.Balance['JPY'] = 0
        self.Balance['RUB'] = 0
        super().__init__()

    def getBalans(self):
        return self.Balance

    def setBalanse(self, param, cunnercy):
        self.Balance[param] = cunnercy;
        pass
