class bankaccount():
    def __init__(self,minbal=500,curbal=1000):
        self.__minbal=minbal
        self.__curbal=curbal
    def Withdraw(self,amount=0):
        self.__curbal=self.__curbal-amount
        if (self.__curbal) < self.__minbal:
            raise Exception("Low Balance")
        
    def __str__(self):
        str=f"Minimum Balance: {self.__minbal}\nCurrent Balance: {self.__curbal}"
        return str
def main ():
    x=[]
    a=bankaccount(200,1000) 
    x.append(a)
    b=bankaccount(100,300)
    x.append(b)
    a.Withdraw(100)
    c=bankaccount(1000,2000)
    #c.withdraw(1100)
    for i in x:
        print(i)
    
    
main()        
            
           
        
