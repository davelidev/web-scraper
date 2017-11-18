# get number of weeks
week = 12
# get number of lectures
lecture = 10
# get number of words per second
words = 2.5

calorie_per_second = 0.008
seconds_in_hour = 3600
# calorie = week * lecture * seconds_in_hour * words * calorie_per_second
calorie = week * lecture * seconds_in_hour * words * calorie_per_second
# print calorie
print ("The calories burned = ", calorie)
