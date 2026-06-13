def merge(arr: list, start: int, mid: int, end: int):
    print(arr)
    temp: list = []
    i, j = start, mid
    while i < mid and j < end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while i < mid:
        temp.append(arr[i])
        i += 1
    while j < end:
        temp.append(arr[j])
        j +=1
    for itr in range(len(temp)):
        arr[start+itr] = temp[itr]


def merge_sort(arr: list, start: int, end: int):
    if end - start <=1:
        return
    mid: int = (start+end)//2
    merge_sort(arr,start,mid)
    merge_sort(arr,mid,end)
    merge(arr, start, mid, end)


def main():
    input_list: list = [5,4,3,2,1]
    merge_sort(arr=input_list, start=0, end=len(input_list))
    print(input_list)



if __name__ == "__main__":
    main()

    

