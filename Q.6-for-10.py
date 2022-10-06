#6. Write a python script to print first N even natural numbers

n=int(input("Enter a number:-"))
for e in range(1,(n+1)*2):
    if e%2==0:
      print(e)