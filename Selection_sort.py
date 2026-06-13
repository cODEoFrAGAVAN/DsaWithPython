def selection_sort(arr:list)-> list:
    if not arr:
        return arr
    n:int = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

def main():
    input_array:list = [5,4,3,2,1]
    print("Before sorting :: ",input_array)
    output_array:list = selection_sort(arr=input_array)
    print("After sorting :: ",output_array)

if __name__ == "__main__":
    main()
