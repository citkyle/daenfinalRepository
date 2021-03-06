#   Establishes class with constructor 
#   and the two methods getString and printString
class Login:
    def __init__(self):
        self.userName = ""

    def getString(self):
        self.userName = str(input()) 
    
    def printString(self):
        print("Pet Care Website")
        print("User Login:", self.userName.upper())

#   Main section of the code that creates the instance 
#   of Login class as my_login and calls getString 
#   and printString methods of the class      
my_login = Login()
my_login.getString()
my_login.printString()


