import os, time
from sys import platform

class mainMenu(object):
    
    def __init__(self):
        
        ##To clear console according to the platform 
        
        if platform == "linux" or platform == "linux2" or platform == "darwin":
        
            self.clear = lambda: os.system('clear')
            
        elif platform == "win32":
            
            self.clear = lambda: os.system('cls')
        
        
        self.welcomeScreen()  # To display main menu at start
        
        
    def subMenu(self): # Function to handle user input
        
        if self.choice == 1 :   # sign in
            
            self.signUp()
        
        elif self.choice == 2 : # sign out
            
            self.signIn()
        
        elif self.choice == 3 : # admin sign in
            
            self.adminSignIn()

        elif self.choice == 4 : # quit
            
            self.quit()
        
        else :                 # Invalid choice 
            
            print("Sorry! System can't determine the request....")
            self.welcomeScreen()
    
    
    def welcomeScreen(self): # Function to display main menu & prompting user choice
        
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

        self.choice = int(input('\n Enter your choice : ')) # To capture desired input
    
        self.subMenu() # To interpret user choice & perform specific functions

                            
            
if __name__ == '__main__':

    menuObject = mainMenu()