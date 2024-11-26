def DigoAdd(Arr,iRow,iCol):
    iSum = 0

    for i in range(iRow):
        for j in range(iCol):
            if(i == j):
                iSum = iSum + Arr[i][j]

    return iSum

def main():

    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of rows : ")
    iNo2 = int(input())

    print("Enter the element")
    arr = []
    for i in range(iNo1):
        row = []
        for j in range(iNo2):
            iValue = int(input())
            row.append(iValue)
        
        arr.append(row)

    print("Entered elements are")
    for i in range(iNo1):
        for j in range(iNo2):
            print(arr[i][j],end = '\t')
        print()

    iRet = DigoAdd(arr,iNo1,iNo2)
    print(iRet)

if __name__ == "__main__":
    main()