import os

def Create(FileName):

    if os.path.exists(FileName):
        print("File Allready exist on this paath")
    
    else:
        open(FileName,"x")
        print("File gets successfully created")

def main():

    print("Enter the File name you want to create : ")
    Arr = input()

    Create(Arr)

if __name__== "__main__":
    main()