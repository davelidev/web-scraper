# if we open a file for reading, we can't write to it
my_file = open("test_file.txt", "r")
# my_file.write("Hello")  #  this will cause an error
my_file.close()

# open a file for writing... create it if it isn't already there
my_file = open("new_file.txt", "w")
my_file.write("Testing testing 1,2,3\n")  # have to add our own \ns
my_file.write("Ground control to Major Tom\n")
my_file.write("Is there anybody out there?\n")
my_file.close()  # if you don't close it... it may not write

my_file = open("new_file.txt", "w")   # whatever was there will go away
my_file.write("This\nwill\nappear\non\nmultiple\nlines\n")
my_file.close()

my_file = open("new_file.txt", "a")  # now we'll append instead
my_file.write("Adding to the old file\n")
my_file.write("The answer to life, the universe and everything is:")
# my_file.write(42)  #  can't do this, we can only write strings
my_file.write(str(42))
my_file.write("\n")
my_file.close()
