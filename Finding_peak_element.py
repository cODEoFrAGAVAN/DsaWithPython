def peak_element(array:list)->dict:
    if len(array)<=0:
        return -1
    max_index = 0
    max_element = array[max_index]
    for i in range(1,len(array)):
        if array[i] > max_element :
            max_element = array[i]
            max_index = i
    return {
        "max_element":max_element,
        "max_index":max_index
    }

def main():
    input_list:list = [1,2,3,2,1]
    peak_value = peak_element(array=input_list)
    print(peak_value)

if __name__ == "__main__":
    main()