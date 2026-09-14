# class creation
class MyClass:
    
    #private variable
    __privateVar = 27
    
    #private method 
    def privMethod(self):
        print("I'm inside class MyClass")
    
    #function to print value of private variable
    def hello(self):
        print("Private Variable Value: ", MyClass.__privateVar)
        
#Object creation and method call
foo = MyClass()
foo.hello()
