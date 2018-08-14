import pyperclip

##############
# msg = "Hello world!"
# key = 3
# mode = 'encrypt'
# #ALL  symbols that can be encrypted;
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# translate = ""
# #capitalize the letters


def caesarAligarthom():
	print("#####################Caesare Cypher########################")
	print("Enter a message:")
	msg = input()

	print("Do you want to decrypt or encrypt?\n *type 'en' to encrypt or 'de' to decrypt")
	
	mode = input()

	print("What is the key? (0 - 26)")

	key = int(input())
	#ALL  symbols that can be encrypted;
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	translate = ""
	#capitalize the letters
	msg = msg.upper();


	for symbol in msg:
		if symbol in letters:
			num = letters.find(symbol)
			if mode == 'en':
				num = num + key
			elif mode == "de":
				num = num - key

			#handle if number in larger than length of letters or less than zero

			if num >= len(letters):
				num = num - len(letters)
			elif num < 0:
				num = num + len(letters)

			translate = translate + letters[num]
		else:
			translate = translate + symbol;

	print(translate)
	pyperclip.copy(translate)
	if __name__ == '__main__':
		caesarAligarthom()
if __name__ == '__main__':
	caesarAligarthom()
####################333