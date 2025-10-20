def correctvalue():
  while True:
    choices=int(input("Please Enter the correct choices from the given list(1-5):"))
    if choices>=1 and choices<=5 :
      return choices
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def division(a,b):
  if b==0:
    return "As 2nd value is Zero, so ZeroDivision error will occur so please choose aother number rather than zero"
  return a/b
def multiplication(a,b):
  return a*b
print("Welcome to python's Command-Line-Calculator")
while True:
  print("Please select the correct operation from below")
  print("1-Additioin(+)")
  print("2-Subtraction(-)")
  print("3-Multiplication(*)")
  print("4-Division(/)") 
  print("5-End")

  choices=int(input("Enter the correct choices:"))
  if choices>5:
    choices= correctvalue()
    
  if choices==5:
    print("Thank You")
    break
  try:
    a=float(input("Enter the first value:"))
    b=float(input("Enter the first value:"))
  except  ValueError:
    print("Please enter the numeric value only")
  if choices==1:
    print("result:",add(a,b))
  elif choices==2:
    print("result:",subtract(a,b))
  elif choices==3:
    print("result:",multiplication(a,b))        
  elif choices==4:
    if b==0:
      b=float(input("Please enter the another value rather than Zero:"))
    print("result:",division(a,b))    
  else:
    print("Please enter the correct operation")
