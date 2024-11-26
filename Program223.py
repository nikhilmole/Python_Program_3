import os

def Append(Filename,Data):

    if os.pat.exists(Filename):

        fobj = open(Filename,'a')

        fobj.write(Data)
        print("Successfully append the data")
    
    else:
        print("cannot uppend the data")


def main():

    print("Enter the Filename you want to append the data")
    ch = input()

    print("Enter the data you want to add in file")
    Data = input()

    Append(ch,Data)

if __name__ == "__main__":
    main()