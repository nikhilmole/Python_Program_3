import os

def CountCapital(Filename):

    iCnt = 0

    if os.path.exists(Filename):
        fobj = open(Filename,'r')
        while True:
            char = fobj.read(1)
            if not char:
                break
            if(char >= 'A')and(char <= 'Z'):
                iCnt += 1
    
    return iCnt
    
def main():

    print("Enter the File name : ")
    ch = input()

    iRet = CountCapital(ch)
    print("The capital count is : ",iRet)

if __name__ == "__main__":
    main()