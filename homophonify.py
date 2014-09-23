import json
import os.path
import random
import re

DICTIONARY_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "homophones.json")

def main():
  dictionary = json.load(open(DICTIONARY_FILE))

  text = input("Enter some text: ")

  words = text.split(" ")

  for i in range(len(words)):
    word_extraction = "^([\"\'‘’“”<>]?)((\w|[-'])+?)([.,?!]?[\'\"‘’“”<>]?[.,?!]?)$"
    matches = re.findall(word_extraction, words[i].lower())
    if not matches:
      continue

    prefix = matches[0][0]
    word = matches[0][1]
    suffix = matches[0][3]

    if word in dictionary:
      # Copy first letter capitalization.
      new_word = random.choice(dictionary[word])
      if words[i][0].isupper():
        new_word = new_word[0].upper() + new_word[1:]

      words[i] = prefix + new_word + suffix

  text = " ".join(words)
  print(text)

main()
