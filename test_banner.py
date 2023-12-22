file = open("E:\\Python\\HelloWorld\\text.txt",'w')
def print_banner(text,file_input):
    banner_width = 100
    border_char = "#"
    padding_char = " "
    
    file_input.write(border_char * banner_width + "\n")
    
    # Calculate padding for centering text
    padding_length = (banner_width - len(text)) // 2
    padding = padding_char * padding_length
    
    # Print the centered text
    file_input.write(f"{border_char}{padding}{text}{padding}{border_char}"+"\n")
    
    file_input.write(border_char * banner_width + "\n")
    file_input.close()

# Call the function to print a banner
print_banner("Welcome to Python Banner Example",file)
