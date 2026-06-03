def rotate_an_array(arr:list , k:int):
    if k<=0 or not arr:
        return
    k %= len(arr)
    def reverse(start:int, end:int):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0,len(arr)-1)
    reverse(0,k)
    reverse(k+1,len(arr)-1)

def main():
    rotation:int = 2
    input_array: list = [1,2,3,4,5]
    print("Before rotation :: ",input_array)
    rotate_an_array(arr=input_array, k=rotation)
    print("After rotation :: ",input_array)

if __name__ == "__main__":
    main()