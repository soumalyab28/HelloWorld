def checkPrime(num):
    if num < 0:
        return False
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num > 2:
        for i in range(2,num,1):
            remainder = num%i
            if remainder == 0:
                primeChecker = False
                break
            elif num%i > 0:
                primeChecker = True
    return primeChecker

def printPrime(limit):
    for num in range(2,limit,1):
        if checkPrime(num):
            print(str(num), end=', ')

input_num = input("Enter any number : ")
num = int(input_num)
if checkPrime(num):
    print(str(num)+' is a Prime Number')
else:
    print(str(num)+' is not a Prime Number')

input_num = input("Enter any limit upto which Prime number are needed : ")
num = int(input_num)
printPrime(num)