#/*=================================================
#=> Function: Practice words by writing repeatedly
#=> Input: Files with words to learn in appropriate format
#=> Output: varied
#=> Author: Roberto Gervacio ~~ Mx ~~
#=> Start Data: 21/01/2019
#=> Last Update: 17/04/2019
#=> Aditional Comments: ---
#===================================================*/
import os
from shutil import copyfile
from reviewer import start_words, start_expressions

def main():
	clear = lambda: os.system('clear')

	def menu():
		print("#########################")
		print("######## WELCOME ########")
		print("#########################")
		print(" 1 - General Words | use the file words.txt > has many words")
		print(" 2 - Similar Words | use the file similar.txt > has similars words")
		print(" 3 - Expressions   | use the file expressions.txt > common expressions")
		print(" 4 - Collocations  | use the file collocations.txt > famaous collocations")
		print(" 5 - Recent        | use new words lastest_words.txt > has many words")
		print(" 6 - Go back")
		print("Choose: ", end="")
	
	def set_up_enviroment():
		print("Copying files... ")
		print("Copying words.txt")
		copyfile("/home/" + os.getlogin() + "/Dropbox/main/words/words.txt", os.getcwd() + "/words.txt")
		print("Copying similar.txt")
		copyfile("/home/" + os.getlogin() + "/Dropbox/main/words/similar.txt", os.getcwd() + "/similar.txt")
		print("Copying expressions.txt")
		copyfile("/home/" + os.getlogin() + "/Dropbox/main/words/expressions.txt", os.getcwd() + "/expressions.txt")
		print("Copying collocations.txt")
		copyfile("/home/" + os.getlogin() + "/Dropbox/main/words/collocations.txt", os.getcwd() + "/collocations.txt")
		print("Copying lastest_words.txt")
		copyfile("/home/" + os.getlogin() + "/Dropbox/main/words/lastest_words.txt", os.getcwd() + "/lastest_words.txt")
	
	def clear_enviroment():
		os.remove("words.txt")
		os.remove("similar.txt")
		os.remove("expressions.txt")
		os.remove("collocations.txt")
		os.remove("lastest_words.txt")

	#main
	clear()
	set_up_enviroment()
	option = "-1"

	while(option != "6"):
		menu()
		option = input();
		clear()
		if(option == "1"):
			start_words("words.txt")
		elif(option == "2"):
			start_words("similar.txt")
		elif(option == "3"):
			start_expressions()
		elif(option == "4"):
			start_words("collocations.txt")
		elif(option == "5"):
			start_words("lastest_words.txt")
		elif(option == "6"):
			print("You will pass the final exam! no worry =)")
		else:
			print("Are you stupid?, come on choose something valid")
	clear_enviroment()


if __name__ == "__main__":
	main()
