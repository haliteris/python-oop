# Using @property methods, we define a method like a typical method, but we are able to
# access it like an attribute.
#
# Using Setter we can change the attribute without having an error of "can't set the attribute."
# Therefore we will give ability to a method to change an class parameter.
# to use that we simply re-define the same method using @method.setter decorator.
#
# Deleters are used for 'Clean-up codes'. We use, @method.deleter decorator and simply equal
# the values to None.

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, new_fname):
        first, last = new_fname.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name is deleted.')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


# Creating an Employee Instance
emp_1 = Employee('Halit', 'Eris')

# The first form of the Employee 1.
print("The instance's email and fullname is constructed as: ")
print(emp_1.email)
print(emp_1.fullname)

# Using Setter we can change the first and last name attributes.
emp_1.fullname = 'Elif Birdir'
print('After using setter method, full name can be editted as : ')
print(emp_1.email)
print(emp_1.fullname)

# Since we defined a deleter decorator for fullname class-function.
# using del, we can delete the fullname attribute to None.
del emp_1.fullname
print(emp_1.fullname)

# Instead of using these commands below like a method with (), we access them like an attribute
# using property methods.
# print(emp_1.first)
# print(emp_1.email())
# print(emp_1.fullname())
