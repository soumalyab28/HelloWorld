def get_character(input_char,step):
    ascii_value = ord(input_char)
    if ascii_value >= 65 and ascii_value <=90:
        new_ascii = ascii_value + step
        if new_ascii > 90:
            new_ascii = 65 + new_ascii % 90

    elif ascii_value >= 97 and ascii_value <= 122:
        new_ascii = ascii_value + step
        if new_ascii > 122:
            new_ascii = 97 + new_ascii % 122
    
    elif (ascii_value < 65 and ascii_value > 90) or (ascii_value < 97 and ascii_value > 122):
        new_ascii = ascii_value
        
    return chr(new_ascii)

input_str = str(input("Enter a string : "))
step = int(input("Enter step : "))


for i in input_str:
    new_char = get_character(i,step)
    print(new_char, end='')
