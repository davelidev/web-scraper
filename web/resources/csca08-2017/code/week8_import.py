from week8_person import Person

# this is the ugly sort of data structure we'd need to use before OOP
details = {('Alice', 21, 150, 'F'), ('Bob', 25, 180, 'M'),
           ('Carol', 18, 190, 'F'), ('David', 12, 110, 'M')}

# but thanks to OOP, we can just have a nice easy to use set of people objects
my_people = set()

# create one person for every name in the set, and put that person into
# our set of people
for next_entry in details:
    (name, age, height, gender) = next_entry
    temp_person = Person(name, age, height, gender)
    my_people.add(temp_person)

# now let's print out all of our people to make sure they're there
for next_person in my_people:
    print(next_person)
