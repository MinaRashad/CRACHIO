import time, os, sys, reverseCypher, caesar
import Transpostion, decryptFiles, caesarCracker
import decryptFiles
def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	print("\n\nMain Menu: \n 1.Crack \n 2.Encrypt\\Decrypt\n 3.file operations")

	respond = input(">> ")

	if respond == '1':
		crackMenu()
	elif respond == '2':
		encryptDecrypt()
	elif respond == '3':
		files()

def files():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	print("\n\nFiles operations: \n 0.Main Menu \n 1.Transposition Cypher")

	respond = input(">> ")

	if respond == '0':
		main()
	if respond == '1':
		DecryptFile()

def crackMenu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	print("\n\nCrack Menu: \n 0.Main Menu  \n 1.Caesar Cypher \n 2.Transposition Cypher")

	respond = input(">> ")

	if respond == '0':
		main()
	elif respond == '1':
		caesarCrack()
	elif respond == '2':
		TransCrack()
	# elif respond == '3':
	# 	transpostionCrack()
################
def encryptDecrypt():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	print("\n\nCypher Menu: \n 0.Main Menu \n 1.Reverse Cypher \n 2.Caesar Cypher\n 3.Transposition Cypher")

	respond = input(">> ")

	if respond == '0':
		main()
	elif respond == '1':
		reversecypher()
	elif respond == '2':
		caesarcypher()
	elif respond == '3':
		transpostioncypher()

def reversecypher():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	print("\n\nReverse Cypher :\n *decrypting and encrypting are the same")

	msg = input("Enter You Message:")
	print("Tanslated Message : \n %s " %(reverseCypher.reverse(msg)))
	x =input("Press Enter To Continue")
	encryptDecrypt()
	
def caesarcypher():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	print("\n\nCaesar Cypher :\n *decrypting and encrypting are the same")
	caesar.caesarAligarthom()
	x =input("Press Enter To Continue")
	
	encryptDecrypt()

def transpostioncypher():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	Transpostion.main()
	x =input("Press Enter To Continue")
	encryptDecrypt()

################

def caesarCrack():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")
	caesarCracker.crack()
	x =input("Press Enter To Continue")
	crackMenu()

def DecryptFile():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("################################################################")
	print("###################### C R A C H O R I O #######################")

	decryptFiles.transpos()

	x =input("Press Enter To Continue")
	crackMenu()

if __name__ == '__main__':
	main()