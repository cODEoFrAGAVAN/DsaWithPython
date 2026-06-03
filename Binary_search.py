def binary_search(arr:list, target:int) -> int:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1
        
    return -1

def main():
    input_list:list = [5,4,3,10,44]
    target_num = 44
    value = binary_search(arr=input_list, target=target_num)
    if value == -1:
        print("The value is not found in the list")
    else:
        print(f"The value is found in the list in the index of {value}")

if __name__ == "__main__":
    main()
