def reverse_function(array:list, start:int, end:int):
    while start<end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

def main():
    input_list = [5,10,6,4,2]
    print("before reversing",*input_list)
    rev = reverse_function(input_list,0,len(input_list)-1)
    print("after reversing", *rev)

if __name__ == "__main__":
    main()

