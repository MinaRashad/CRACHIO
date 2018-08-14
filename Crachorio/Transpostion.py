import math, pyperclip

def main():
	msg = input("################\nTo leave press ctrl + c \n ##Transpostion Encryption##\n Enter your message: \n")

	mode = input("Do you want to encrypt or decrypt\ntype 'en' to encrypt or 'de' to decrypt:\n")
	
	key = int(input("Enter your key (recommended (2 - %s) ):" %(math.floor(len(msg)/2))))

	if mode == "en":
		text = encryptMessage(key, msg)
	elif mode == "de":
		text = decryptMessage(key, msg)

	

	print(text + "|")

	pyperclip.copy(text)

	if __name__ == '__main__':
		main()
def encryptMessage(key, msg):
	#Create  a variable to hold an array of columns because
	#the number of collums is equal to the key
	cyperText = ['']* key
	#now we create a for loop to go through every column
	for col in range(key):
		pointer = col
		#the pointer will go through every element in the column
		while pointer < len(msg):
			cyperText[col] += msg[pointer]
			#that will choose next element in the column
			pointer += key
	
	return ''.join(cyperText)



	###############Example: key= 3 msg = hello############
	#########       H       #        E        #     L    #
	#index###		0		#		 1		  #		2	 #
	######################################################
	#########       L       #        L        #     O    #
	#index###		3		#		 4		  #		5	 #
	######################################################

	#first col index msg [0] , msg [3]
	#second col 	 msg [1] , msg [4]
	#third			 msg [2] , msg [5]
	#which is programmed as msg[the index of the col + key*it's number in the row]
	#in pointer += key e.g. key = 3
	#pointer = 0 then 3 then 6 then 9 and so on 
	#that's key * number of row

def decryptMessage(key, msg):
	numOfcolumns = math.ceil(len(msg) / key)
	numOfRows = key
	numOfShadedBoxes = (numOfcolumns * numOfRows) - len(msg)
	plainText = [''] * numOfcolumns

	col = 0
	row = 0

	for symbol in msg:
		plainText[col] += symbol		#print(plainText)
		col += 1 

		if (col == numOfcolumns) or (col == numOfcolumns - 1 and row >= numOfRows - numOfShadedBoxes):
			
			col = 0
			#row += 1

	return ''.join(plainText)


if __name__ == '__main__':
	main()