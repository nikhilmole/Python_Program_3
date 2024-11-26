def Matrice(Arr, iRow, iCol):
    
    temp = 0
    for i in range(iRow):
        for j in range(iCol):
            if((i == j)and(Arr[i][j] != 1)):
                return False
            elif((i != j)and(Arr[i][j] != 0)):
                return False

    return True

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
    bRet = Matrice(arr, iNo1, iNo2)
    if(bRet == False):
        print("False")
    else:
        print("True")

            
if __name__ == "__main__":
    main()
