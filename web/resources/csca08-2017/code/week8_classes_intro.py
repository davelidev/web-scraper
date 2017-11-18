class CoolThing:
    '''This class represents a cool thing'''

    def awesome_method(i_dont_know_what_this_is_yet):
        print("This is my awesome method, inside CoolThing")


class TestA:
    a = ["A", "B", "C"]

    def __init__(self, lista):
        self._lista = lista

class TestB:

    def __init__(self, listb):
        self._listb = listb

    def mutate(self):
        self._listb[0] = 99

l = [1, 2, 3]
a = TestA(l)
b = TestB(l)
b.mutate()
print(l)
aa = a.a
print(aa)
aa[0] = "X"
print(aa)
print(a.a)