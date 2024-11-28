from Customer import Customer
from Bank import Bank
from transaction import transaction


class customerfilehandling:
    def initialize(self,filename,customers):
        file=open(filename,'r')
        for f in file.readlines():
            
            f=f.rstrip()
            customers.append(f)
        file.close()
    def stringtocustomer(self,customers):
        for customer in customers:
            customerdetail=customer.split()
            customerid=int(customerdetail[0])
            customeraccno=customerdetail[1]
            customername=customerdetail[2]
            customerbalance=customerdetail[3]
            customerpassword=customerdetail[4]
            # print(customerid)
            custom=Customer(customerid,customeraccno,customername,customerbalance,customerpassword)
            Bank.customerlist.append(custom)
            Bank.customermap[customerid]=custom
    # def customertostring(self,customer,filename):
    #     file=open(filename,'a')
    #     file.write(str(customer))
        
    def updatecustomerstring(self,filename):
        # print(customer.balance)
        # with open(filename) as file:
        #     li=file.readlines()
        # for line in range(len(li)):
        #     cuslist=li[line].split()
        #     # print(cuslist)
        #     customerid=cuslist[0]
        #     if int(customerid)==customer.customerid:
        #         li[line]=str(customer).strip()
        # print(li)
        # print(Bank.customermap)
        with open(filename,'w') as file:

            for id,customer in Bank.customermap.items():
                    # print(str(customer))
                    file.write(str(customer)+'\n')
                    
    def transactionhandling(self,filename):
         with open(filename,'w') as file:

            for customertransact in transaction.transactionlist:
                    # print(str(customertransact))
                    file.write(str(customertransact)+'\n')
        
        

