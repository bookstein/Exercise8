from sys import argv
import random
import string

def create_dictionary(filename):
	dictionary = {}

	f = open(filename)
	text = f.read()
	f.close()

	# create list of words separated by spaces
	word_list = text.strip().split()

	# gets word at index i,
	# then associates it with words at positions +1 and +2
	for index in range(len(word_list)-2):
		# the dict key is a tuple (word0, word1)
		# setdefault checks if key exists already,
		# returns assoc value if yes, sets default to [] if no
		# appends to value (list) or to []
		dictionary.setdefault(
			(word_list[index], word_list[index+1]),[]).append(word_list[index+2])

	# print dictionary



def main():
script, filename = argv

create_dictionary(filename)
	random_text = create_random_text(dictionary)
	print random_text


if __name__ == "__main__":
	main()