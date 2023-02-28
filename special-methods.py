# Special Methods
# __methods__ are called as Dunder functions they have very useful abilities. Meaning Double Underscore.
# More can be found here: https://docs.python.org/3/reference/datamodel.html#emulating-callable-objects

# __init__, is a constructer, creating instances in your class. Takes 'self' as an attribute.

# __repr__, Since printing a class object out may not give any opinion about the object,
# using this dunder you can have a string representation of a class object.
# You can re-define __repr__ at your class to maintain the ability of the dunder.

# __str__, Called by str(object) and the built-in functions format() and print()
# to compute the “informal” or nicely printable string representation of an object.
# The return value must be a string object. Very useful for debugging.

# __add__, Sequence types of dunders should implement addition (meaning concatenation) for your built
# parameters. They can be used as object.__add__, and also can be maintained using a defined class function.

# __len__, Calls to implement the built-in function len(). Should return the length of the object,
# and integer if >= 0.

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.email = first + '.' + last
        self.pay   = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Halit', 'Eris', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


# print(emp_1 + emp_2)

print(len(emp_1))

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1,2))
# print(str.__add__('a','b'))