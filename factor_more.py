import math

number = int(input("Please insert a number: "))

divisor = 2

end_number_check = number - 1

divisible = False
remainder = True

number_check = False
divisor_check = False

prime = False

def isprime(n):
	if n % 2 == 1:
		return True
	else:
		return False
    

def check_no_remainder():
    if new_number/int(new_number) == 1: # checks too see if new number is an integer 
        remainder = True

while divisible == False:
	new_number = number/divisor
	check_no_remainder()
	if remainder == True:
	    number_check = isprime(round(new_number))
	    divisor_check = isprime(round(divisor))
	if new_number == int(new_number) and divisor == int(divisor):
	    print(number, "is divisible by", number/divisor, "and", divisor, sep=" ")
	    quit()
	if divisor == end_number_check:
		print(number, "is not a semi-prime.", sep=" ")
		quit()
	divisor += 1
quit()
