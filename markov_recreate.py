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

	return dictionary

def create_random_text(dictionary):
	random_words_list = []
	#select 'random' key
	random_key = random.sample(dictionary.keys(), 1)
	key_tuple = random_key[0]
	# print key_tuple

	# LOOP

	#select 'random' list element in list associated with key
	word_list = dictionary[key_tuple]
	random_index = random.randint(0, len(word_list)-1) # why is it -1?
	next_word = word_list[random_index]
	random_words_list.append(next_word)
	print random_words_list

	# set new key to be the last words of random_words_list
	# new_key = (random_words_list[-1])
	# print new_key

def main():
	script, filename = argv

	dictionary = create_dictionary(filename)
	random_text = create_random_text(dictionary)
	# print random_text


if __name__ == "__main__":
	main()