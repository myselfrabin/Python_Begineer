# Inverted Pyramid pattern with the same digit
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5

n=int(input("Enter the number of rows you want to print"))
for i in range(1,n+1):
    for j in range((n+1)-i):
        print(5,end=' ')
    print()    