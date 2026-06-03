def find_int(string:str)->list:
    if not string:
        return []
    
    nums:list = []
    digit:str = ""
    for ch in string:
        if ch.isdigit():
            digit += ch
        else:
            if len(digit)>0:
                nums.append(digit)
                digit = ""
    
    if len(digit)>0:
        nums.append(digit)
    return nums

def main():
    input_string = "12.number of string in this string 1234"
    digits:list = find_int(string=input_string)
    if not digits:
        print("Digits not found in the list")
    else:
        print("Digits :: ",digits)

if __name__ == "__main__":
    main()
    


    
