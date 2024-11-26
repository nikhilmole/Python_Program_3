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
    
    def SeconMax(self):
        iNum = 0
        temp = self.First
        Max = temp.data
        SecondMax = 0

        if(temp == None)or(temp.next == None):
            print("LL is empty")

        while(temp != None):
            iNum = temp.data
            if(iNum > Max):
                SecondMax = Max
                Max = temp.data
            else:
                SecondMax = iNum

            temp = temp.next
        
        return SecondMax
def main():

    obj = SinglyLL() 
    
    obj.InsertFirst(41)
    obj.InsertFirst(32)
    obj.InsertFirst(20)
    obj.InsertFirst(11)

    obj.Display()

    iRet = obj.SeconMax()
    print(iRet)

if __name__ == "__main__":
    main()