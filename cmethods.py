#Class variables.

class Employee:

    num_of_emps  = 0
    raise_amount = 1.04

#Tip !:
# Regular Methods automatically pass the instance as the first argument, called self.
# Class Methods automatically pass the class as the first argument, called cls.
# Static Methods don't pass anything automatically, neither the instance nor the class.

    def __init__(self,first,last,pay): #Constructer, works everytime we create an instance.
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+ '.' + last + '@company.com'
        Employee.num_of_emps += 1

    #Regular Method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #Alternative Constructer From Strings Split with (-)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #Static Method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True


emp_1 = Employee('Halit', 'Eris', 50000)
emp_2 = Employee('User' , 'Test', 60000)


#To test the static method
import datetime
my_date = datetime.date(2023,2,27)
print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'


# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)


# Employee.set_raise_amt(1.05)
#
# #if instance has the attribute, then the objects inherits the attribute.
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)