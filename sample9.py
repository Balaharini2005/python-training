Ip=""
while(!="q"):
    def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return"error : div by zero:"
    return x/y
print("=== simple calculator ===")
print("press 'q' to quit.\n")
op = "" 
while op != "q":
    op = input("enter operation(+, - ,*,/ or q to quit):")
    if op =="q":
        print("\n exiting.....Good bye!\n")
        break
    if op not in('+' ,'-', '*' , '/'):
        print("invalid operator! try again .\n")
        continue
    a = int(input("enter the value of a: "))
    b = int(input("enter the value of b:" ))
    Ip=input("again or quit[q]")
else:
    print("thank you")
