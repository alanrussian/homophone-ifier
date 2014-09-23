import random
import re

DICTIONARY_FILE = "homophones"

# TODO: Move to utility file and cache dictionary.
def create_dictionary():
  dictionary = {}

  for line in open(DICTIONARY_FILE):
    # If a line contains "(see ...)" then the homophones will be listed elsewhere.
    if "(see " in line:
      continue

    word_strings = [word.strip() for word in line.split(",")]

    words = []
    plural_words = []
    for word_string in word_strings:
      matches = re.findall("([^( ]+) ?(\(-(.+?)\))?", word_string)

      if not matches:
        continue

      # These need to be lower case, but only do this to dictionary key in case the word is an
      # acronym.
      word = matches[0][0]
      plural_word = matches[0][2]

      if plural_word:
        plural_words.append(word + plural_word)

      words.append(word)

    for word in words:
      dictionary[word.lower()] = [x for x in words if x is not word]
    for plural_word in plural_words:
      dictionary[plural_word.lower()] = [x for x in plural_words if x is not plural_word]

  return dictionary

def main():
  dictionary = create_dictionary()

  text = input("Enter some text: ")
  
  # TODO: Handle punctuation.
  words = text.split(" ")

  for i in range(len(words)):
    word = words[i].lower()

    if word in dictionary:
      # Copy first letter capitalization.
      new_word = random.choice(dictionary[word])
      if words[i][0].isupper():
        new_word = new_word[0].upper() + new_word[1:]

      words[i] = new_word

  text = " ".join(words)
  print(text)

main()
