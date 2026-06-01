Num=int(input("Enter a Number:"))
# PRIME NUMBERR OR NOT
if Num < 1 :
    print("Not a prime number")
else:
    for i in range(2,int(Num**0.5)+1):
        if Num % i == 0:
            print("The number is not a prime number")
            break
        else:
            print("The number is prime")
            break
            
#ODD OR EVEN

if Num % 2 == 0 :
    print("The number is even")
else:
    print("The number is odd")
