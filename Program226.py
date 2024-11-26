import os

def CountSpace(Filename):

    iCnt = 0

    if os.path.exists(Filename):

        fobj = open(Filename,'r')

        while True:

            char = fobj.read(1)

            if not char:
                break

            if(char == ' '):
                iCnt += 1
    
    return iCnt

def main():

    print("Enter the file name")
    ch = input()

    iRet = CountSpace(ch)
    print(iRet)

if __name__ == "__main__":
    main()
    


