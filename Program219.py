import os

def OpenFile(FileName):

    if os.path.exists(FileName):
        print("File allready available on this path")

    else:
        open(FileName,"x")
        print("File gets successfully created")

    if os.path.exists(FileName):
        open(FileName,"r")
        print("File successfully open for reading purpose")
    
    else:
        print("File is no available on this path")

def main():

    print("Enter the File name you want to create")
    Arr = input()

    OpenFile(Arr)

if __name__ == "__main__":
    main()