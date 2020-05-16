import sqlite3


#conn = sqlite3.connect('maint.db')
#c = conn.cursor()

#This creates the table, commented out after intial table creation.
#c.execute('''CREATE TABLE cars (
#	inv text,
#	year integer,
#	make text,
#	model text,
#	vin integer,
#	cur_miles integer,
#	fbrakes integer,
#	rbrakes integer,
#	oil integer
#)''')

def car_adder():
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	inv = input('Enter Inventory Number: ')
	year = input('Enter a four digit year: ')
	make = input('Enter the make: ')
	model = input('Enter the model: ')
	vin = input('Enter the last four vin: ')
	cur_miles = input('Enter current miles: ')
	fbrakes = input('Enter the mileage of the last front brake job: ')
	rbrakes = input('Enter the mileage of the last rear brake job: ')
	oil = input('Enter the mileage of the last oil change: ')


	c.execute("INSERT INTO cars (inv, year, make, model, vin, cur_miles, fbrakes, rbrakes, oil) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (inv, year, make, model, vin, cur_miles, fbrakes, rbrakes, oil))
	
	print('****Database updated****')
	conn.commit()
	conn.close()

def update_oil():
	print('****Updating Oil Change Mileage****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET oil=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')
	
def update_current_miles():
	print('****Updating Current Mileage****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET cur_miles=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')
	
def update_frbrakes():
	print('****Updating Front Brake Mileage****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET fbrakes=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')

def update_rrbrakes():
	print('****Updating Rear Brake Mileage****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET rbrakes=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')
	
def update_year():
	print('****Updating Year****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET year=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')
	
def update_make():
	print('****Updating Make****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET make=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')

def update_model():
	print('****Updating Model****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET model=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')

def update_vin():
	print('****Updating VIN****')
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('What car would you like to update? ')
	value = input('What is the new value? ')
	c.execute(""" UPDATE cars SET vin=? where inv=?""", (value, car))
	conn.commit()
	conn.close()
	print('****Database updated****')
	
def selector():
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()
	car = input('Which car would you like to view? ')
	c.execute("""SELECT * FROM cars WHERE inv=?""", (car,))
	records = c.fetchall()
	for row in records:
		print('Inventory number: ', row[0])
		print('Year: ', row[1])
		print('Make: ', row[2])
		print('Model: ', row[3])
		print('VIN: ', row[4])
		print('Current Miles: ', row[5])
		print('Last front brake change mileage: ', row[6])
		print('Last rear brake change mileage: ', row[7])
		print('Last oil change mileage: ', row[8])
	conn.close()

	


if __name__ == '__main__':
	selector()
	
	


#c.execute(update)

#print(c.fetchall())

#conn.commit()
#conn.close()

