__name__ = '__main__'
import sqlite3
from maintUtility import *

running = 0
while running < 1: 
	command = input("What would you like to do? Enter 'add' to add a car, 'edit' to edit an existing car, 'view' to view a car, or 'quit' to exit: ")
	
	if command == 'edit':
		editing = input("What would like to edit? You can enter 'year', 'make', 'model', 'vin', current miles', 'front brakes', 'rear brakes' or 'oil'  :")
		if editing == 'year':
			update_year()
		if editing == 'make':
			update_make()
		if editing == 'model':
			update_model()
		if editing == 'vin':
			update_vin()
		if editing == 'current miles':
			update_current_miles()
		if editing == 'front brakes':
			update_frbrakes()
		if editing == 'rear brakes':
			update_rrbrakes()
		if editing == 'oil':
			update_oil()
		
	if command == 'add':
		car_adder()
	if command == 'view':
		selector()
	if command == 'quit':
		break