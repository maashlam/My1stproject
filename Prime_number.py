a=int(input("Type a number to check if prime or not"))
for i in range(2,a): #Range should not start from 1 as every number is divisible by 1
      if  a % i == 0:
        print(a, " is not a prime number")
        break
else:
    print(a, "is  a prime number") #Correct code may be an interview question