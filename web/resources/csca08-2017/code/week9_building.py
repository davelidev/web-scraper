class Room():
    '''A class to represent a general room'''

    def __init__(self):
        '''(Room) -> NoneType

        Creates a new, clean room
        '''
        self._is_clean = True

    def __str__(self):
        '''(Room) -> str

        Return the string representation of this room (the area, and the room
        type)
        '''
        if(self._is_clean):
            state = "clean"
        else:
            state = "dirty"
        return state

    def clean(self):
        '''(Room) -> NoneType

        Make this room clean
        '''
        self._is_clean = True

    def dirty(self):
        '''(Room) -> NoneType

        Make this room dirty
        '''
        self._is_clean = False


class Building():
    ''' A class to reprenset a general building'''

    def __init__(self, address, num_rooms):
        '''(Building, str, int) -> NoneType

        Initialize this building to have address Street address and
        num_rooms total rooms
        REQ: num_rooms > 0
        '''
        self._address = address
        # we'll hold the rooms as a list of Room objects
        self._rooms = []
        # create as many rooms as needed, add them to the list of rooms
        for i in range(num_rooms):
            new_room = Room()
            self._rooms.append(new_room)

    def __str__(self):
        '''(Building) -> str

        Return the string representation of this building (saying
        which rooms are clean or dirty)
        '''
        out = self._address + ":"
        for count in range(0, len(self._rooms)):
            out += " room #" + str(count) + " is " + str(self._rooms[count])
        return out

    def use_room(self, room_num):
        '''(Building, int) -> NoneType

        Use room #room_num, making it dirty
        REQ: room_num > 0
        '''
        self._rooms[room_num].dirty()

    def clean_room(self, room_num):
        '''(Building, int) -> NoneType

        Clean room #room_num, making it clean
        REQ: room_num > 0
        '''
        self._rooms[room_num].clean()

if(__name__ == "__main__"):
    my_house = Building("123 Main st", 7)
    print(my_house)
    my_house.use_room(1)
    my_house.use_room(3)
    my_house.use_room(4)
    print(my_house)
    my_house.clean_room(3)
    my_house.clean_room(1)
    print(my_house)
