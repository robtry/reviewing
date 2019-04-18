import random, re
import os
clear = lambda: os.system('clear')

class expresion(object):

	def __init__(self, english, comment):
		self.missing = re.findall(r'-.*-', english)[0].replace("-", "");
		self.english = re.sub('-' + self.missing + '-', "_____", english, 1)
		self.completed = 0
		self.comment = comment

	def is_completed(self):
		return self.completed == 4
	
	def ask(self):
		print(self.english, "|", self.comment)
		print("==> ",end='')
		typed = input()
		if typed == "help!":
			return True
		if typed == self.missing:
			self.completed += 1
		else:
			print("Incorrect:", typed)
		print("Correct:", self.english, "=>", self.missing, "|", self.comment)
		print("--------------------------------")

	def __str__(self):
		return "{} => {} | {} <> {}%".format(self.english, self.missing, self.comment, self.completed * 25)

def start_expressions():
	vocabulary = []

	def read_file():
		try:
			f = open("expressions.txt", "r")
			text = f.read().split("\n")
			for i in text:
				words = i.split('=')
				if len(words) == 2:
					vocabulary.append(expresion(words[0], words[1]))
		except FileNotFoundError:
			print("No se encuentra el archivo \"expressions.txt\"")
	
	def keep_iterating():
		for i in vocabulary:
			if not i.is_completed():
				return True
		return False
	

	#main
	read_file()

	while keep_iterating():
		position = random.randint(1, len(vocabulary)) - 1
		while vocabulary[position].is_completed():
			position = random.randint(1, len(vocabulary)) - 1
		
		if vocabulary[position].ask():
			clear();
			print("++++++++++++++++++++++++")
			for i in vocabulary:
				print(i)
			print("++++++++++++++++++++++++")
		
	
	if not keep_iterating():
		print("You have done!")