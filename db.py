import mysql.connector

connection = mysql.connector.connect(
  user='joren',
  password='grapefruits',
  host='127.0.0.1',
  database='python'
)

cursor = connection.cursor()

userText = input('\nWhat bicycle do you want to add to the list?\n\n')
print('\n\n')
price = 2000
addQuery = 'INSERT INTO bicycles (brand, price, electric) VALUES (%s, %s, false)'
cursor.execute(addQuery, (userText,price))
connection.commit()

cursor.execute('SELECT * FROM bicycles;')
bicycles = cursor.fetchall()

for bicycle in bicycles:
  print(bicycle[1])


connection.close()

# Database
# User input

list = [1,2,3]
tuple = (1,2,3)
dict = {
  'my_key': 123
}

