#!/usr/bin/env python

import sys
import random
import string
import os
import twitter

word_choices = {}

def read_in_files(directory):

    files = os.listdir(directory)
    for textfile in files:
        make_chains(directory, textfile)


# read_in_files("sourcetext")


def make_chains(directory, corpus):
    
    # word_choices = {}

    text = open(directory + "/" + corpus)
    start_text = text.read()
    text.close()

    words = start_text.strip().split()

    #print words

    for i in range(len(words)-2):
        word_choices.setdefault(
            (words[i], words[i+1]), []).append(words[i+2])

    # print word_choices

    # return word_choices

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    enders = '.?!"\''
    starters = string.ascii_uppercase


    
    next_word = ''

    key_string = " "

    while key_string[0] not in starters:
        the_key = random.sample(chains, 1)
        key_string = the_key[0][0]
        # the_key = the_key[0]
        # print key_string

    # the_key = random.sample(chains, 1)
    the_key = the_key[0]
    random_words = [the_key[0], the_key[1]]

    num_chars = len(" ".join(random_words))

    while next_word != 'the end' and num_chars < 130:

        get_words = chains.get(the_key, ['the end'])

        index = random.randint(0, len(get_words)-1)
        
        next_word = get_words[index]
        random_words.append(next_word)

        if next_word[-1] in enders:
            break
        new_key = (random_words[-2], random_words[-1])
        the_key = new_key

        num_chars += (len(next_word) + 1)
        print num_chars

    random_text = " ".join(random_words)
    if random_text[-1] not in enders:
        random_text = random_text + '.'
    return random_text

def main():
    script, directory = sys.argv

    read_in_files(directory)
    random_text = make_text(word_choices)

    api = twitter.Api(consumer_key=os.environ.get('TWITTER_API_KEY'),
                     consumer_secret=os.environ.get('TWITTER_SECRET_KEY'),
                     access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
                     access_token_secret=os.environ.get('TWITTER_SECRET_TOKEN'))

    # api.PostUpdate(random_text)
    print random_text

if __name__ == "__main__":
    main()