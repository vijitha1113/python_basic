class Dog: 
     species = "Canis familiaris" 
     def __init__(self, name, age): 
           self.name = name 
           self.age = age
     # Instance method 
     def description(self):
          print(self.name ,"is", self.age ,"years old") 
# Another instance method
     def speak(self, sound): 
           print(self.name, "says" ,sound)
miles=Dog("miles",4)
miles.description()
miles.speak("Woof Woof")
