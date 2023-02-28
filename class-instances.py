#Python Object-Oriented Programming Guidelines for beginners.

class Employee:
    def __init__(self,first,last,pay): #Constructer
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Halit', 'Eris', 50000)
emp_2 = Employee('User', 'Test', 60000)

#instance returns
print(emp_1.fullname())

#Also this can be obtained by:
print(Employee.fullname(emp_1))
