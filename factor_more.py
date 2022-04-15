import math

number = int(input("Please insert a number: "))

divisor = 2

divisible = False
remainder = True

number_check = False
divisor_check = False

prime = False

def isprime(num): # checks if number is prime
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def check_no_remainder():
    if new_number == int(new_number): # checks too see if new number is an intiger 
        for i in range(number):
            if new_number % (i+1) == 0 and divisor % (i+1) == 0:
                remainder = True

while divisor != (int(number))**2 - 1 and divisible == False:
	new_number = number/divisor
	check_no_remainder()
	print("...")
	divisor = divisor + 1
	if remainder == True:
	    number_check = isprime(new_number)
	    divisor_check = isprime(divisor)
	if number_check == True and divisor_check == True:
	    print(number, "is divisible by", new_number, "and", divisor, sep=" ")
	    number_check = False
	    divisor_check = False
	    divisble = True
	
if number_check == False and divisor_check == False:
    print(number, "is not a semi-prime.", sep=" ")
    quit()
quit()
