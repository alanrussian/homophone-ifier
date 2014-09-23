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
    matches = re.findall(word_extraction, words[i])
    if not matches:
      continue

    prefix = matches[0][0]
    word = matches[0][1]
    suffix = matches[0][3]

    word_safe = word.lower()
    if word_safe in dictionary:
      # Copy first letter capitalization.
      # TODO: Handle case of "I".
      new_word = random.choice(dictionary[word_safe])
      if word[0].isupper():
        new_word = new_word[0].upper() + new_word[1:]

      words[i] = prefix + new_word + suffix

  text = " ".join(words)
  print(text)

main()
