def Transpose(Arr, iRow, iCol):
    # Create a new matrix for the transposed result
    transposed = [[0] * iRow for _ in range(iCol)]
    
    for i in range(iRow):
        for j in range(iCol):
            transposed[j][i] = Arr[i][j]
    
    return transposed

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
    transposed_arr = Transpose(arr, iNo1, iNo2)

    print("Transposed elements are:")
    for row in transposed_arr:
        print('\t'.join(map(str, row)))

if __name__ == "__main__":
    main()
