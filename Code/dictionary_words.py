import random
import sys
from helper import get_random_words

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    number_of_words = int(sys.argv[1]) #get after the file name
    line = get_random_words(number_of_words)
    # print(line)
