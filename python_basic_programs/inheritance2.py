# Python code to demonstrate how parent constructors 
# are called. 
  
# parent class 
class Person( object ):     
  
        # __init__ is known as the constructor          
        def __init__(self, name, idnumber):    
                self.name = name 
                self.idnumber = idnumber 
        def display(self): 
                print(self.name) 
                print(self.idnumber) 
  
# child class 
class Employee( Person ):            
        def __init__(self, name, idnumber, salary, post): 
                self.salary = salary 
                self.post = post 
  
                # invoking the __init__ of the parent class  
                Person.__init__(self, name, idnumber)  
  
                  
# creation of an object variable or an instance 
a = Employee('Anjali', 886012, 200000, "Intern")
b = Employee('Amrutha', 886009, 350000, "Operation manager")
  
# calling a function of the class Person using its instance 
a.display()
b.display()
