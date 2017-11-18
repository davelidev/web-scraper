class Buyer():
    ''' A class representing a buyer of a car'''
    def __init__(self, name, address, phone):
        '''(str, str, str) -> NoneType
        sets up a new buyer by its name, address and phone
        '''
        self._name = name
        self._address = address
        self._phone = phone

    def __str__(self):
        ''' (Buyer) -> str
        returns a string representing this buyer
        '''
        return (self._name + " lives in " + self._address +
                " and can be contacted on " + self._phone)


class Car():
    ''' A class representing a car'''
    def __init__(self, make, color, buyer):
        '''(str, str, Buyer) -> NoneType
        sets up a new car by its make, color and the owner of this car
        '''
        self._make = make
        self._color = color
        self._buyer = buyer

    def __str__(self):
        ''' (Car) -> str
        returns a string representing this car
        '''
        return ("This car is a " + self._color + " " + self._make +
                " that belongs to " + self._buyer._name)

    def set_buyer(self, buyer):
        ''' (Buyer) -> NonType
        sets up a new buyer for this car
        '''
        self._buyer = buyer

    def start(self):
        ''' (Car) -> NoneType
        starts this car
        '''
        pass


class SaleRepresentative():
    ''' A class representing a sale Representative'''
    pass


class Form():
    ''' A class representing a form to be filled in by sale representative'''
    pass


class BankAccount():
    ''' A class representing banking information'''
    pass


class Dealership():
    ''' A class representing a dealership'''
    pass

if (__name__ == "__main__"):
    Brian = Buyer("Brian", "1000 Main Street", "98765432100")
    print(Brian)
    Marzieh = Buyer("Marzieh", "2000 Somewhere Stree", "10123456789")
    print(Marzieh)
    his_car = Car("Lamborghini", "black", Brian)
    print(his_car)
    my_car = Car("Bugatti", "red", Marzieh)
    print(my_car)
    his_car = my_car
    his_car.set_buyer(Brian)
    print(my_car)
    print(his_car)
    my_car = None
    print(my_car)
    print(his_car)
