import random
import os

clear = lambda: os.system('clear')

class palabra(object):

	def __init__(self, spanish, english, note="?"):
		self.spanish = spanish
		self.english = english
		self.spanish_c = 0
		self.english_c = 0
		self.completed = 0
		self.note = note

	def is_completed(self):
		return self.completed == 2

	def alert(self):
		if self.completed == 2:
			print("Completed!!")

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
		if self.note != "?":
			print("Correct:", self.spanish, "<>", self.note)
		else:
			print("Correct:", self.spanish)
		
		self.alert()
		print("--------------------------------")

	def guess_english(self):
		#clear()
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
		if self.note != "?":
			print("Correct:", self.english, "<>", self.note)
		else:
			print("Correct:", self.english)

		alert()
		print("--------------------------------")

	def get_next_to_guess(self):
		#1 = ingles
		#2 = español
		return 2
		# to_return = random.randint(0,1)
		# if to_return == 1:
		# 	if self.english_c < 2:
		# 		return 1
		# 	return 0
		# elif to_return == 0:
		# 	if self.spanish_c:
		# 		return 0
		# 	return 1

	def __str__(self):
		return "{} => {} | {}%".format(self.english, self.spanish, self.completed * 50)


def start_words(file_to_open):

	vocabulary = [] #store objects of Palabra

	def read_file():
		try:
			f = open(file_to_open, "r")
			text = f.read().split("\n")
			for i in text:
				words = i.split('=')
				if len(words) == 2:
					vocabulary.append(palabra(words[1], words[0]))
				elif len(words) == 3:
					vocabulary.append(palabra(words[1], words[0], words[2]))
		except FileNotFoundError:
			print("No se encuentra el archivo \"", file_to_open, "\"")

	def keep_iterating():
		for i in vocabulary:
			if not i.is_completed():
				return True
		return False


	#Main
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
			clear();
			print("++++++++++++++++++++++++")
			for i in vocabulary:
				print(i)
			print("++++++++++++++++++++++++")

	if not keep_iterating():
		print("You have done!")