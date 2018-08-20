import os, time
from sys import platform

class mainMenu(object):
    
    def __init__(self):
        
        ##To clear console according to the platform 
        
        if platform == "linux" or platform == "linux2" or platform == "darwin":
        
            self.clear = lambda: os.system('clear')
            
        elif platform == "win32":
            
            self.clear = lambda: os.system('cls')
        
        
        self.welcomeScreen()
    
    
    def welcomeScreen(self):
        
        self.clear() # clear console
        
        print("\n\n\n\t Welcome to banking services....... ") # welcome message
        time.sleep(2) # sleep for 2 sec
        
        self.clear() # clear console
        
        ##Menu 
        
        print(''' \n\n\t  MENU 
                  
                  1. Sign Up (New Customer)
                  2. Sign In (Existing Customer)
                  3. Admin Sign In
                  4. Quit ''')

        self.choice = input('\n Enter your choice : ') # To capture desired input