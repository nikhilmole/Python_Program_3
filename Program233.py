def AddCol(Arr,iRow,iCol):

    temp = 0

    for i in range(iRow-1):
        for j in range(iCol):
            temp = Arr[i][j]
            Arr[i][j] = Arr[i + 1][j]
            Arr[i + 1][j] = temp
def main():

    print("Enter the Number of rows : ")
    iNo1 = int(input())

    print("Enter the Number of cols : ")
    iNo2 = int(input())

    print("Enter the elements : ")
    arr = []
    for i in range(iNo1):
        ptr = []
        for j in range(iNo2):
            iValue = int(input())
            ptr.append(iValue)
        arr.append(ptr)

    print("Entered numbers are : ")
    for i in range(iNo1):
        for j in range(iNo2):
            print(arr[i][j],end = '\t')
        
        print()

    AddCol(arr,iNo1,iNo2)
    print("After swaping : ")
    for i in range(iNo1):
        for j in range(iNo2):
            print(arr[i][j],end = '\t')
        
        print()
if __name__ == "__main__":
    main()