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
            print(f"|{temp.data}|->",end = '')
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
    
    def EvenAdd(self):
        iNum = 0
        temp = self.First
        iAdd = 0

        while(temp != None):
            iNum = temp.data

            if(iNum % 2 == 0):
                iAdd = iAdd + iNum
            
            temp = temp.next
        
        return iAdd
def main():

    obj = SinglyLL() 
    
    obj.InsertFirst(41)
    obj.InsertFirst(32)
    obj.InsertFirst(20)
    obj.InsertFirst(11)

    obj.Display()

    iRet = obj.EvenAdd()
    print(iRet)

if __name__ == "__main__":
    main()