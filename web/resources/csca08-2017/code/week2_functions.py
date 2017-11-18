#a simple function to print the word Hello. Takes no paramters
#and doesn't return anything
def say_hello():
    print("Hello")

#a function that takes a name as a string, and returns a greeting based
#on that name
def create_greeting(name):
    greeting = "Hello " + name + " how are you today?"
    return greeting

#a function that takes a number and returns that number multipled by 10
def multiply_by_ten(input_number):
    result = input_number * 10
    return result

#a simple function for comparison to the mathematical function
#f(x) = x + 1
def f(x):
    result = x + 1
    return result

#this is the global code, where we can call our functions
say_hello()
hello_ret = say_hello()
print("say_hello() doesn't have a return statement, so it returns:",hello_ret)
greeting = create_greeting("Brian")
print("My greeting is:",greeting)
user_number = input("Give me a number:")
ten_x_number = multiply_by_ten(user_number)
print("your number * 10 is:",ten_x_number)
#oops, looks like we forgot that input always gives us a string, let's case
#it to an int and try again
user_number = int(user_number)
ten_x_number = multiply_by_ten(user_number)
print("your number * 10 is:",ten_x_number)
