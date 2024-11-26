class node:
    def __init__(self,iNo):
        self.next = None
        self.data = iNo

class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCnt = 0

    def Display(self):
        temp = self.First
        if(temp == None):
            print("The LL is empty")

        while(temp != None):
            print(f"|{temp.data}|->")
            temp = temp.next
    
    def Count(self):
        return self.iCnt
    
    def InsertFirst(self,iNo):
        newn = node(iNo)

        if(self.First == None):
            self.First = newn
        
        else:
            newn.next = self.First
            self.First = newn
    
    def PrimeNum(self):
        iNum = 0
        temp = self.First

        while(temp != None):
            iNum = temp.data
            isprime = 1
            if(iNum <= 1):
                isprime = 0

            for i in  range(2,iNum // 2 + 1):
                if(iNum % i == 0):
                    isprime = 0
            
            temp = temp.next

            if(isprime):
                print(f"{iNum} is the prime number")
def main():

    obj = SinglyLL() 
    
    obj.InsertFirst(89)
    obj.InsertFirst(6)
    obj.InsertFirst(41)
    obj.InsertFirst(17)
    obj.InsertFirst(28) 
    obj.InsertFirst(11)

    obj.Display()

    obj.PrimeNum()


if __name__ == "__main__":
    main()