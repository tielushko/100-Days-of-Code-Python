#Write your code below this line 👇

def prime_checker(number):
    isPrime = True
    #checking for divisions from 2 to number - 1, because if it is divisible by any of those without remainder, it is not prime
    
    for divisor in range(2, number):
        if number % divisor == 0:
            isPrime = False

    if number == 1:
        isPrime = False
        
    if isPrime:
        print("The number entered is a prime number")
    else:
        print("The number entered is NOT a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



