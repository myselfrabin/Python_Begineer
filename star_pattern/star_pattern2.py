# *
# * *
# * * *
# * * * *
# * * * * *
# yaha mero 5 ota row number xa i=5 ani i=0 ma 1 ta star xa i=1 ma 2 ta star xa and so on 
# basically j=i+1 huna jancha

n=int(input("Enter the number of rows you want to print"))
for i in range(n):
    for j in range(i+1):
        print("* ",end=' ') 
    print("\n")    