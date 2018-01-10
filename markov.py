"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as contents:  # using content manager to open and auto-close file
        src_str = contents.read()
    return src_str

#print open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
       
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # convert string to list
    # make keys = tuples from list = range(len([::2]))
    # make values =

    corpus = text_string.split()
    corpus.append(None)

    size_of_gram = raw_input('Enter a gram size: ')  # think about wording
    size_of_gram = int(size_of_gram)

    for i in range(len(corpus) - size_of_gram):
        mlist = []
        for j in range(i, i + size_of_gram):
            mlist.append(corpus[j])
        mtuple = tuple(mlist)
        
        new_value_var = corpus[i + size_of_gram]
        if mtuple in chains:
            chains[mtuple].append(new_value_var)
        else:
            chains[mtuple] = [new_value_var]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # add tuple to list as 2 strings
    # infinite loop, break if None
    # random sample a value and append
    # access key for [1,2], random sample a value and append
    # end if key is not in dict

    keys = chains.keys()  # list of tuples
    n = len(keys[0])

    while True:
        random_key = choice(keys)  # selects a tuple
        if random_key[0][0].isupper():
            break

    for initial_append in range(n):
        words.append(random_key[initial_append])  # append tuple to list as strings

    next_value = choice(chains[random_key])  # picks a random sample from the value list in chains dict
    words.append(next_value)

    counter = 1
    while True:
        shift_list = []
        for k in range(counter, counter + n):
            shift_list.append(words[k])
        shift_tuple = tuple(shift_list)

        # shift_key = (words[counter], words[counter + 1])
        if chains[shift_tuple] == [None]:  # why [None] vs None
        # if chains[shift_tuple][0] == None
            break
        another_next_value = choice(chains[shift_tuple])  # explore use of random.sample later
        words.append(another_next_value)
        counter += 1
    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
