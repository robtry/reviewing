import random, re

class expresion(object):

	def __init__(self, complete, missing, comment="?"):
		self.complete = re.sub(missing, "___",  complete, 1)
		self.missing = missing
		self.completed = 0
		self.comment = comment


	def is_completed(self):
		return self.completed == 4

	def __str__(self):
		return "{} => {}%".format(self.complete, self.missing)

def start_expressions():

	try:
		f = open("expressions.txt", "r")
		text = f.read().split("\n")
		for i in text:
			words = i.split('=')
			if len(words) == 2:
				print(expresion(words[0], words[1]))
	except FileNotFoundError:
		print("No se encuentra el archivo \"expressions.txt\"")