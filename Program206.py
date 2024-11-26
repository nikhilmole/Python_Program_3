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
    
    def Pro(self):
        iNo = 0
        iDigit = 0
        temp = self.First
        iPro = 0

        while(temp != None):
            iPro = 1
            iNo = temp.data

            while(iNo > 0):
                iDigit = iNo % 10
                iPro = iPro * iDigit
                iNo = iNo // 10

            print(f"|{iPro}|->")
            temp = temp.next

def main():

    obj = SinglyLL() 
    
    obj.InsertFirst(41)
    obj.InsertFirst(32)
    obj.InsertFirst(20)
    obj.InsertFirst(11)

    obj.Display()

    obj.Pro()

if __name__ == "__main__":
    main()