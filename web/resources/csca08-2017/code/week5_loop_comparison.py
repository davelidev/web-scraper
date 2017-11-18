my_string = "Hello World!"

## Counting upper/lower case characters

## while loop
upper_count = 0
lower_count = 0
index = 0
# loop through every index in the string, stopping when we hit the end
while(index < len(my_string)):
    # get the letter
    letter = my_string[index]

    # check the case of the letter, update our counters accordingly
    if(letter.isupper()):
        upper_count += 1
    elif(letter.islower()):
        lower_count += 1

    # don't forget to move on to the next letter
    index += 1

print(upper_count, lower_count)

## indexed for loop

upper_count = 0
lower_count = 0
# loop through every index in the string
for i in range(len(my_string)):
    # get the letter
    letter = my_string[i]

    # check the case of the letter, update our counters accordingly
    if(letter.isupper()):
        upper_count += 1
    elif(letter.islower()):
        lower_count += 1

print(upper_count, lower_count)

## elemental for loop

upper_count = 0
lower_count = 0
# loop through every letter in the string
for letter in my_string:

    # check the case of the letter, update our counters accordingly
    if(letter.isupper()):
        upper_count += 1
    elif(letter.islower()):
        lower_count += 1

print(upper_count, lower_count)

## building a string of every other character

## while loop
result = ""

index = 0
# keep looping as long as we're still inside the string
while(index < len(my_string)):
    # get the letter and add it to our result
    letter = my_string[index]
    result += letter
    # move over 2 characters
    index += 2

print(result)

## indexed for loop
result = ""

# loop through every index in the string, going up by 2s
for i in range(0, len(my_string), 2):
    # get the letter and add it to our result
    letter = my_string[i]
    result += letter

print(result)

## elemental for loop
result = ""

# we'll need to keep track of whether or not we've already printed
# so that we know whether or not to print this time
printed_last_time = False
for letter in my_string:
    # if we printed last time, don't print this time
    if(printed_last_time):
        # update so that next time we know to print
        printed_last_time = False
    else:
        # we didn't print last time, so we know that we can print this time
        result += letter
        # update our boolean so we know not to print next time
        printed_last_time = True

print(result)


## Example, parsing the function name out of a test file

my_string = "my_function|1,2,3|'text explanation'|True"

## while loop

# start at the first character
index = 0
# we'll use this to build up our result string
result = ""
# we'll set this to True when we've found the bar, and know we need to stop
found_bar = False
# loop until we either run off the end of the string, or find the | character
while((index < len(my_string)) and (not found_bar)):
    # get the next character in the input string
    current_char = my_string[index]
    # test to see if it's the bar character
    if(current_char == "|"):
        found_bar = True
    # if it's not the bar character, add it to our output string
    else:
        result += current_char
    # don't forget to move to the next index in the input string
    index += 1
print(result)

## indexed for loop
## important to note here that even if this doens't seem more complicated
## it's MUCH less efficient, particularly if the string was really really
## long, and the character we were looking for came early on

# once again, we need a boolean to tell us when we've found the bar
found_bar = False
result = ""
# loop for every chracter in the string
# (yes, I know we could use a string method to find a better stopping point
# but that would sort of ruin the whole point of the exercise, since
# that string method just uses a loop itself)
for index in range(0, len(my_string), 1):
    # get the next_character in the input_string
    current_char = my_string[index]
    # test to see if it's the bar character
    if(current_char == "|"):
        found_bar = True
    # now we need to have a separate if character, because we don't just
    # avoid printing the bar, we have to avoid printing every character
    # after it, since this loop will go through the whole string
    if(not found_bar):
        result += current_char
print(result)
