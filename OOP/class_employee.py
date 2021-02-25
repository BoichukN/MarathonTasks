# Create a class Employee that will take a full name as argument,
# as well as a set of none, one or more keywords.
# Each instance should have a name and a lastname attributes plus one more attribute
# for each of the keywords, if any.

class Employee:
    def __init__(self, fullname, **kwargs):
        self.fullname = fullname
        self.name = self.fullname.split()[0]
        self.lastname = self.fullname.split()[1]
        for keyword, value in kwargs.items():
            self.__dict__[keyword] = value
