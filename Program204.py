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
        print("None")
    
    def Count(self):
        return self.iCnt
    
    def InsertFirst(self,iNo):
        newn = node(iNo)

        if(self.First == None):
            self.First = newn
        
        else:
            newn.next = self.First
            self.First = newn
    
    def Rev(self):
        iNo = 0
        iDigit = 0
        temp = self.First
        iRev = 0

        while(temp != None):
            iRev = 0
            iNo = temp.data

            while(iNo > 0):
                iDigit = iNo % 10
                iRev = iRev * 10 + iDigit
                iNo = iNo // 10
            
            print(f"|{iRev}|->",end = '')
            temp = temp.next

def main():

    obj = SinglyLL() 
    
    obj.InsertFirst(41)
    obj.InsertFirst(32)
    obj.InsertFirst(20)
    obj.InsertFirst(11)

    obj.Display()

    obj.Rev()

if __name__ == "__main__":
    main()