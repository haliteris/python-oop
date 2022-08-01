#Class variables.

class Employee:

    num_of_emps  = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay): #Constructer, works everytime we create an instance.
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+ '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print('Number of Employees: '+ str(Employee.num_of_emps))

emp_1 = Employee('Corey', 'Scahfer', 50000)
emp_2 = Employee('User', 'Test', 60000)

print('Number of Employees: '+ str(Employee.num_of_emps))
emp_1.raise_amount = 1.05

print(emp_1.__dict__)

#if instance has the attribute, then the objects inherits the attribute.
print(Employee.raise_amount)
print(emp_1.apply_raise())
print(emp_1.pay)
print(emp_2.raise_amount)