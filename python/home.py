import os, time
from sys import platform

class mainMenu(object):
    
    def __init__(self):
        
        ##To clear console according to the platform 
        
        if platform == "linux" or platform == "linux2" or platform == "darwin":
        
            self.clear = lambda: os.system('clear')
            
        elif platform == "win32":
            
            self.clear = lambda: os.system('cls')