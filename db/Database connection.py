import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="HULKhari2328!")

# print(mydb)

cursor = mydb.cursor()

# cursor.execute("Create database Practice")
cursor.execute("USE Practice")
# cursor.execute("Create Table GYM(PrCode varchar(50) Primary key,PrName varchar(255),UnitPrice integer,Manufacturer varchar(255))")
#
# cursor.execute("insert into gym(PrCode,PrName,UnitPrice,Manufacturer) values\
# ('P101','Cross Trainer',25000,'Avon Fitness'),\
# ('P102','Thread Mill',32000,'AG Fitline'),\
# ('P103','Massage Chair',20000,'Fit Express'),\
# ('P104','Vibration Trainer', 22000,'Avon Fitness'),\
# ('P105','Bike',13000,'Fit Express');")

# cursor.execute("Alter table gym add column dt_of_manuf date")

# cursor.execute("Alter Table gym MODIFY COLUMN PrName varchar(30);")

# cursor.execute("ALTER TABLE gym CHANGE UnitPrice u_price integer;")

# cursor.execute("ALTER TABLE gym DROP COLUMN dt_of_manuf")

"""
cursor.execute("SELECT PrName FROM gym;")
product_names = cursor.fetchall()                                           # A

print("Product Names:")
for product in product_names:
    print(product[0])
"""

"""
cursor.execute("SELECT PrName,u_price FROM gym;")
product_names = cursor.fetchall()                                       # B

print("Product Names and unit price:")
for product in product_names:
    print(f'{product[0]}  {product[1]}')
"""

"""
cursor.execute("SELECT PrName FROM gym WHERE u_price < 20000.00")
product_names = cursor.fetchall()                                         #C

print("Product Names with Unit Price < Rs. 20000.00:")
for product in product_names:
    print(product[0])
"""
"""
cursor.execute("SELECT PrName FROM gym WHERE u_price Between 20000 and 30000")
product_names = cursor.fetchall()                                         #D

print("Product Names with Unit Price between 20000 to 30000:")
for product in product_names:
    print(product[0])
"""
"""
cursor.execute("SELECT PrName FROM gym WHERE Manufacturer = 'Fit Express'")
product_names = cursor.fetchall()

print("Product Names by Fit Express:")                                         #E
for product in product_names:
    print(product[0])

"""
"""cursor.execute("SELECT * FROM gym ORDER BY u_price DESC")                   #f
product_names = cursor.fetchall()
for product in product_names:
    print(f'{product[0]}   {product[1]}     {product[2]}       {product[3]}')
"""
"""
cursor.execute("insert into gym(PrCode,PrName,u_price,Manufacturer) values\
('P106', 'Vibro Exerciser', 23000, 'Avon Fitness');")             # G
"""
"""
cursor.execute("UPDATE gym SET u_price = u_price - (u_price * 0.1)")   # H
"""
"""
cursor.execute("SELECT * FROM gym WHERE Manufacturer LIKE 'A%'")              # I
product_details = cursor.fetchall()

print("Product Details with Manufacturer Name Starting with 'A':")
for product in product_details:
    print(product)
"""
mydb.commit()
cursor.execute("Select * from gym")

data = cursor.fetchall()
print(data)