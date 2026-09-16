class Details: 
    def __init__(self): 
        self.__password = 9593 
        
    def resetpassword(self, password1): 
        self.__password = password1

    def get_password(self):
        return self.__password

    def __str__(self):
        return "Account details are secured."

p = Details() 
p.resetpassword(1000) 

print(p)

try:
    print(p.__password)
except AttributeError:
    print("Error: Cannot access the password directly from outside the class")

