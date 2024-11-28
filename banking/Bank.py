class Bank:
    customerid=0
    accno=11003
    customerlist=[]
    customermap={}
    def setcustomerid():
        filename='bankdb.txt'
        with open(filename) as file:
            li=file.readlines()
        if li:
            lastlineintransaction=li[-1].split()
            lastid=lastlineintransaction[0]
            Bank.customerid=int(lastid)+1
        else:
            Bank.customerid=1
    
        