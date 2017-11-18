#A simple person class that can print out its own family tree
#submitted without comments (left for exercise)

class Person():
    def __init__(self, name):
        self._name = name
        self._father = None
        self._mother = None

    def set_father(self, father):
        self._father = father

    def set_mother(self, mother):
        self._mother = mother

    def print_family_tree(self, indent=""):
        if(self._father != None):
            self._father.print_family_tree(indent + "\t")
        print(indent + self._name)
        if(self._mother != None):
            self._mother.print_family_tree(indent + "\t")

a = Person("Alice")
b = Person("Bob")
c = Person("Carol")
d = Person("Dave")
e = Person("Edith")
f = Person("Frank")
g = Person("Gertrude")
h = Person("Henry")
a.set_father(b)
a.set_mother(c)
b.set_father(d)
b.set_mother(e)
c.set_father(f)
c.set_mother(g)
f.set_father(h)
a.print_family_tree()
