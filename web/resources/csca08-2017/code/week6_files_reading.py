# open a file and read one line
my_file = open("test_file.txt", "r")
next_line = my_file.readline()
print(next_line)

# read the rest of the file into a string
whole_file = my_file.read()
print(whole_file)
my_file.close()

# re-open the file to start from the beginning, and
# read it into lists
my_file = open("test_file.txt", "r")
print(next_line)
three_lines = my_file.readlines(3)
all_lines = my_file.readlines()
print(three_lines)
print(all_lines)
my_file.close()

####
# Read a file using method 1
####
my_file = open("test_file.txt", "r")
# read in the first line of code
next_line = my_file.readline()

# so long as there are more lines to read, print the current line,
# and read another
while(next_line != ''):
	# print(next_line)
    # print adds its own \n
    print(next_line.strip('\n'))
    next_line = my_file.readline()
my_file.close()

####
# File Reading Method 2
####
my_file = open("test_file.txt", "r")
all_lines = my_file.readlines()
# we can close the file handle, because we've already got the info
my_file.close()

# now we just loop through the list
for next_line in all_lines:
    print(next_line.strip('\n'))

####
# File Reading Method 3
####
my_file = open("test_file.txt", "r")

# loop through using a custom for loop created for file handles
for next_line in my_file:
    print(next_line.strip('\n'))

my_file.close()
