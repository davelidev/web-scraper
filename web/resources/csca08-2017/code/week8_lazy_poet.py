import random

# the number of words to generate
TEXT_LENGTH = 50

'''A cool program to generate fake text based on some training text.'''


def add_to_dict(word_to_nexts, word, next_word):
    ''' (dict of {str: set of str}, str, str) -> NoneType

    Update word_to_nexts so that word maps to a set containing
    next_word

    >>> my_dict = {'one':{'day', 'two'}, 'a':{'dog', 'day'}}
    >>> add_to_dict(my_dict, 'one', 'time')
    >>> my_dict == {'one':{'day', 'two', 'time'}, 'a':{'dog', 'day'}}
    True

    '''
    # if word is a key in the dictonary
    if(word in word_to_nexts):
        # get the set of possibl next words
        next_word_set = word_to_nexts[word]
        # add next_word into that set
        next_word_set.add(next_word)
    # if word isn't already a key in the dictionary
    else:
        # we'll map word to a new set containing next_word
        word_to_nexts[word] = {next_word}


def build_dictionary(training_file):
    '''(io.TextIOWrapper) -> dict of {str : set of str}

    Return a new dictionary where each key is a word from training_file
    and each value is the set of words that follow that word in
    training_file.
    '''

    # start with an empty dictionary
    word_to_nexts = {}
    # read the whole file into one large string, then split the string
    # into one large list
    word_list = training_file.read().split()

    # for every word in the file, add the word and next_word to the dictionary
    # note that our loop needs to stop at the 2nd to last item in the list,
    # as we always need a "next_word"
    for i in range(0, len(word_list) - 1):
        add_to_dict(word_to_nexts, word_list[i], word_list[i + 1])

    return word_to_nexts


def choose_next_word(word_to_nexts, word):
    ''' (dict of {str: set of str}, str) -> str

    Return a randomly chosen next word to follow word based on
    the possibilities in the word_to_nexts dictionary.
    '''

    # if the word exists in our dictionary
    if word in word_to_nexts:
        # get the set of all possible next words we can return
        next_word_set = word_to_nexts[word]
        # return a random element from that set
        ret = random.choice(list(next_word_set))
    else:
        # if word isn't a key in the dictionary, just return a random
        # word that is a key
        # random.choice only works on lists, and keys returns a set, so we
        # have to cast it.
        full_word_list = list(word_to_nexts.keys())
        ret = random.choice(full_word_list)

    return ret


def generate_text(word_to_nexts, num_words):
    '''(dict of {str : set of str}, int) -> str

    Return a string of num_words words that is generated based on the word
    occurrence info in word_to_nexts.
    '''

    # start with a random word from our dictionary
    # word = random.choice(list(word_to_nexts.keys()))
    # actually... we don't need to do that, all we need to do is start
    # with somethign that isn't a key in our dictionary
    # and choose_next_word will pick a random starting word anyway
    word = ''

    # we'll build up "text" as our return variable
    text = ''

    # create one word at a time, adding to text, until we reach
    # the allocated number of words
    for i in range(num_words):
        next_word = choose_next_word(word_to_nexts, word)
        text = text + ' ' + next_word
        word = next_word

    return text


if(__name__ == "__main__"):
    # prompt the user for a file name, open it and keep the file handle
    my_file = open(input("Which training file? "))

    # Scan the training text and build a dictionary storing
    # word occurrence information.
    word_to_nexts = build_dictionary(my_file)
    # we're done with the file now, so we can close it
    my_file.close()

    # Generate and print a new text with the specified number of
    # words using words from the word coccurrence dictionary.
    new_text = generate_text(word_to_nexts, TEXT_LENGTH)
    print(new_text)
