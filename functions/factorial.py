n=int(input("Enter the value of n:"))
def is_fact(n):
    return 1 if(n==0 or n==1) else  n*is_fact(n-1)

print(is_fact(n))

   
          