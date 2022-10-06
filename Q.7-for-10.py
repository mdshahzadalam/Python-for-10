#7. Write a python script to print first N even natural numbers in reverse order

n=int(input("Enter a number:-"))
for e in range(1,(n+1)*2):
    if e%2==0:
      print(2*(n+1)-e)