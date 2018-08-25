import os, time
from sys import platform
import random

import cx_Oracle
from asn1crypto._ffi import null
from symbol import argument


class configuration(object):          #For initial configuration of db & clear function
    
    
    
    def __init__(self): 
        
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
        
    
    def dbCredentials(self):        #To prompt user for database login credentials
        
        self.id = input('\n Enter your username for database : ')
        self.passwd = input('\n Enter your password for database : ')
        self.dbStart()
    
    
    def dbStart(self):          #To connect to database
        
        self.con = cx_Oracle.connect('{0}/{1}'.format(self.id,self.passwd))   #To connect to database with user_name:$id & password:$passwd
        self.cur = self.con.cursor()
        
    
    def dbStop(self):
        
        self.con.close()
    
     
    def launchMenu(self):
        
        welcomeMenu_Object = mainMenu(self)
    
         

class tableConfiguration (configuration):         #Table for storing aacount no,name,date created,balance,account type,address
    
    
    def __init__(self):

        
        super().__init__()                      #super(tableConfiguration,self).__init__()
        
        self.createTables()
        
        self.launchMenu()
          
    
    def createTables(self):          #To check if CUSTOMERS table already exits or not & if not, create the table
        
        
        self.cur.execute("SELECT table_name FROM all_tables WHERE table_name IN ('CUSTOMERS','ACCOUNTS','CUSTOMER_PASSWORD','CLOSED_ACCOUNTS','TRANSACTIONS')") #Returns the name of tables if they are present in the database

        table_tuple = self.cur.fetchall()   #Returns a list of tuples of relations
        print(table_tuple)
        
        def CREATE_TABLE_CUSTOMERS() :      #For creating relation CUSTOMERS if it doesn't exist
            
            print("table CUSTOMERS does not exist")
                
            self.cur.execute("""CREATE TABLE CUSTOMERS(
                                customer_id VARCHAR2(10)         NOT NULL,
                                customer_name VARCHAR2(20)       NOT NULL,
                                customer_address VARCHAR2(70)    NOT NULL,
                                date_of_sign_up DATE,
                                PRIMARY KEY (customer_id))""")
        
        def CREATE_TABLE_ACCOUNTS():        #For creating relation ACCOUNTS if it doesn't exist
            
            print("table ACCOUNTS does not exist")
                
            self.cur.execute("""CREATE TABLE ACCOUNTS(
                                customer_id VARCHAR2(10)    NOT NULL,
                                account_id VARCHAR2(14)     NOT NULL,
                                account_type VARCHAR2(4)    NOT NULL,
                                main_balance FLOAT          NOT NULL,
                                date_created DATE,
                                PRIMARY KEY (account_id),
                                FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id))""")
            
        def CREATE_TABLE_CUSTOMER_PASSWORD():   #For creating relation CUSTOMER_PASSWORD if it doesn't exist
            
            print("table CUSTOMER_PASSWORD does not exist")
                
            self.cur.execute("""CREATE TABLE CUSTOMER_PASSWORD(
                                customer_id VARCHAR2(10)    NOT NULL UNIQUE,
                                password VARCHAR2(20)       NOT NULL,
                                date_modified DATE)""")
            
        def CREATE_TABLE_CLOSED_ACCOUNTS():     #For creating relation CLOSED_ACCOUNTS if it doesn't exist
            
            print("table CLOSED_ACCOUNTS does not exist")
                
            self.cur.execute("""CREATE TABLE CLOSED_ACCOUNTS(
                                account_id VARCHAR2(14)    NOT NULL UNIQUE,
                                date_of_closure DATE       NOT NULL)""")
            
        def CREATE_TABLE_TRANSACTIONS():        #For creating relation TRANSACTIONS if it doesn't exist
            
            print("table TRANSACTIONS does not exist")
                
            self.cur.execute("""CREATE TABLE TRANSACTIONS(
                                from_account_id VARCHAR2(14)    NOT NULL,
                                to_account_id VARCHAR2(14)      NOT NULL,
                                amount FLOAT                    NOT NULL,
                                date_of_transaction DATE        NOT NULL)""")
        
        
        switchCases = {
                
                'CUSTOMERS'         : CREATE_TABLE_CUSTOMERS,
                
                'ACCOUNTS'          : CREATE_TABLE_ACCOUNTS,
                
                'CUSTOMER_PASSWORD' : CREATE_TABLE_CUSTOMER_PASSWORD,
                
                'CLOSED_ACCOUNTS'   : CREATE_TABLE_CLOSED_ACCOUNTS,
                
                'TRANSACTIONS'      : CREATE_TABLE_TRANSACTIONS 
            
            }
            
        
        table_list = ['CUSTOMERS','ACCOUNTS','CUSTOMER_PASSWORD','CLOSED_ACCOUNTS','TRANSACTIONS']
        
        for i in range(0,len(table_tuple)):
             
            print(i)
            for name in table_tuple[i] :
                
                print(name)
                table_list.remove('{0}'.format(name))
                
        print(table_list)
        
        
        for name in table_list :
            
            print(name)
            switchCases[name]()
        

class mainMenu(object):
    
    
    def __init__(self,parent):
        
        
        self.PARENT = parent
        self.welcomeScreen()  # To display main menu at start
             
                
    def subMenu(self): # Function to handle user input
        
        if self.choice == 1 :   # sign up
            
            signUpMenu(self.PARENT)
        
        elif self.choice == 2 : # sign in
            
            signInMenu(self.PARENT)
        
        elif self.choice == 3 : # admin sign in
            
            self.adminSignIn()

        elif self.choice == 4 : # quit
            
            self.quit()
        
        else :                 # Invalid choice 
            
            print("\n Sorry! System can't determine the request....")
            self.welcomeScreen()
    
    
    def welcomeScreen(self): # Function to display main menu & prompting user choice
        
        self.PARENT.clear() # clear console
        
        print("\n\n\n\t Welcome to banking services....... ") # welcome message
        time.sleep(2) # sleep for 2 sec
        
        self.PARENT.clear() # clear console
        
        ##Menu 
        
        print(''' \n\n\t  MENU 
                  
                  1. Sign Up (New Customer)
                  2. Sign In (Existing Customer)
                  3. Admin Sign In
                  4. Quit ''')

        self.choice = int(input('\n Enter your choice : ')) # To capture desired input
    
        self.subMenu() # To interpret user choice & perform specific functions
        
    

class signUpMenu(object) :
    
    
    def __init__(self,parent):
        
        
        self.PARENT = parent
        
        self.desposit = 0    # Initializing of deposit money
        
        self.signUp()
    
    
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
                            self.PARENT.clear()
                            self.desposit = int(input('\n Enter the amount to deposit : Rs. '))
                            
                        except ValueError: # In case of an invalid input
                            
                            self.PARENT.clear()
                            print("\n\n\n\t Sorry! System can't process your request.... \n\n\t Please enter a valid amount....")
                            time.sleep(2)
                            continue
                        
                        if self.desposit < 5000 :  # Comparing the deposited amount with min bal
                            
                            self.PARENT.clear()
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
                        exit()
                        
#                         mainMenu(self.PARENT).welcomeScreen()
            
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
            
            self.PARENT.clear()
            print("\n Processing your request..... Please wait.....")
            time.sleep(2)
            
            self.PARENT.clear()
            print("\n Creating user account...... This may take a moment......")
            

                            
class signInMenu(object):
    
    
    def __init__(self,parent):
        
        
        self.PARENT = parent
        
        self.signInSubMenu()
        
    
    def signInSubMenu(self):
        
        self.PARENT.clear() # clear console
        
        print("\n\n\n\t Welcome back....... ") # welcome message
        time.sleep(2) # sleep for 2 sec
        
        self.PARENT.clear() # clear console
        
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

    
    initialObject = tableConfiguration()