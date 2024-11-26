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

    def Small(self):

        temp = self.First
        iNo = 0
        iSmall = temp.data

        while(temp != None):
            iNo = temp.data

            if(iSmall > iNo):
                iSmall = iNo

            temp = temp.next
        
        return iSmall
    
def main(): 

    obj = SinglyLL()
    obj.InsertFirst(9)
    obj.InsertFirst(32)
    obj.InsertFirst(20)
    obj.InsertFirst(11)

    obj.Display()

    iRet = obj.Small()
    print(iRet) 


if __name__ == "__main__":
    main()