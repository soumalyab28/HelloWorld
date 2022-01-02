#from typing import TYPE_CHECKING


# Print the length of any input string
input_str = input("Enter any string : ")
#print("Length of input string \""+input_str +"\" is : "+len(input_str))  # Gives Error
print("\nLength of input string \""+input_str+"\" is : "+str(len(input_str)))
print(f"Length of input string \""+input_str+"\" is : " +str(len(input_str)))  # - gives same output

# Print the character at specific indexes
if len(input_str) == 0:
    print("\nInput String is empty or NULL.. Exitting \n")
    exit

elif len(input_str) > 0:
    indx = input("\nEnter the index : ")
if int(indx) > len(input_str):
    print("\nThe Input index is greater than the computable length of input string.. " + str(len(input_str))+"\" .. Exitting\n")
    exit

elif int(indx) < 1:
    print("\nSorry.. Input index must be greater then zero\n")

elif int(indx) <= len(input_str) and int(indx) > 0:
    print("\nThe letter at position "+indx+" of the input String \"" +
          input_str+" is : "+input_str[int(indx)-1]+"\n")

if 0 < int(indx) <= len(input_str):
    print("\nThe letter at position "+indx+" of the input String \"" +
          input_str+"\" is : "+input_str[int(indx)-1]+"\n")

else:
    print("\nThe Input index is either greater than the computable length of input string or zero.. " + str(len(input_str))+"\" .. Exitting\n")

for var in range(len(input_str)-1, 0):
    print(input_str[var])
