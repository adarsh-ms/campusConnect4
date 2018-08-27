import cx_Oracle

con = cx_Oracle.connect('system/campusConnect')   #To connect to database with user_name:$id & password:$passwd
cur = con.cursor()

cust_id = input("\n\t Username/Customer Id : ")

cur.execute("""SELECT customer_id
               FROM CUSTOMER_PASSWORD
               WHERE customer_id = :cust_id""",{"cust_id":cust_id})

query_id = cur.fetchall()
                
print(query_id)