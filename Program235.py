def Reverse(Arr, iRow, iCol):
    
    temp = 0
    for i in range(iRow):
        iStart = 0
        iEnd = iCol - 1
        while(iStart < iEnd):
            temp = Arr[i][iStart]
            Arr[i][iStart] = Arr[i][iEnd]
            Arr[i][iEnd] = temp

            iStart += 1
            iEnd -= 1

def main():
    print("Enter the number of rows: ")
    iNo1 = int(input())

    print("Enter the number of cols: ")
    iNo2 = int(input())

    print("Enter the numbers: ")
    arr = []
    for i in range(iNo1):
        ptr = []
        for j in range(iNo2):
            iValue = int(input())
            ptr.append(iValue)
        arr.append(ptr)

    print("Entered elements are:")
    for row in arr:
        print('\t'.join(map(str, row)))

    # Transpose the matrix
    Reverse(arr, iNo1, iNo2)

    print("Transposed elements are:")
    for i in range(iNo1):
        for j in range(iNo2):
            print(arr[i][j],end = '\t')
        print()
            
if __name__ == "__main__":
    main()
