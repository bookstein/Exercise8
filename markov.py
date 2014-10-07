#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    
    word_choices = {}

    text = open(corpus)
    start_text = text.read()
    text.close()

    words = start_text.strip().split()

    #print words

    for i in range(len(words)-2):
        word_choices.setdefault((words[i], words[i+1]), [words[i+2]]).append(words[i+2])

    # print word_choices

    return word_choices

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""


    i = 0
    next_word = ''

    while next_word != 'the end' and i < 5:
        the_key = random.sample(chains, 1)
        the_key = the_key[0]
        get_words = chains.get(the_key, ['the end'])
        print get_words
        index = random.randint(0, len(get_words)-1)
        print index
        #print start_key, index
        next_word = get_words[index]
        # print next_word
        random_words = [the_key[0], the_key[1], next_word]
        new_key = (random_words[-2], random_words[-1])
        the_key = new_key
        random_words.append(next_word)
        i += 1

    random_text = " ".join(random_words)
    return random_text

    #value = random.sample(chains[start_key], 1)
    #print start_key, type(start_key)
    #print chains[start_key], type(start_key)
    # print start_key, next_word, random_text

    # return "Here's some random text."

def main():
    args = sys.argv

    script, filename = args

    chain_dict = make_chains(filename)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()