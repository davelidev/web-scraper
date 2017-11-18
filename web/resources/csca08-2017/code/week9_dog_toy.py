class Toy():
    '''A class to represent a dog toy'''

    def __init__(self, sound):
        '''(Toy, str) -> NoneType

        Create a new toy that makes the sound given by sound when squeezed
        '''
        self._sound = sound

    def squeeze(self):
        '''(Toy) -> NoneType

        Print the sound made by this toy
        '''
        print(self._sound)


class Dog():
    '''A class to represent a good boy... yes you are... yes you ARE!'''
    # a set of dog breeds that are 'hyper' (will squeeze their toy more
    # than once)
    HYPER_BREEDS = {'Jack Russel', 'Chihuahua', 'Spaniel'}
    # the number of times a hyper dog breed will squeeze its toy
    NUM_HYPER_SQUEEZES = 3

    def __init__(self, breed):
        '''(Dog, str) -> NoneType
        Create a dog of type breed
        '''
        # We will use None to signify a dog that has no toy (so we can check
        # whether the dog has a toy, we need a variable that's always set)
        self._toy = None
        # set a flag to tell us if this is an 'excitable' dog
        self._is_hyper = (breed in Dog.HYPER_BREEDS)

    def give_toy(self, new_toy):
        '''(Dog, Toy) -> NoneType
        Give this dog new_toy, replacing any old toy it may have had
        '''
        self._toy = new_toy

    def play(self):
        '''(Dog) -> NoneType
        Play with this dog. If the dog has a toy, then they will squeeze it,
        the number of times the toy is squeezed will depend on whether or
        not the dog is of a exciteable breed.  Exciteable breeds are
        'Jack Russel', 'Chichuhua' and 'Spaniel'
        '''
        # if the dog has a toy, it will play with the toy
        if(self._toy):
            # all dogs will squeeze their toy once
            self._toy.squeeze()
            # hyper dogs will squeeze their toy many more times
            if(self._is_hyper):
                for i in range(Dog.NUM_HYPER_SQUEEZES - 1):
                    self._toy.squeeze()
        # any dogs that don't have a toy will bark instead
        else:
            print("woof")

if(__name__ == "__main__"):
    lyria = Dog("Newfoundland")
    lyria.play()
    ball = Toy("jingle")
    sanda = Dog("Chihuahua")
    bone = Toy("squeek")
    lyria.give_toy(ball)
    sanda.give_toy(bone)
    lyria.play()
    sanda.play()
