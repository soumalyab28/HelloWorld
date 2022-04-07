#Fibonacci Series
def fibonacci(limit):
    def sum_num (a,b):
        return a+b

    a = 0
    b = 1
    i = 0

    while i < 10:
        sum = sum_num(a,b)  # Get the sum from the function created above
        a = b               # Assign the 2nd num to 1st num
        b = sum             # The sum becomes the 2nd num for next iteration
        i = sum + a         # i variable is assigned the future number 
        print(str(sum), end = ' ')          # Display the sequence horizontally


# for val in range(10):
#     my_list[val] = fibonacci(10)

# print(my_list)