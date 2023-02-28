# Tip! :
# The Subclasses are useful because we can get all the functionality.
# and we can overwrite or add completely new functionality without
# without affecting the parent class.

#Super function, Manager Function, Inheritance

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.email = first + '.' + last + '@email.com'
        self.pay   = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev_1 = Developer('Halit', 'Eris', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Mert', 'Chick', 90000, [dev_1])


#Checking if is instance or Subclass
print('Checking if mgr_1 is instance of Employee  : ', isinstance(mgr_1, Employee))
print('Checking if mgr_1 is instance of Developer : ', isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print(help(Manager))
# print(mgr_1.email)
# mgr_1.print_emps()
#
#
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
#
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# USEFUL COMMAND TO VISUALIZE.
# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)