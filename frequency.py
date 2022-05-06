# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Word Frequency
#
# NAME:         Julio Arias
# ASSIGNMENT:   Technical HW: Arrays & Maps

from operator import itemgetter
import string

import json

# Create a function word_frequencies that takes
# a string filename as a parameter and returns a
# dictionary mapping each word in the text file
# to the total number of times it occurs. All
# letters should be treated as lower case, and both
# punctuation and numbers should be ignored.
# Letters separated by apostrophes should be left together.
# Your solution may use string & file functions.
# Hint: see https://www.techiedelight.com/remove-punctuations-string-python/

def word_frequencies(filename):
  d = {}

  #These are the valis characters
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'’ " 
  
  characters = []
  with open(filename, 'r', encoding='UTF-8') as f:
    for char in f.read():
      #Looks for characters and if not found makes it a space
          characters.append(' ') if char not in chars else characters.append(char) 
 
  info = ''.join(characters)
  info = info.lower()
  #Apostrophes must be deleted instead of made into a space
  info = info.translate(str.maketrans("", "","'’"))

  #Uses accumulator to put letter in until it finds a space
  word = ''
  accumulator = ''
  for letter in info:
    accumulator += letter
    if letter == ' ':
      word = accumulator
      accumulator = ''
      word = word.translate(str.maketrans("", "", " "))
      if word not in d:
        if word != '':
          d[word] = 0
      if word != '':
        d[word] += 1
  word = accumulator
  

  #runs code again to look for skipped spaces
  if word not in d:
    if word != '':
      d[word] = 0
  if word != '':
      d[word] += 1
  return d

def print_map_by_value(map):
    for k, v in sorted(map.items(), key=itemgetter(1), reverse=True):
        print("%6d %s" % (v, k) )


def main():
    # files = ["pytest", "turing", "austen"]
    files = ["austen"]
    for f in files:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/"+f+".txt"))

# Don't run main on import
if __name__ == "__main__":
    main()
