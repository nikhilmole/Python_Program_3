import os

def CountSmall(Filename):

    iCnt = 0

    if os.path.exists(Filename):

        fobj = open(Filename,'r')
        print("File successfully open for reading purpose")

        while True:
            char = fobj.read(1)

            if not char:
                break

            if((char >= 'a')and(char <= 'z')):
                iCnt += 1
    else:
        print("File does not exist into this path")
           
    return iCnt
def main():

    print("Enter the file name that you want to count small character")
    ch = input()

    iRet = CountSmall(ch)
    print(iRet)

if __name__ == "__main__":
    main()