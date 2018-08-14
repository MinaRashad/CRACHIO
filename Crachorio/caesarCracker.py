
def crack():
	print("#####################################\nTo leave press (ctrl + c)\n#############Caesare cracker############")
	msg = input("Enter Encrypted message(Capitalized):")

	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	msg.upper();
	for key in range(len(letters)):

		translate = ''

		for symbol in msg:
			if symbol in letters:
				num = letters.find(symbol)
				num = num - key

				#handle if number in larger than length of letters or less than zero

				if num < 0:
					num = num + len(letters)

				translate = translate + letters[num]
			else:
				translate = translate + symbol;

		print("Key %s: %s " % (key,translate))
		
	if __name__ == '__main__':
		crack()
if __name__ == '__main__':
	crack()
