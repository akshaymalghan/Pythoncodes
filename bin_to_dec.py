import math 




def bin_to_dec(num):

	string=str(num)
	length=len(string)
	num1=0

	for i in range(length):
		
		num1=int(string[length-i-1])*pow(2,i)+num1
	print(num1)


bin_to_dec(int(input('Enter the binary number ')))
