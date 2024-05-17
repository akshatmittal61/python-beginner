# Normal functions
def add(x, y):
    return x+y
print(add(4, 5))

# defining lambda function - inline, anonymous function
lambda x,y: x+y

# add an identifier
add2 = (lambda x,y: x+y)
print(add2(4,5))

# Call them as IIFE
print((lambda x,y: x+y)(4,5))

# make a lambda function to print average of all number args

lambda