#/*=================================================
#=> Function: Practice words by writing repeatedly
#=> Input: File with words to learn
#=> Output: Result for each word 
#=> Author: Roberto Gervacio ~~ Mx ~~
#=> Start Data: 21/01/2019
#=> Last Update: 
#=> Aditional Comments: ---
#===================================================*/

def main():
	try:
		f = open("words.txt", "r")
		text = f.read().split("\n")
		for i in text:
			print(i)
	except FileNotFoundError:
		print("No se encuentra el archivo \"words.txt\"")

if __name__ == "__main__":
	main()