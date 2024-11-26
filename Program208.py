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

        while(temp != None):
            print(f"|{temp.data}|->",end='')
            temp = temp.next
        
        print("NULL")

    def InsertFirst(self,iNo):

        newn = node(iNo)
        if(self.First == None):
            self.First = newn

        else:
            newn.next = self.First
            self.First = newn
    
        self.iCnt += 1

    def Largest(self):

        temp = self.First
        iNo = 0
        Largest = temp.data

        while(temp != None):
            iNo = temp.data

            if(Largest < iNo):
                Largest = iNo

            temp = temp.next
        
        return Largest
    
def main(): 

    obj = SinglyLL()
    obj.InsertFirst(9)
    obj.InsertFirst(32)
    obj.InsertFirst(20)
    obj.InsertFirst(11)

    obj.Display()

    iRet = obj.Largest()
    print(iRet) 


if __name__ == "__main__":
    main()