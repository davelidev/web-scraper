class Person:
    '''A class to represent a human being'''

    def __init__(self, name, age, height, gender):
        '''(Person, str, int, int, str) -> NoneType
        Create a new person named name, who is age years old, is
        height cm tall and has gender either "M" (Male) or "F" (Female)
        REQ: age >=0
        REQ: height >=0
        REQ: gender in {'M', 'F'}
        '''
        self._name = name
        self._age = age
        self._height = height
        self._gender = gender

    def __str__(self):
        '''(Person) -> str
        Return a string representing this person's name and an image of them
        '''
        # the height at which we will consider someone tall enough to draw
        # them differently
        TALL_HEIGHT = 175
        ret = ""
        # add a honorific based on this person's gender
        if(self._gender == "M"):
            ret += "Mr. "
        else:
            ret += "Ms. "

        ret += self._name + " "
        # add an image of this person based on their height
        if(self._height > TALL_HEIGHT):
            ret += "O-|--<"
        else:
            ret += "O|-<"

        return ret
