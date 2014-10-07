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
    index = 0 #random.randint(0, len(chains[start_key]))
    next_word = chains[start_key][index]
    random_words = [start_key[0], start_key[1], next_word]
    i = 0

    while next_word != 'the end' and i < 5:
        new_key = (random_words[-2], random_words[-1])
        #print type(new_key)
        #index = random.randint(0, len(chains[new_key])-1)
        #print type(chains[new_key])
        next_word = chains.get(new_key, ['the end'])
        next_word = next_word[0]
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