class Customer:
    def __init__(self,customerid,accno,name,balance,password) -> None:
        self.customerid=customerid
        self.customeraccno=accno
        self.name=name
        self.balance=balance
        self.password=password
        
    def __str__(self) -> str:
        return f"{self.customerid} {self.customeraccno} {self.name} { self.balance} {self.password} "