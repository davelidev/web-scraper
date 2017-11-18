# Some More List Examples
name_list = ["Alice", "Bob", "Andrew", "Dave", "Allison", "Carol"]

# want to count the number of names starting with 'A'
a_name_count = 0
for next_name in name_list:
    if(next_name.startswith("A")):
        a_name_count += 1

print ("There were", a_name_count, "people whose name started with 'A'")

# Count the number of upper/lower case/other characters
my_string = "HeLlO, My NAme IS BRiaN"

cap_count = 0
lower_count = 0
for next_char in my_string:
    if(next_char.isupper()):
        cap_count += 1
    elif(next_char.islower()):
        lower_count += 1

print("There were ", cap_count, " capital letters, and ",
      lower_count, " lower case letters")
# this is more efficient than adding another elif to the above loop
other_count = len(my_string) - (cap_count + lower_count)
print("There were also ", other_count, " other characters")

# Range Examples
# note that if we leave the step out, Python assumes it's 1
# and if we leave the start off, Python assumes it's 0
my_range = range(1, 100)
print("The 5th element of the range is:", my_range[4])
my_range = range(100, 1, -3)
print("Now the 5th element is:", my_range[4])

step_value = 1  # What would happen if this value were negative?
start_value = 1
end_value = 10  # Note that range doesn't INCLUDE the upper bound

for next_value in range(start_value, end_value, step_value):
    print(next_value)

# While Examples
user_name = ""
while(user_name != "Dave"):
    user_name = input("Please enter your name (only Dave is allowed in):")

print("Welcome Dave")

loop_counter = 0
while(loop_counter < 10):
    # Since we don't check again until the block is done, this won't stop us
    loop_counter += 1000
    loop_counter -= 1000
    loop_counter += 1
    print(loop_counter)

# Infinite loop example, uncomment at your own risk
# while(True):
#    print("All work and no play makes Jack a dully boy")
