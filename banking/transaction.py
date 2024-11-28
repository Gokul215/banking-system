class transaction:
    id=1
    transactionmap={}
    transactionlist=[]
    def __init__(self,customerid,type,amount,balance) -> None:
        self.customerid=customerid
        self.transactionid=transaction.id
        transaction.id+=1
        self.type=type
        self.amount=amount
        self.balance=balance
    def __str__(self) -> str:
        return f"{self.transactionid} {self.type} {self.amount} {self.balance}"
    def settransactioid():
        filename='transaction.txt'
        with open(filename) as file:
            li=file.readlines()
        if li:
            lastlineintransaction=li[-1].split()
            lastid=lastlineintransaction[0]
            transaction.id=int(lastid)+1
        else:
             transaction.id==0