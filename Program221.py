import os

def Read(Filename):

    if os.path.exists(Filename):
        print("Unable to open file")

    else:
        fobj = open(Filename,'r')
        print("File gets successfuly open")

        Data = fobj.read()
        print(Data)

        fobj.close()

def main():

    print("Enter the File name you want to read")
    ch = input()

    Read(ch)

if __name__ == "__main__":
    main()