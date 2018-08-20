import os, time

print("\t Welcome to banking services....... ")
time.sleep(2)
clear = lambda: os.system('cls')
clear()

print(''' \n\n\t  MENU 
          
          1. Sign Up (New Customer)
          2. Sign In (Existing Customer)
          3. Admin Sign In
          4. Quit ''')

choice = input('\n Enter your choice : ')