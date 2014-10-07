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

    start_key = random.sample(chains, 1)
    start_key = start_key[0]
    index = random.randint(0, len(chains[start_key]))
    next_word = chains[start_key][index]
    #value = random.sample(chains[start_key], 1)
    #print start_key, type(start_key)
    #print chains[start_key], type(start_key)
    print start_key, next_word

    # return "Here's some random text."

def main():
    args = sys.argv

    script, filename = args

    chain_dict = make_chains(filename)
    random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()