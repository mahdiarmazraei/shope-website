# Python program to illustrate
# nested functions
def outerFunction(text):
	t = text
	
	def innerFunction():
		print(t)
	
	innerFunction()
	
if __name__ == '__main__':
	outerFunction('Hey !')
