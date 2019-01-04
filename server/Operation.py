class Operation:
    method = '';
    data = '';
    account = '';
    amt = '';
    ccy = '';

    def __init__(self, method, data, account, amt, ccy) -> None:
        self.method = method
        self.data = data
        self.account = account
        self.amt = amt
        self.ccy = ccy
        super().__init__()
