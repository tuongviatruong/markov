"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents



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
    words = input_text.split()
    print words
    #creates dictionary
    chains = {}
  

    #iterates over str(words)
    for i in range(len(words)-2):
        # chains.get(key) returns value or None 
        #if dict empty, returns None and else statement initiated
        # if the key exists, returns the value
        # key = (words[i], words[i +1])
        
        ##checks to see if key already has a value
        ##if so, add value
        ## Else, add key and value to list
        if chains.get((words[i], words[i + 1])):
            #there is a key that exist, its value is returned; append value to key
            chains.get((words[i], words[i + 1])).append(words[i + 2])

        # if dict is empty or key not exist, create the key=value     
        else:
            chains[(words[i], words[i + 1])] = [words[i + 2]]

        #rememberd: chains.get(key) returns value, and holds type; value is list for this function 

   
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
