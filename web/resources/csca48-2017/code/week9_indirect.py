# A fun little example of mutual recursion. Presented in its raw form with
# poorly chosen words and no comments.

import random
noun_list = ["apple", "bear", "cat", "dog", "egg", "fish", "goat", "head",
             "igloo", "junk", "kid", "laser", "monkey", "necktie",
             "ostrich", "penguin", "queen", "racecar", "steak", "truck",
             "ukulele", "van", "window", "x-ray", "yo-yo", "zoo"]
verb_list = ["ate", "bit", "caught", "dared", "egged", "fought", "goaded",
             "hated", "irked", "jammed", "kicked", "loved", "mocked",
             "nuzzled", "opened", "poked", "quoted", "roasted", "smooched",
             "tamed"]
det_list = ["the", "a", "my", "your"]
pronoun_list = ["blue", "cool", "dirty", "fancy", "green", "hot", "juicy",
                "lovely", "massive", "new", "old", "poor", "quirky", "steel",
                "violent", "wax"]
prep_list = ["with", "in", "beside", "near"]


def noun():
    return random.choice(noun_list)


def verb():
    return random.choice(verb_list)


def det():
    return random.choice(det_list)


def pronoun():
    return random.choice(pronoun_list)


def prep():
    return random.choice(prep_list)


def prep_phrase():
    return prep() + " " + noun_phrase()


def noun_phrase():
    ret = det() + " " + pronoun() + " " + noun()
    if(random.random() > 0.5):
        ret += " " + prep_phrase()
    return ret


def verb_phrase():
    return verb() + " " + noun_phrase()


def sentence():
    return noun_phrase() + " " + verb_phrase()

print(sentence())
