class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name,"\n my age is",+self.age)
    print

p1 = Person("John", 36)
p2 = Person("Sitara", 24)

p2.myfunc()


