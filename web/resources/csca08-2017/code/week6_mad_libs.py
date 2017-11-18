# these are all the bad words I know
CENSORED_WORDS = ['heck', 'darn', 'crud', 'butt']
NAMES = ['Alice', 'Bob', 'Carol', 'Dave']
FOOD = ['pizza', 'hamburger', 'chilli', 'cheese', 'sandwich', 'steak']


def mad_lib(input_file, output_file):
    '''(io.TextIOWrapper, io.TextIOWrapper) -> NoneType

    Copy the contents of input_file to output_file, but replace every word that
    appears in NAMES or FOODS with text input by the user.
    If the user's words are in the CENSORED_WORDS list, prompt again until
    they give an example that isn't.
    If any word in input_file is in CENSORED_WORDS, replace it with ****
    REQ: input_file is a file open for reading
    REQ: output_file is a file open for writing/appending
    '''
    # loop through each line in the file
    for next_line in input_file:
        # for each word in the line (see help(str) for how split works)
        for next_word in next_line.split():
            # if the word is in names
            if(next_word in NAMES):
                # ask the user for a name
                user_word = input("Please enter a name:")
                # if the user gives a censored name, keep asking them until
                # they give us a real name
                while(user_word in CENSORED_WORDS):
                    user_word = input("Are you 10? Give a real name:")
                # once we have a real name, add it to our output
                output_file.write(user_word + " ")
            # if the next word is a food
            elif(next_word in FOOD):
                # ask the user to enter a new food
                user_word = input("Please enter a food:")
                # if they provide a censored word, keep asking them until they
                # give us a real food
                while(user_word in CENSORED_WORDS):
                    user_word = input("Very mature... try again please:")
                # once we have a non-censored word, add it to our output
                output_file.write(user_word + " ")
            # if the word is already censored, replace it with stars
            elif(next_word in CENSORED_WORDS):
                output_file.write("**** ")
            # otherwise, just add the word to our output
            else:
                output_file.write(next_word + " ")
        # at the end of each line, we'll need to add in the newline
        output_file.write("\n")

if(__name__ == "__main__"):
    # test our code with some sample files:
    input_file = open("input_file.txt", "r")
    output_file = open("output_file.txt", "w")
    mad_lib(input_file, output_file)
    input_file.close()
    output_file.close()
