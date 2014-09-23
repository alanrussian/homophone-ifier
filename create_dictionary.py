import json
import re
import sys

def create_dictionary(dictionary_file):
  dictionary = {}

  for line in open(dictionary_file):
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
  if len(sys.argv) < 2:
    print("Syntax is \"... {0} <dictionary_file>\"".format(sys.argv[0]))
    sys.exit(1)

  dictionary_file = sys.argv[1]

  dictionary = create_dictionary(dictionary_file)
  print(json.dumps(dictionary))

main()