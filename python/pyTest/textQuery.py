# import cx_Oracle
# # 
# con = cx_Oracle.connect('system/campusConnect')   #To connect to database with user_name:$id & password:$passwd
# cur = con.cursor()
# 
# cust_id = input("\n\t Username/Customer Id : ")
# 
# cur.execute("""SELECT address_line1,address_line2,city,state,pincode
#                FROM CUSTOMERS
#                WHERE customer_id = :cust_id""",{"cust_id":cust_id})
# 
# query_id = cur.fetchall()
#                 
# print(query_id)

import unittest
import home as home


class test(unittest.TestCase):
    
    object = home.signInMenu(home.configuration())
    object.addressChange()
    