from customerfilehandlig import customerfilehandling
from Customer import Customer
from Bank import Bank
from transaction import transaction


class Main:
    def addcustomer(self):
        customername=input("enter customer name: ")
        password=input("enter password: ")
        repassword=input("re enter password: ")
        if password!=repassword:
            print("password not match")
            return
        else:
            password=self.validate(password)
            # print(password)
            customerid=Bank.customerid
            custom=Customer(customerid,Bank.accno,customername,10000,password)
            # customerfie.customertostring(custom,filename)
            Bank.customermap[customerid]=custom
            transact=transaction(customerid,"Opening",10000,custom.balance)
            transaction.transactionlist.append(transact)
            transaction.transactionmap[customerid]=transact
            customerfie.transactionhandling(transationfilename)
            customerfie.updatecustomerstring(filename)
            Bank.customerid+=1
            Bank.accno+=1
            # print(Bank.customermap)
    def validate(self,password):
        password=str(password)
        anotherpassword=''
        for i in range(len(password)):
            
            if password[i].isdigit() and int( password[i]) < 9 and int( password[i]) >=1:
                anotherpassword+=str(int(password[i])+1)
            elif password[i].isdigit() and int(password[i]==9):
                anotherpassword+='0'
            elif password[i].isalpha() and password[i] >='a' and password[i] <'z' :
                anotherpassword+=str(chr(ord(password[i])+1))
            elif  password[i] >='A' and password[i] <'Z':
                anotherpassword+=str(chr(ord(password[i])+1))
            elif password[i].isalpha() and  password[i] == 'z':
                anotherpassword+='a'
            elif password[i].isalpha() and  password[i] == 'Z':
                anotherpassword+='A'
                
        return (anotherpassword)
 
    def verifyuser(self,customerid,password):
        if customerid in Bank.customermap:
            customer=Bank.customermap[customerid]
            customerpassword=customer.password
            if customerpassword==password:
                return True
            else:
                print("wrong password")
                return False
        else:
            print("invalid user")
            return False
        
    def deposit(self,customerid,amount):
    
        if customerid in Bank.customermap:
            customer=Bank.customermap[customerid]
            customer.balance=int(customer.balance)+amount
            transact=transaction(customerid,"Deposit",amount,customer.balance)
            transaction.transactionlist.append(transact)
            transaction.transactionmap[customerid]=transact
            customerfie.transactionhandling(transationfilename)
            
            customerfie.updatecustomerstring(filename)
            print("deposit successful")
        else:
            print("No customer")
            return
    def withdraw(self,customerid,amount):
        
        if customerid in Bank.customermap:
            customer=Bank.customermap[customerid]
            customeramount=customer.balance
            if customeramount-amount>=1000:
                customer.balance-=amount
                transact=transaction(customerid,"Withdraw",amount,customer.balance)
                transaction.transactionlist.append(transact)
                transaction.transactionmap[customerid]=transact
                customerfie.transactionhandling(transationfilename)
                
                customerfie.updatecustomerstring(filename)
                print("withdraw successful")
                return True
                
            else:
                print("Minimum balance limit exceeded")
                return False
        else:
            print("No customer")
            return False
    def transfermoney(self,fromaccountid,toaccountid,amount):
        if toaccountid in Bank.customermap:
            if self.withdraw(fromaccountid,amount):
                self.deposit(toaccountid,amount)
                print("Transfer successful")
        else:
            print("To account invalid")
            return
    
    def viewtransaction(self):
        customerid=int(input("enter the customer id:"))
        if customerid in transaction.transactionmap:
            for customertransact in transaction.transactionlist:
                if customertransact.customerid==customerid:
                    t=str(customertransact)
                    print(t)
        else:
            print("invalid id")
            return 
        
        
        
            
filename='bankdb.txt'
transationfilename='transaction.txt'
customers=[]
customerfie=customerfilehandling()
customerfie.initialize(filename,customers)
customerfie.stringtocustomer(customers)
# print(Bank.customermap)
transaction.settransactioid()
Bank.setcustomerid()

main=Main()

while True:
    print("1. Add customer \n2. cash deposit \n3. withdraw \n4. transfer money \n5.View transaction")
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            main.addcustomer()
        case 2:
            customerid=int(input("enter the customer id: "))
            amount=int(input("enter the amount: "))
            password=input("enter password: ")
            password=main.validate(password)
            # print(password)
            if main.verifyuser(customerid,password):
                main.deposit(customerid,amount)
        case 3:
            customerid=int(input("enter the customer id: "))
            amount=int(input("enter the amount: "))
            password=input("enter password: ")
            password=main.validate(password)
            
            if main.verifyuser(customerid,password):
                main.withdraw(customerid,amount)
        case 4:
            fromaccountid=int(input("enter the from customer id: "))
            toaccountid=int(input("enter the to customer id: "))
            amount=int(input("enter the amount: "))
            password=input("enter password: ")
            password=main.validate(password)
            
        
            if main.verifyuser(fromaccountid,password):
                main.transfermoney(fromaccountid,toaccountid,amount)
        case 5:
            main.viewtransaction()
            
    