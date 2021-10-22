def maximum(a,b,c):
    if (a > b) and (a > c):
        largest = a
    elif (b > a) and (b > c):
        largest = b
    else:
        largest = c

    return largest

a=30
b=46
c=25
print("The largest number is:", maximum(a, b, c))