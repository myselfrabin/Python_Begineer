num1=float(input("Enter the first number:"))
op=input("Enter the operator you want to perform with:")
num2=float(input("Enter the second number:"))
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
        
else:
    print("You enter a wrong operator")
print("You did an amazing job") 