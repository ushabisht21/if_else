num1=int(input("enter first number:"))
num2=int(input("enter second number"))
symbol=input ("enter the symbol:")
if symbol== "+":
    print(num1 + num2)
elif symbol=="-":
    print(num1 -num2)
elif symbol=="*":
    print(num1 * num2)
elif symbol=="%":
    print(num1 % num2)
elif symbol=="/":
    print(num1 / num2) 
elif symbol=="**":
    print(num1 ** num2)
elif symbol=="//":
    print(num1 // num2)
elif symbol=="==":
      print(num1 == num2)
elif symbol=="!=":
    print(num1!=num2)
elif symbol==">":
    print (num1 > num2)   
elif symbol== ">=":
    print (num1 >= num2)
elif symbol== "<":
    print (num1 < num2)
elif symbol=="<=":
    print(num1 <= num2)
elif symbol=="and":
    print(num1 and num2)
elif symbol=="or":
    print(num1 or num2)
elif symbol=="not":
    print("num1 not num2")
elif symbol=="is":
    print(num1 is num2)
elif symbol=="is not":
    print (num1 is not num2)
elif symbol=="not":
    print (num1 not in num2)
else :   
    print("nothing")