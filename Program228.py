import os
def Read(Filename):

    if os.path.exists(Filename):
        fobj = open(Filename,'r')

        char = fobj.read()

        print(char)
        
def main():

    print("Enter the Filename")
    ch = input()

    Read(ch)

if __name__ == "__main__":
    main()