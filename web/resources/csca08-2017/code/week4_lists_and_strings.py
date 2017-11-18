my_list = [1, 'a', True, "Hello", [1, 2, 3], 3.1415926]
my_string = "Welcome to CSCA08"

print("The first element in my list is:", my_list[0])
print("The first 3 elements in my list are:", my_list[0:3])
print("I can capitalize my string:", my_string.upper())
print("But it doesn't change the string itself:", my_string)
print("If I try to do the same thing with reverse, something funny happens:",
      my_list.reverse(),
      " <-- I thought that would be my list backwards")
print("I guess I should read the help documentation to see what a method does")

# we can't edit strings
# my_string[3] = 'C' <-- this would crash

# but we can edit lists
print(my_list)
my_list[3] = ["Hello", "Goodbye", "Hi"]
print(my_list)
# and we can even edit lists inside lists
my_list[3][0] = "Test"
print(my_list)

# it's really important to be able to use the memory model to trace
# this sort of thing. This is where we get the payoff for learning
# the memory model the other week (you did spend the time to learn
# it, right?)
