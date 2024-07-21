#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    
    # Open the file and read all words into a list
    with open(filename, 'r') as file:
        words = file.read().split()

    # Initialize an empty dictionary to hold the mimic dictionary
    mimic_dict = {}
    # Initialize the previous word as an empty string
    prev_word = ''
    
    # Iterate through each word in the list of words
    for word in words:
        # If the previous word is not already in the dictionary, add it with an empty list
        if prev_word not in mimic_dict:
            mimic_dict[prev_word] = []
        # Append the current word to the list of words that follow the previous word
        mimic_dict[prev_word].append(word)
        # Update the previous word to the current word
        prev_word = word

    # Return the completed mimic dictionary
    return mimic_dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    
    # Import the random module
    import random
    
    # Print 200 words
    for _ in range(200):
        # Print the current word followed by a space
        print(word, end=' ')
        # Get the list of next words that follow the current word from the mimic dictionary
        next_words = mimic_dict.get(word)
        # If there are no next words (word not in dictionary), use the list of words that follow the empty string
        if not next_words:
            next_words = mimic_dict['']
        # Choose a random word from the list of next words to be the next word to print
        word = random.choice(next_words)
    # Return from the function
    return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
