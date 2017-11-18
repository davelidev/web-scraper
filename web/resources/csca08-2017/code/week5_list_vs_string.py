sample_list = ["A", "BC", 10, [1, 2, 3], ["A", "E", ["F", 4]]]
sample_string = "The road to success is under construction :)"

# use the memory model to find what would be the output
sample_list[0] = 100
sample_list[3][0] = 100
sample_list[4][2][0] = 100
print(sample_list)

# accessing the elements
print("sample_list [0] = ", sample_list[0])
print("sample_string [0] = ", sample_string[0])

print ("sample_list[0:2]=", sample_list[0:2])
# try 0:100. This means you have to be very careful in using indexes.
print ("sample_string[0:8] = ", sample_string[0:8])  # excludes index 8

print ("sample_list[:]=", sample_list[:])
print ("sample_string[:] = ", sample_string[:])

print ("sample_list[-1]=", sample_list[-1])
print ("sample_string[-1] = ", sample_string[-1])

print ("sample_list[-4]=", sample_list[-4])
print ("sample_string[-4] = ", sample_string[-4])

print ("sample_list[-6:]=", sample_list[-6:])  # strangely correct
# includes item at index-1
print ("sample_string[-6:] = ", sample_string[-6:])

print ("sample_list[-6:-1]=", sample_list[-6:-1])
# excludes item at index-1
print ("sample_string[-6:-1] = ", sample_string[-6:-1])

# returns null (an empty list)
print ("sample_list[-2:-5]=", sample_list[-2:-5])
print ("sample_string[-2:-5] = ", sample_string[-2:-5])

print ("sample_list[:-4]=", sample_list[:-4])
print ("sample_string[:-4] = ", sample_string[:-4])


# finding the length
print("len(sample_list)= ", len(sample_list))
print("len(sample_string) = ", len(sample_string))

# finding an element, this only works iff the given
# string is in the list or string
print("sample_list.index(\"BC\") = ", sample_list.index("BC"))
print("sample_string.find(\"success\") =  ", sample_string.find("success"))


# count the number of ocurrence of an item
print("sample_string.count(\"s\") =  ", sample_string.count("s"))
print("sample_list.count(\"A\") = ", sample_list.count("A"))

# replace
sample_list[0] = "AA"
print("sample_list = ", sample_list)
# sample_string[0] = "t"   will crash
sample_string.replace("T", "t")
print(sample_string)  # oops, strings are immutable
sample_string = sample_string.replace("T", "t")
print(sample_string)

# insert
sample_list.insert(1, "BB")
print(sample_list)
# no "insert" method for strings. You need to write a code for it.
