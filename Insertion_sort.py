def insertion_sort(arr:list)->list:
    if not arr:
        return arr

    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def main():
    input_array:list = [5,3,2,1,4]
    print("Before sorting :: ",input_array)
    output_array:list = insertion_sort(arr=input_array)
    print("After sorting :: ",output_array)

if __name__ == "__main__":
    main()