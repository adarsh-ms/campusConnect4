import os, time
from sys import platform
import random

import cx_Oracle


class configuration(object):          #For initial configuration of db & clear function
    
    
    
    def initializer(self):            #Replacement for constructor to avoid re-initialising the functions 
        
        self.clearFunction()
        self.dbSetup()
        self.dbCredentials()
        
          
    def clearFunction(self):    #Initialising clear
        
         
        ##To clear console according to the platform 
        
        if platform == "linux" or platform == "linux2" or platform == "darwin":
         
            self.clear = lambda: os.system('clear')
             
        elif platform == "win32":
             
            self.clear = lambda: os.system('cls')


    def dbSetup(self):          #Initialising db for linux

        ##To set environment variables for installed database 
        
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            
            os.environ['ORACLE_HOME'] = '/u01/app/oracle/product/11.2.0/xe'
            os.environ['LD_LIBRARY_PATH'] = '/u01/app/oracle/product/11.2.0/xe/lib'
        
            print(os.environ.get('ORACLE_HOME'))
            print(os.environ.get('LD_LIBRARY_PATH'))
            time.sleep(2)
        
    
    def dbCredentials(self):        #To prompt user for database login credentials
        
        self.id = input('\n Enter your username for database : ')
        self.passwd = input('\n Enter your password for database : ')
        self.dbStart()
    
    
    def dbStart(self):          #To connect to database
        
        self.con = cx_Oracle.connect('{0}/{1}'.format(self.id,self.passwd))   #To connect to database with user_name:$id & password:$passwd
        self.cur = self.con.cursor()
        
    
    def dbStop(self):
        
        self.con.close()
    
     
    def createTable(self):          #To check if CUSTOMERS table already exits or not & if not, create the table
        
        
        self.CUR.execute("SELECT tname FROM tab WHERE tname = 'CUSTOMERS'")
        print(self.CUR.fetchall())
        time.sleep(2)
        
        if self.CUR.fetchall() == "[]" :
            
   
            
            print("table created")
            time.sleep(2)
         

class TABLE_USERS (object):         #Table for storing aacount no,name,date created,balance,account type,address
    
    
    def __init__(self,cur):

        self.CUR = cur              #cur=con.cursor() from configuration class via child class
        self.createTable()
          
        print("USERS")  
    
    
    def insertIntoTableCustomers(self,accNo,line1,line2,city,state,zipCode):
        
        
        self.accountNumber = accNo
        self.addressLine1 = line1
        self.addressLine2 = line2
        self.city = city
        self.state = state
        self.zipCode = zipCode
        
        self.CUR.execute("""INSERT INTO customers VALUES (:accountNumber,
                            ADDRESS_TABLE(ADDRESS_SUB_COLUMNS(:addressLine1, :addressLine2, :city, :state, :zip)""",
                            (self.accountNumber,self.addressLine1,self.addressLine2,self.city,self.state,self.zip))
        
        

class mainMenu(configuration,TABLE_USERS):
    
    
    def __init__(self):
        
        
        super().initializer()       #To initialize functions in parent1 (configuration)         
        
        super().__init__(self.cur)  #Call to constructor in parent2 (TABLE_USERS) : passing cur from parent1
        
        
        self.welcomeScreen()  # To display main menu at start
             
                
    def subMenu(self): # Function to handle user input
        
        if self.choice == 1 :   # sign in
            
            signUpMenu_Object = signUpMenu()
            signUpMenu_Object.signUp()
        
        elif self.choice == 2 : # sign out
            
            signInMenu_Object = signInMenu()
            signInMenu_Object.signIn()
        
        elif self.choice == 3 : # admin sign in
            
            self.adminSignIn()

        elif self.choice == 4 : # quit
            
            self.quit()
        
        else :                 # Invalid choice 
            
            print("\n Sorry! System can't determine the request....")
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
        
    

class signUpMenu(configuration) :
    
    
    def __init__(self):
        
        super().clearFunction()
        
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
                            self.clear()
                            self.desposit = int(input('\n Enter the amount to deposit : Rs. '))
                            
                        except ValueError: # In case of an invalid input
                            
                            self.clear()
                            print("\n\n\n\t Sorry! System can't process your request.... \n\n\t Please enter a valid amount....")
                            time.sleep(2)
                            continue
                        
                        if self.desposit < 5000 :  # Comparing the deposited amount with min bal
                            
                            self.clear()
                            print("\n\n\t Note : Current accounts must have a minimum balance of Rs.5000.\n\n\t Please try again.....")
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
            
            self.clear()
            print("\n Processing your request..... Please wait.....")
            time.sleep(2)
            
            self.clear()
            print("\n Creating user account...... This may take a moment......")
            

                            
class signInMenu(configuration):
    
    
    def __init__(self):
        
        super().clearFunction()
        
        self.signInSubMenu()
        
    
    def signInSubMenu(self):
        
        self.clear() # clear console
        
        print("\n\n\n\t Welcome back....... ") # welcome message
        time.sleep(2) # sleep for 2 sec
        
        self.clear() # clear console
        
        ##Sub-menu for signIn
        
        print(''' \n\n\t  MENU 
                  
                  1. Address Change
                  2. Money Deposit
                  3. Money Withdrawal
                  4. Print Statement
                  5. Transfer Money
                  6. Account Closure
                  7. Customer Logout ''')

        self.signInChoice = int(input('\n Enter your choice : ')) # To capture desired input
    
        self.userChoice() # To interpret user choice & perform specific tasks

    
    def userChoice(self):
        
        if self.signInChoice == 1 :         # Address Change
            
            self.addressChange()

        elif self.signInChoice == 2 :       # Money Deposit
            
            self.depositMoney()
    
        elif self.signInChoice == 3 :       # Money Withdrawal
            
            self.withDrawMoney()

        elif self.signInChoice == 4 :       # Print Statement
            
            self.printStatement()

        elif self.signInChoice == 5 :       # Transfer Money
            
            self.moneyTransfer()

        elif self.signInChoice == 6 :       # Account Closure
            
            self.closeAccount()
        
        elif self.signInChoice == 7 :       # Customer Logout
            
            self.customerLogout()

        else :
            
            print("\n Sorry! System can't determine the request....")
            self.signInSubMenu()
            
            
if __name__ == '__main__':

    
    initialObject = configuration()