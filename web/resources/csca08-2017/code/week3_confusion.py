def my_func0 ():
    my_var = 2
    print (my_var)
    
def my_func1 (my_var):
    print ( my_var)
    my_var = my_var + my_var
    print (my_var)
    return my_var
def my_func2(my_var1, my_var2):
    my_var1 = my_var1 + my_var2
    print(my_var1)
    return ( my_var1)
    
my_var = my_func0()
print("first call:" , my_var)
my_var = 3
my_var = my_func1(my_var)
print("second call:", my_var)
my_var = my_func2(my_var, my_func1(my_var))
print("third call:", my_var)
my_var = my_func1(my_func2(my_func1(my_var), my_func1(my_var))) 
print("fourth call:", my_var)
