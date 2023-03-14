def add(x,y):
    return x+y
def sub(x,y):
    return x-y 
def mult(x,y):
    return x*y 
def div(x,y):
    return x/y 

x=int(input("Enter first no."))
y=int(input("Enter second no."))
z=input("Enter operation")
if z=="+":
   print(add(x,y))
if z=="-":
   print(sub(x,y))
if z=="*":
   print(mult(x,y))
if z=="/":
   print(div(x,y))


