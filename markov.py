#!/usr/bin/env python

import sys
import random
import string
import os
import twitter

word_choices = {}

def read_in_files(directory, n):
    """Loops through all the files in the directory, and passes them to make_chains."""

    files = os.listdir(directory)
    for textfile in files:
        make_chains(directory, textfile, n)



def make_chains(directory, corpus, n):
    """Reads the file corpus and creates markov chain using n-grams"""

    text = open(directory + "/" + corpus)
    start_text = text.read()
    text.close()

    #list of all words in corpus text
    words = start_text.strip().split()

    #loops through list of words in text, stopping n words from the end
    for i in range(len(words)-n):
        # initialize start_key as an empty tuple
        start_key = ()
        # j is a counter which goes from 0 to n
        for j in range(n):
            # finds the next word and creates a new key by concatenating that word to start_key
            start_key = start_key + (words[i+j],)
        #checks if start_key is already in the dictionary word_choices
        #if the start_key is not there, returns and sets the value to an empty array
        #appends the word that follows the start_key to the value
        word_choices.setdefault(start_key, []).append(words[i+n])


def make_text(chains, n):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # sets variables for ending punctuation and all uppercase letters
    enders = '.?!"\''
    starters = string.ascii_uppercase

    #initializes empty string for the next word in the text,
    # initializes an empty string for the key's first word, and
    # initializes and empty list which will hold the random text
    next_word = ''
    key_string = " "
    random_words = []

    # keeps picking a starter key until it finds one that starts with a capital letter
    while key_string[0] not in starters:
        # random.sample returns a list with tuple inside it
        the_key = random.sample(chains, 1)
        # sets key_string to the first letter of the first word in the tuple the_key
        key_string = the_key[0][0]

    # the_key is now the tuple with n words in it (takes tuple out of list)
    the_key = the_key[0]

    # puts the words in the first key in the list random words
    for word in the_key:
        random_words.append(word)

    # initializes num_chars as the number of characters plus spaces in the words in random_words
    num_chars = len(" ".join(random_words))

    # this loop constructs a list of words that will contain approximately 130 characters, including spaces
    while next_word != 'the end' and num_chars < 130:
        # set the return value from hashing the_key (a list of words). If key does not exist, returns "the end"
        get_words = chains.get(the_key, ['the end'])

        # chooses a random integer less than length of get_words
        index = random.randint(0, len(get_words)-1)

        # use the random index number to choose from the list of possible next words
        next_word = get_words[index]
        random_words.append(next_word)

        # if the last character in next_word is punctuation - break while loop
        if next_word[-1] in enders:
            break

        # initialize a new tuple
        new_key = ()
        # loops over the last n values in random_words
        for word in random_words[-n:]:
            # concatenates each new word to new_key
            new_key = new_key + (word,)
        # set the next key to new key
        the_key = new_key

        # increment num_chars by the word just added, +1 for space
        num_chars += (len(next_word) + 1)

    # takes the list of random_words and joins them using " ", which creates one long string of random text
    random_text = " ".join(random_words)
    # checks if there is punctuation at the end of random_text, and adds a period of not.
    if random_text[-1] not in enders:
        random_text = random_text + '.'
    return random_text

def main():
    # expects user to input script name, directory for the source text, and the "n" for n-grams
    script, directory, n = sys.argv
    n = int(n)

    #set twitter api keys and tokens
    api = twitter.Api(consumer_key=os.environ.get('TWITTER_API_KEY'),
                     consumer_secret=os.environ.get('TWITTER_SECRET_KEY'),
                     access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
                     access_token_secret=os.environ.get('TWITTER_SECRET_TOKEN'))

    while True:
        # pass the file to read files
        read_in_files(directory, n)
        # pass everything to make text so we can random_text
        random_text = make_text(word_choices, n)

        # post random text to twitter
        print random_text
        print "\n\n"

        print "post this to twitter? (y/n)"
        answer = raw_input()
        if answer == 'y':
            api.PostUpdate(random_text)

        print "run again? (y/n)"
        answer2 = raw_input()
        if answer2 == 'y':
            continue
        elif answer2 == "n":
            break
        else:
            print "I only understand y or n! Quitting."
            break

if __name__ == "__main__":
    main()