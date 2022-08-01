#Python Object-Oriented Programming Guidelines for beginners.

class Employee:
    def __init__(self,first,last,pay): #Constructer
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+ '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Corey', 'Scahfer', 50000)
emp_2 = Employee('User', 'Test', 60000)

#instance returns
print(emp_1.fullname())

#Also this can be obtained by:
print(Employee.fullname(emp_1))


""" DONT DO THIS
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'User'
emp_2.last = 'Test'
emp_2.email = 'user.test@company.com'
emp_2.pay = 60000
"""