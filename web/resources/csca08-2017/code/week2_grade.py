#our first attempt
print ("My grade on the first assignment was ", 12/15)
print ("If I get 50% on a2, my average will be ", (0.5 + 12/15)/2)
print ("If I get 60% on a2, my average will be ", (0.6 + 12/15)/2)
print ("If I get 70% on a2, my average will be ", (0.7 + 12/15)/2)
print ("If I get 80% on a2, my average will be ", (0.8 + 12/15)/2)
print ("If I get 90% on a2, my average will be ", (0.9 + 12/15)/2)
print ("If I get 100% on a2, my average will be ", (1 + 12/15)/2)

print("---")
#Using input & variables
a1_grade = float(input("Enter your grade on the first assignment: "))
print ("If I get 50% on a2, my average will be ", (0.5 + a1_grade)/2)
print ("If I get 60% on a2, my average will be ", (0.6 + a1_grade)/2)
print ("If I get 70% on a2, my average will be ", (0.7 + a1_grade)/2)
print ("If I get 80% on a2, my average will be ", (0.8 + a1_grade)/2)
print ("If I get 90% on a2, my average will be ", (0.9 + a1_grade)/2)
print ("If I get 100% on a2, my average will be ", (1 + a1_grade)/2)

#using functions (note that normally we would put our functions at the top
#of the file, but I wanted to break the file up into the three examples)
def calculate_average(mark1, mark2):
    #result = (mark1 + mark2)/2
    #weighted average example
    result = (0.3*mark1 + 0.7*mark2)
    return result
print("---")
print ("If I get 50% on a2, my average will be ", calculate_average(0.5, a1_grade))
print ("If I get 60% on a2, my average will be ", calculate_average(0.6, a1_grade))
print ("If I get 70% on a2, my average will be ", calculate_average(0.7, a1_grade))
print ("If I get 80% on a2, my average will be ", calculate_average(0.8, a1_grade))
print ("If I get 90% on a2, my average will be ", calculate_average(0.9, a1_grade))
print ("If I get 100% on a2, my average will be ", calculate_average(1, a1_grade))
