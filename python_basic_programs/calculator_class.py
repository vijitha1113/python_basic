class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    def floordiv(self):
        return self.a//self.b

a = float(input('Enter First number : '))
b = float(input('Enter Second number : '))        
obj=cal(a,b)
while True:
    def menu():
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide \n5. Floor division') 
        print(x)
    menu()
    choice = int(input('Please select one of the following : ')) 
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    elif choice == 3:
        print("Result: ",obj.multiply())    
    elif choice == 4:
        print("Result: ",obj.divide())
    elif choice==5:
        print("Result:",obj.floordiv())
    elif choice == 0:
        print('Again try one of the following')
        break
    else:
        print('Invalid option') 
        break       
print()
