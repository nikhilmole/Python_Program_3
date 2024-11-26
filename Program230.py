def Freq(Arr, iRow, iCol, iFind):
    iCnt = 0

    for i in range(iRow):
        for j in range(iCol):
            if(Arr[i][j] == iFind):
                iCnt += 1

    return iCnt
def main():

    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of cols : ")
    iNo2 = int(input())

    print("Enter the number you want to find the freq : ")
    iFind = int(input())

    print("Enter the Elements : ")
    ptr = []
    for i in range(iNo1):
        arr = []
        for j in range(iNo2):
            ino = int(input())
            arr.append(ino)
        ptr.append(arr)
    
    print("Enter Elemments are : ")
    for i in range(iNo1):
        for j in range(iNo2):
            print(ptr[i][j],end = "\t")

        print()

    iRet = Freq(ptr, iNo1, iNo2, iFind)
    print(iRet)
    
if __name__ == "__main__":
    main()