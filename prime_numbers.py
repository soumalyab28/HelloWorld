def checkPrime(num):
    if num < 0:
        primeChecker = False
    if num == 1:
        primeChecker = False
    elif num == 2:
        primeChecker = True
    elif num > 2:
        for i in range(2,num,1):
            remainder = num%i
            if remainder == 0:
                primeChecker = False
                break
            elif num%i > 0:
                primeChecker = True
    return primeChecker

def printPrime(lower_limit,upper_limit):
    for num in range(lower_limit,upper_limit,1):
        if checkPrime(num):
            print(str(num), end=', ')

# The ratinale being  - Choice 1 - for checking if an input number is Prime and choice 2 to generate a set of Prime Numbers 
# between two limits
choice_for_Prime = input(" Enter 1 for Prime Number check ;  Enter 2 for Prime Number generation \n")
choice_for_Prime = int(choice_for_Prime)
if choice_for_Prime == 1:
    input_num = input("Enter any number : ")
    num = int(input_num)
    if checkPrime(num):
        print(str(num)+' is a Prime Number')
    else:
        print(str(num)+' is not a Prime Number')

# The Upper limit should be greater than lower limit and both should be positive integers. Not null condition must also be handled.
elif choice_for_Prime == 2:
    input_ll = input("Enter the lower limit for Prime Number generation: ")
    if input_ll is None:
        input_ll = 2
    else:
        input_ll = int(input_ll)
    input_ul = input("Enter the upper limit for Prime Number generation: ")
    input_ul = int(input_ul)

    if (0 < input_ll < input_ul and input_ul is not None):
        printPrime(input_ll,input_ul)
    else:
        print("Upper limit must be greater than Lower Limit and both should be psotitive integers and not null")
else:
    print("Incorrect choice.. Exitting")
