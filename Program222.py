import os

def Size(Filename):

    if os.path.exists(Filename):
        print("The file gets successfully open")
        iSize = os.path.getsize(Filename)

    else:
        print("The file is not available on this path")

    return iSize

def main():

    print("Plss enter the file name you want to get size : ")
    ch = input()

    iRet = Size(ch)
    print("The size of the file is : ",iRet)

if __name__ == "__main__":
    main()