# The "print(" denotes the Python Prompt")
# "E" or "e" implies exponent - or 10^ 
print(10e2)        # 1000.0
print(1E3)         #1000.0
print(10e-2)       # 0.1
print(16/3)  # 5.333333333333333
print(float(16/3))  # 5.333333333333333
print(float(16/float(3)))  # 5.333333333333333
print(format(float(16/float(3))))  # '5.333333333333333'
# print( format(float(16/float(3)),.3f))  #SyntaxError: invalid syntax
print(format(float(16/float(3)), '.3f'))  # '5.333'
print(float(16/3))  # 5.333333333333333
print(format(float(16/float(3)), '.2f'))  # '5.33'
print(round(float(16/3), 2))  # 5.33
print(round(float(16/3), 5))            # 5.33333
print(round(float(17/3), 5))        # 5.66667

#Enter any number and convert it to other Number format
num = int (input("Enter any number : "))
print("\nBinary of "+str(num)+" is : "+ str(bin(num)))
print("\nHexadecimal of "+str(num)+" is : "+ str(hex(num)))
print("\nOctal of "+str(num)+" is : "+ str(oct(num)))
print("\nSquare root of "+str(num)+" is : "+ str(num**0.5))

#Compute area of a triangle by Heron's formula
print("\nEnter three sides of the triangle : ")
side1 = float(input("First side : "))
side2 = float(input("Second side : "))
side3 = float(input("Third side : "))
s = (side1 + side2 + side3)/2
area = format((s*(s-side1)*(s-side2)*(s-side3))**0.5,'0.3f')
print("\nArea of the triangle is : " + str(area))