n=int(input("Enter the value of n:"))
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count==2):
        print("Prime")
    else:
        print("Not prime")
is_prime(n)                    