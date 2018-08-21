import os, time
from sys import platform


##To clear console according to the platform 
        
if platform == "linux" or platform == "linux2" or platform == "darwin":
 
    clear = lambda: os.system('clear')
     
elif platform == "win32":
     
    clear = lambda: os.system('cls')
            

class mainMenu(object):
    
    def __init__(self):
        
        
        self.welcomeScreen()  # To display main menu at start
    
    
    def subMenu(self): # Function to handle user input
        
        if self.choice == 1 :   # sign in
            
            signUpMenu_Object = signUpMenu()
            signUpMenu_Object.signUp()
        
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
        
        clear() # clear console
        
        print("\n\n\n\t Welcome to banking services....... ") # welcome message
        time.sleep(2) # sleep for 2 sec
        
        clear() # clear console
        
        ##Menu 
        
        print(''' \n\n\t  MENU 
                  
                  1. Sign Up (New Customer)
                  2. Sign In (Existing Customer)
                  3. Admin Sign In
                  4. Quit ''')

        self.choice = int(input('\n Enter your choice : ')) # To capture desired input
    
        self.subMenu() # To interpret user choice & perform specific functions


class signUpMenu(object) :
    
    
    def __init__(self):
        
        self.desposit = 0    # Initializing of deposit money
    
    
    def userAddress(self):
                
            print("\n Address : ")                          # Address of user ( line 1 & 2, city, state, pincode )
            self.line1 = input('\n\t Line 1 : ')
            self.line2 = input('\n\t Line 2 : ')
            self.city = input('\n\t City : ')
            self.state = input('\n\t State : ')
            self.pinCode = input('\n\t Pincode : ')    
    
    
    def userName(self):
                
            print("\n Name : ")                                # Name of user ( fName & lName )
            self.fName = input('\n\t First Name : ')
            self.lName = input('\n\t Last Name : ')
    
    
    def accountType(self):   # Function for determining acnt type during sign up
            
            print("\n Choose your account type : "),         # Account type ( savings or current )
            print("\n \t a. Savings Account [s]"),
            print("\t b. Current Account [c]")
            self.accntType = input('\n Enter your choice (s/c) : ')
            
            if self.accntType == 's' or self.accntType == 'S' :     # Prompt if savings account
                
                decision = input("\n Do you wish to make an initial deposit ? [y/n]")
                if decision == 'y' or decision == 'Y' : # If chooses to pay
                    
                    self.desposit = int(input('\n Enter the amount to deposit : Rs. '))
                
        
            elif self.accntType == 'c' or self.accntType == 'C' :   # Prompt if current account
                
                decision = input("\n Note : 'Current account' need a minimum balance of Rs. 5000. \n Do you wish to continue ? [y/n]")
                if decision == 'y' or decision == 'Y' : # If choice is to make the payment
                    
                    while True :   # To check if entered amount is enough to create an account
                        
                        try:
                            clear()
                            self.desposit = int(input('\n Enter the amount to deposit : Rs. '))
                            
                        except ValueError: # In case of an invalid input
                            
                            clear()
                            print("\n\n\t Sorry! System can't process your request.... Please enter a valid amount....")
                            time.sleep(2)
                            continue
                        
                        if self.desposit < 5000 :  # Comparing the deposited amount with min bal
                            
                            clear()
                            print("\n\n\t Note : Current accounts must have a minimum balance of Rs.5000. Please try again.....")
                            time.sleep(2)
                            continue
                        
                        else :
                            
                            break    # To break the loop if condition is satisfied
                
                else :  # Prompt for changing the account type or cancel application
                    
                    decision = input("\n Do you wish to change account type or cancel the process ? [y/q]")
                    if decision == 'y' or decision == 'Y' :
                        
                        self.accountType()
                    
                    else : # If choice is to cancel application
                        
                        print("\n Processing your request... Please wait.....")
                        time.sleep(1)
                        
                        mainMenu_Object = mainMenu()
                        mainMenu_Object.welcomeScreen()
            
            else : 
                
                print("\n Sorry! Our bank doesn't provide this type of account. Please choose from the available options.....")
                time.sleep(2)
                self.accountType()
                
            
    
    def signUp(self): # Function for new user registration data collection
        
        print("\n Please fill the neccessary details below : ")
    
        self.userName()
        self.userAddress()
        self.accountType()
        
        
        decision = input('\n Your account is to be created. Do you wish to proceed or quit ? [y/q]')
        
        if decision == 'y' or decision == 'Y' :
            
            clear()
            print("\n Processing your request..... Please wait.....")
            time.sleep(2)
            
            clear()
            print("\n Creating user account...... This may take a moment......")

                            
            
if __name__ == '__main__':

    menuObject = mainMenu()