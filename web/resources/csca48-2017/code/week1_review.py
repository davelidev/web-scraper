# We should also be comfortable with the basic principles of
# working with objects


class Person():
    '''A class to represent a person'''

    def __init__(self, name, age, phone):
        '''(Person, str, int, str) -> NoneType

        Create a new person with name, age and phone as their
        primary attributes
        REQ: age >= 0
        '''
        self._name = name
        self._age = age
        self._phone = phone

    def __str__(self):
        '''(Person) -> str

        Return the string representation of this person, which
        consists of a greeting based on their age, and their name
        '''
        res = ""
        # young people are less formal
        if(self._age < 17):
            res += "Yo dude! "
        elif(self._age < 70):
            res += "Hello, "
        else:
            res += "Hi there sonny "
        res += "My name is " + self._name
        return res

    def get_age(self):
        '''(Person) -> int

        Return the age of this person
        '''
        return self._age

    def get_phone(self):
        '''(Person) -> str

        Return this person's phone number
        '''
        return self._phone

class Student(Person):
    '''A class to represent a student'''

    def __init__(self, name, age, phone, student_num):
        '''(Student, str, int, str, str) -> NoneType

        Create a new person with name age, phone as their personal
        attributes, and student_num as their student number
        REQ: age >= 0
        '''
        self._student_num = student_num
        self._GPA = 4.0
        Person.__init__(self, name, age, phone)


    def get_age(self):
        '''(Student) -> int

        Return the age of this student. If they are under 19, they
        will lie and return 19 instead (no idea why)
        '''
        return max(self._age, 19)


def phone_nums_in_age_range(address_book, lower_age, upper_age):
    '''(dict of {str: Person} -> set of str

    Return the phone numbers of all people in address book with age
    between lower_age and upper_age (inclusive)

    >>> d = {'alice':Person('Alice', 10, '111-1111'), 'bob':Person('Bob', 20, '222-2222'),\
    'carol':Person('Carol', 30, '333-3333')}
    >>> s = phone_nums_in_age_range(d, 15, 20)
    >>> s == {'222-2222'}
    True
    >>> s = phone_nums_in_age_range(d, 5, 40)
    >>> s == {'111-1111', '222-2222', '333-3333'}
    True
    >>> s = phone_nums_in_age_range(d, 35, 40)
    >>> s == set()
    True
    '''
    phones = set()
    # loop over every person in the dictionary
    for next_name in address_book:
        # to make our lives easier, get all their information out ahead
        # of time
        next_person = address_book[next_name]
        age = next_person.get_age()
        phone_num = next_person.get_phone()
        # if this person is below the cutoff age, add their phone
        # number to the set
        if(age >= lower_age and age <= upper_age):
            phones.add(phone_num)
    return phones

if(__name__ == "__main__"):
    alice = Person('Alice', 15, '123-1234')
    bob = Person('Bob', 95, '111-1111')
    carol = Student('Carol', 25, '999-9999', '1234')
    dave = Student('Dave', 17, '987-6543', '6789')
    ab = {'alice': alice, 'bob':bob, 'carol':carol, 'dave':dave}
    young_nums = phone_nums_in_age_range(ab, 1, 20)
    print(young_nums)


