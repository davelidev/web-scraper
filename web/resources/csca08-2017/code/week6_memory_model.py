#  Try working through all of these examples on paper, drawing out the memory
#  model as you go. Then check in pythontutor to see if you were correct.
#  You'll thank me for it in the long run


def mutate(input_list):
    input_list[0] = 99

# let's start with a few simple assignments
x = 7
y = 7
x = 8

# now adding in lists
x = [1, 2, 3]
y = [1, 2, 3]
x[0] = 99

# trying mutation with functions (this is a good one to play around with
# a bit more. try messing with mutate, and see what it does)
x = [1, 2, 3]
mutate(x)

# a more complicated list (but notice that the model doesn't get
# any more difficult)
x = [[1, 2, 3], 1, [3, 2, 1]]
x[2][0] = 99

# y = x doesn't seem to do anything unusual with immutable types
x = 7
y = x
x = 8

# but when we have mutable types, it create an alias (again, seems
# strange to humans but makes perfect sense within the memory model
x = [1, 2, 3]
y = x
x[0] = 99

# let's try making a clone
x = [1, 2, 3]
y = x[:]
x[0] = 99

# but remember... cloning only makes a shallow copy.
# let's try a more complicated example. If you can do this,
# then you can really call yourself a master of the memory model.
x = [[1, 2, 3], [3, 2, 1], [1, 2]]
y = x[:]
x[1][2] = 99

# and here are a few randomly generated strings. Remember that Python
# doesn't care about the meaning of strings, so you should just write
# these down and not worry about the meaning. (If there are any
# subliminal messages in there, it's purely coincidence)
x = "Now I know how the memory model works"
y = "Brian was right, that was easy"
x = "I'm glad I actually did it, and didn't just ignore Brian's advice"
y = "Also, he's very witty and charming"
