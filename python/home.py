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
        
    
    def signUp(self): # Function for new user registration data collection
        
        print("\n Please fill the neccessary details below : ")
    
            
        def userName():
                
            print("\n Name : ")                                # Name of user ( fName & lName )
            self.fName = input('\n\t First Name : ')
            self.lName = input('\n\t Last Name : ')
        
        def userAddress():
                
            print("\n Address : ")                          # Address of user ( line 1 & 2, city, state, pincode )
            self.line1 = input('\n\t Line 1 : ')
            self.line2 = input('\n\t Line 2 : ')
            self.city = input('\n\t City : ')
            self.state = input('\n\t State : ')
            self.pinCode = input('\n\t Pincode : ')
        
        
        def accountType():
            
            print("\n Choose your account type : "),         # Account type ( savings or current )
            print("\n \t a. Savings Account [s]"),
            print("\t b. Current Account [c]")
            self.accntType = input('\n Enter your choice (s/c) : ')
            
            if self.accntType == 's' or self.accntType == 'S' :     # Prompt if savings account
                
                decision = input("\n Do you wish to make an initial deposit ? [y/n]")
                if decision == 'y' or decision == 'Y' : # If chooses to pay
                    
                    self.desposit = input('\n Enter the amount to deposit : Rs. ')
                
                else :
                    
                    self.deposit = 0
                
            elif self.accntType == 'c' or self.accntType == 'C' :   # Prompt if current account
                
                    decision = input("\n Note : 'Current account' need a minimum balance of Rs. 5000. \n Do you wish to continue ? [y/n]")
                    if decision == 'y' or decision == 'Y' : # If choice is to make the payment
                        
                        self.desposit = input('\n Enter the amount to deposit : Rs. ')    
                    
                    else :  # Prompt for changing the account type or cancel application
                        
                        decision = input("\n Do you wish to change account type or cancel the process ? [y/q]")
                        if decision == 'y' or decision == 'Y' :
                            
                            accountType()
                        
                        else : # If choice is to cancel application
                            
                            print("\n Processing your request... Please wait.....")
                            time.sleep(1)
                            self.welcomeScreen()
 
        userName()
        userAddress()
        
        accountType()
    
        
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