
# I was not able to connect to the database using sir's code so i used Chat GPT

import mysql.connector

try:
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='127.0.0.1',  # Use localhost or actual IP if MySQL is on a different machine
        user='root',
        password='',
        auth_plugin='mysql_native_password',  # Specify the authentication plugin if needed
        database = 'indigo'
    )

    mycursor = conn.cursor()

    # Create a new database
    # mycursor.execute("CREATE DATABASE indigo") '#' ye ek bar database bana ke commnt kr diya

    print('Connection established and database created')

except mysql.connector.Error as err:
    print('Connection error:', err)

# create a table
# airport -> airport_id | code | name | city

# mycursor.execute("""
# CREATE TABLE airport(
#    airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#    name VARCHAR(255) NOT NULL
#)
#""")
#conn.commit()

# ek bar excicute hone ke bad # kr diya kyu ki bar bar table create nahi krna hai

# Insert data to the table

#mycursor.execute("""
#INSERT INTO airport VALUES
    #(1,'DEL','New delhi','IGIA'),
    #(2,'CCU','Kolkata','NSCA'),
    #(3,'BOM','Mumbai','CSMA')
#""")
#conn.commit()

# ek bar excicute hone ke bad # kr diya kyu ki bar bar insert nahi krna hai

# Search/Retrive
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1 ")
data = mycursor.fetchall() # fetchall() to fetcha all the data, fetchone() to fetch one data
print(data)

# Update
mycursor.execute("""
UPDATE airport
SET city = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)

# Delete
mycursor.execute("DELETE FROM airport WHERE airport_id = 2")
conn.commit()

mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)







