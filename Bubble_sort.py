def bubble_sort(array:list)->list:
    n = len(array)
    for i in range(n):
        swapped:bool = False
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break

    return array

def main():
    input_array:list = [2,1,5,3,4]
    print("input array :: ",input_array)
    output_array:list = bubble_sort(array=input_array)
    print("output array :: ",output_array)

if __name__ == "__main__":
    main()
