def MaxinDigo(Arr,iNo1,iNo2):
    Digo1 = 0
    Digo2 = 0

    for i in range(iNo1):
        for j in range(iNo2):
            if(i == j):
                if(Digo1 < Arr[i][j]):
                    Digo1 = Arr[i][j]

            elif(i + j == iNo2 - 1):
                if(Digo2 < Arr[i][j]):
                    Digo2 = Arr[i][j]
    
    print(Digo1)
    print(Digo2)

def main():

    print("Enter the number or of rows : ")
    iNo1 = int(input())

    print("Enter the number or of cols : ")
    iNo2 = int(input())

    print("Enter the Elements : ")
    arr = []
    for i in range(iNo1):
        ptr = []
        for j in range(iNo2):
            iValue = int(input())
            ptr.append(iValue)
        arr.append(ptr)
    
    for i in range(iNo1):
        for j in range(iNo2):
            print(arr[i][j],end = '\t')
        
        print()

    MaxinDigo(arr,iNo1,iNo2)

if __name__ == "__main__":
    main()