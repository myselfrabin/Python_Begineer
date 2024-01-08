# is_male=True
# is_tall=False
# if is_male and is_tall:
#     print("You are a male or you are tall:")
    
# else:

#     print("You are neither male nor tall")

# num1=6
# num2=70
# num3=int(input("Enter the num3:"))
# if num3>num2:
#     print("Greater")
# else:
#     print("Lesser")
    
#     A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount. 

salary=int(input("Enter the salary you will get:"))
yos=int(input("Enter the yos you have done in this company:"))
if yos>5:
    print("Your salary will increse by 5% bonus:", 0.05*salary)
else:
    print("YOu have to gain some more experience")    