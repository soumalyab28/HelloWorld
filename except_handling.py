x = 5
y = 2
z = 0
res,res_div = 0,0
try:
    res_div = y/z
    res = x * y
except:
    print("Can't divide by zero")
finally:
    if (x*y):
        print(res)
        print(res_div)