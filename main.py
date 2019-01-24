#/*=================================================
#=> Function: Practice words by writing repeatedly
#=> Input: File with words to learn
#=> Output: Result for each word 
#=> Author: Roberto Gervacio ~~ Mx ~~
#=> Start Data: 21/01/2019
#=> Last Update: 23/01/2019
#=> Aditional Comments: ---
#===================================================*/

import random

class palabra(object):

	def __init__(self, spanish, english, pronunciation="?"):
		self.spanish = spanish
		self.english = english
		self.spanish_c = 0
		self.english_c = 0
		self.completed = 0
		self.pronunciation = pronunciation

	def is_completed(self):
		return self.completed == 4

	def guess_spanish(self):
		print(self.english)
		print("==> ",end='')
		typed = input()
		if typed == "help!":
			return True
		if "/" in self.spanish:
			deep_search = self.spanish.split("/")
			if typed in deep_search:
				self.spanish_c += 1
				self.completed += 1
			else:
				print("Incorrecto:", typed)
		elif typed == self.spanish:
			self.spanish_c += 1
			self.completed += 1
		else:
			print("Incorrecto:", typed)
		print("Correcto:", self.spanish)
		print("----------------------------------")

	def guess_english(self):
		print(self.spanish)
		print("==> ",end='')
		typed = input()
		if typed == "help!":
			return True
		if typed == self.english:
			self.english_c += 1
			self.completed += 1
		else:
			print("Incorrect:", typed)
		print("Correct:", self.english, "<==>", self.pronunciation)
		print("----------------------------------")

	def get_next_to_guess(self):
		#1 = ingles
		#2 = español
		to_return = random.randint(0,1)
		if to_return == 1:
			if self.english_c < 2:
				return 1
			return 0
		elif to_return == 0:
			if self.spanish_c:
				return 0
			return 1

	def __str__(self):
		return "{} => {} | {}%".format(self.english, self.spanish, self.completed * 25)


def main():

	vocabulary = []

	def read_file():
		try:
			f = open("words.txt", "r")
			text = f.read().split("\n")
			for i in text:
				words = i.split('=')
				if len(words) == 2:
					vocabulary.append(palabra(words[1], words[0]))
				elif len(words) == 3:
					vocabulary.append(palabra(words[1], words[0], words[2]))
		except FileNotFoundError:
			print("No se encuentra el archivo \"words.txt\"")

	def keep_iterating():
		for i in vocabulary:
			if not i.is_completed():
				return True
		return False

	read_file()

	while keep_iterating():

		position = random.randint(1, len(vocabulary)) - 1
		while vocabulary[position].is_completed():
			position = random.randint(1, len(vocabulary)) - 1

		if vocabulary[position].get_next_to_guess() == 1:
			is_help = vocabulary[position].guess_english()
		else:
			is_help = vocabulary[position].guess_spanish()

		if is_help:
			print("++++++++++++++++++++++++")
			for i in vocabulary:
				print(i)
			print("++++++++++++++++++++++++")

	print("You have done!")


if __name__ == "__main__":
	main()
