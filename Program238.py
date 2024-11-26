def Matrice(Arr, iRow, iCol):
    
    Element = iRow * iCol
    iCnt = 0
    for i in range(iRow):
        for j in range(iCol):
           if(Arr[i][j] == 0):
               iCnt += 1
    
    if(iCnt == Element / 2):
        return True

    return False

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
