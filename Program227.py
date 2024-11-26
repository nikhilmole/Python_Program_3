import os

def Occ(Filename,ch):

    iCnt = 0
    Occ = 0

    if os.path.exists(Filename):
        fobj = open(Filename,'r')

        while True:

            char = fobj.read(1)

            if not char:
                break

            if(char == ch):
                Occ = iCnt
                break
            
            iCnt += 1

    return Occ

def main():

    print("Enter the file name")
    ch = input()

    print("Enter the chaacter")
    cValue = input()

    iRet = Occ(ch,cValue)
    print(iRet)

if __name__ == "__main__":
    main()