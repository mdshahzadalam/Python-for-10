#5. Write a python script to print first N odd natural numbers in reverse order

n=int(input("Enter a number:-"))
for e in range(1,(n)*2):
    if e%2!=0:
      print(e)