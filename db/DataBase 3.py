import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="HULKhari2328!",
                               database="Practice")

cursor = mydb.cursor()

# cursor.execute("create table  Grocer(Item_Id INTEGER PRIMARY KEY,ItemName varchar(30) UNIQUE,\
# UnitPrice Decimal(10,2),  quantity INTEGER,  date_of_purchase DATE)")

"""
cursor.execute("insert into Grocer(Item_Id,ItemName,UnitPrice,quantity,date_of_purchase) values\
(1,'Rice',52.50,80,'2010-02-01'),\
(2,'Wheat',25.40,50,'2010-03-09'),\
(3,'corn',50.80,100,'2010-03-11'),\
(4,'Semolina',28.90,50,'2010-01-15')\
")
"""
"""
cursor.execute("SELECT ItemName, UnitPrice, date_of_purchase FROM Grocer;")            # 1
product_names = cursor.fetchall()

for product in product_names:
    print(f'{product[0]}  {product[1]}    {product[2]}')"""

"""
cursor.execute("SELECT ItemName, MONTH(date_of_purchase) FROM Grocer;")    #2
product_names = cursor.fetchall()
for product in product_names:
    print(f'{product[0]}  {product[1]}  ')
"""
"""
cursor.execute("SELECT ItemName, YEAR(date_of_purchase) FROM Grocer;")         #3
product_names = cursor.fetchall()
for product in product_names:
    print(f'{product[0]}  {product[1]}  ')
"""
"""
cursor.execute("SELECT Item_Id, date_of_purchase, DAYNAME(date_of_purchase) FROM Grocer") #4
product_names = cursor.fetchall()

for product in product_names:
    print(f'{product[0]}  {product[1]}    {product[2]}')
"""
"""
cursor.execute("SELECT ItemName FROM Grocer WHERE DAYNAME(date_of_purchase) IN ('Monday', 'Tuesday');")  #5
product_names = cursor.fetchall()
for product in product_names:
    print(f'{product[0]}  ')
"""
"""
cursor.execute("SELECT DAYNAME(date_of_purchase) FROM Grocer WHERE ItemName = 'Rice';")     #6
product_names = cursor.fetchall()
for product in product_names:
    print(f'{product[0]}  ')
"""
"""
cursor.execute("SELECT ItemName, CAST(UnitPrice AS UNSIGNED) FROM Grocer;")        #7
product_names = cursor.fetchall()
for product in product_names:
    print(f'{product[0]}  {product[1]} ')
"""
"""
cursor.execute("SELECT CURDATE(),CURTIME()")            #7
result = cursor.fetchone()
print(f'{result[0]}      {result[1]}')
"""

mydb.commit()
cursor.execute("Select * from Grocer")

data = cursor.fetchall()
print(data)