def linear_search(array:list, search_value:int)->int:
    if len(array)==0:
        return -1
    for i in range(0,len(array)):
        if search_value == array[i]:
            return i
    return -1

def main():
    input_value:list = [1,2,3,55,66,3,7,8,9,10]
    finding_value = 55
    search_index = linear_search(array=input_value,search_value=finding_value)
    if search_index > 0:
        print(f"The value is present in the list and the index is {search_index} and the value is {input_value[search_index]}")
    else:
        print("The value is not found in the list")

if __name__ == "__main__":
    main()

