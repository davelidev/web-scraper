from datetime import date


class Person():
    '''A class representing a person, used to show a simple example
    of OOP concepts'''

    def __init__(self, name, dob, gender):
        '''(Person, str, str, str) -> NoneType
        Set up a new person with a name dob (date of birth) and gender
        REQ: dob is formatted as "YYYY-MM-DD" all numeric values
        REQ: gender is one of "Male","Female"
        '''
        self._name = name
        year = int(dob[0:4])
        month = int(dob[5:7])
        day = int(dob[8:10])
        self._dob = date(year, month, day)
        self.is_male = (gender == "Male")

    def __str__(self):
        '''(Person) -> str
        Return a string representing this person
        '''
        return ("Hi, my name is " + self._name + " and I am " +
                str(self.get_age()) + " years old")

    def get_age(self):
        '''(Person) -> int
        Return this person's current age in years
        '''
        total_age = date.today() - self._dob
        age_years = total_age.total_seconds() // (365 * 24 * 60 * 60)
        return int(age_years)


class Student(Person):
    '''A class representing a student, created by inheritence
    inheriting attributes/methods from person and only extending
    the ones we need to make this a student'''

    def __init__(self, name, dob, gender, student_num, gpa):
        '''(Student, str, str, float) -> NoneType
        Set up a new student with a name dob (date of birth), gender,
        student_num, and their current gpa
        REQ: dob is formatted as "YYYY-MM-DD" all numeric values
        REQ: gender is one of "Male","Female"
        REQ: 0 <= gpa <= 4
        '''
        self._name = name
        year = int(dob[0:4])
        month = int(dob[5:7])
        day = int(dob[8:10])
        self._dob = date(year, month, day)
        self.is_male = (gender == "Male")
        self._student_num = student_num
        self._gpa = gpa

    def __str__(self):
        '''(Student) -> NoneType
        Return a string representing this student
        '''
        # get the result of my parent class's string method, and add to it
        ret = ("Hi, my name is " + self._name + " and I am " +
               str(self.get_age()) + " years old")
        if(self._gpa >= 3.5):
            ret += " and I'm on the honours list"
        elif(self._gpa < 2):
            ret += " and I need to study harder"
        return ret

    def raise_gpa(self, raise_amount):
        '''(Student, float) -> NoneType
        Increase the student's GPA by raise_amount
        '''
        self._gpa += raise_amount
        # Cap the GPA at 4
        if(self._gpa > 4):
            self._gpa = 4


if (__name__ == "__main__"):
    alice = Person("Alice Jones", "1978-03-05", "Female")
    bob = Student("Robert Smith", "1995-01-01", "Male", "1234", 3.6)
    print(alice)
    print(bob)
    # we cah get both of their ages
    print(alice.get_age())
    print(bob.get_age())
    # but only students have a raise_gpa method
    # alice.raise_gpa(0.1) #<-- this will cause a crash
    bob.raise_gpa(0.1)
