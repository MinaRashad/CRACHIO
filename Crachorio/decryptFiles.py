import time, os, sys, Transpostion

def transpos():
	print("################################\n##Transpostion file decryptor/encryptor##\n###############################")
	inputFilename = input("Enter the file name:")
	outputFilename = input("Enter the output File name:")
	mode = input("Do you want to (en)crypt or (de)crypt:")
	key = int(input("Enter the Key:"))
	

	if not os.path.exists(inputFilename):
		print("The file %s doesn't exist. Quiting.."%(inputFilename))
		sys.exit()

	if os.path.exists(outputFilename):
		print("This will overwrite the file %s. (C)ontinue or (Q)uit?"%(outputFilename))
		response = input('> ')
		if not response.lower().startswith('c'):
			sys.exit()


	fileObj = open(inputFilename)
	content = fileObj.read()
	fileObj.close()

	print("%scrypting..."%(mode.title()))

	startTime = time.time()

	if mode == "en":
		translated = Transpostion.encryptMessage(key, content)
	elif mode == "de":
		translated = Transpostion.decryptMessage(key, content)
	totalTime = round(time.time() - startTime, 2)
	print("%scrypted. Time: %s seconds"%(mode.title(),totalTime))
	#'w' refers to write mode
	outputFileObj = open(outputFilename, 'w')
	outputFileObj.write(translated)
	outputFileObj.close()

	print("%scrypted %s written ( %s characters)."%(mode.title(),inputFilename,len(content)))
	print("Made file %s" %(outputFilename))

if __name__ == '__main__':
	Transpostion()