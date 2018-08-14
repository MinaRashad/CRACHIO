#reverse cypher
def start():
	print("To close the program press  'ctrl + c'\n ==========REVERSE CYPHER===============")
	print("Enter to reverse cypher or unreverse it.")

	print(reverse(input()));



def reverse(msg):	
	translatedMsg = ""
	i = len(msg) -1
	while i >= 0:
		translatedMsg = translatedMsg + msg[i]
		i = i - 1;

	#print(translatedMsg);
	return translatedMsg
	if __name__ == '__main__':
		start()
if __name__ == '__main__':
	start()