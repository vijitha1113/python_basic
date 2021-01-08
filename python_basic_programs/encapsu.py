# Python program to
# demonstrate protected members


# Creating a base class
class Base:
	def __init__(self):
		
		# Protected member
		self._name = "vijitha"
		self._age=30
		self.sales=30000

# Creating a derived class 
class Derived(Base):
	def __init__(self):
		
		# Calling constructor of
		# Base class
		Base.__init__(self) 
		print("Calling protected member of base class: ")
		print(self._name)
		print(self._age)
		

obj1 = Derived()
		
obj2 = Base()

# Calling protected member
# Outside class will result in 
# AttributeError
print(obj2.sales)
print(obj2.name)
