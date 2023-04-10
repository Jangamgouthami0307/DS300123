# Create a JSON file (employee.json) containing employee information of minimum 5 employees.
# Each employee information consistsof Name, DOB, Height, City, State.
# Write a python program that reads this information from 
# the JSON file and saves the informationinto a list of objects of Employee class.
# Finally print the list of the Employee objects.

import json

mydict = {
{

		"Name" : input("Enter the name of Employee1 : "),
		" dob " : input("Enter the DOB of Employee1 : "),
		"height" : input("Enter the Height of the Employee1 : "),
		"City "  : input("Enter the City of Employee1 : "),
		"State" : input("Enter the State of Employee1 : ")
	},    
	{

		"Name" : input("Enter the name of Employee2 : "),
		" dob " : input("Enter the DOB of Employee2 : "),
		"height" :input("Enter the Height of the Employee2 : "),
		"City "  : input("Enter the City of Employee2 : "),
		"State" : input("Enter the State of Employee2 : ")
	},    
	{

		"Name" : input("Enter the name of Employee3 : "),
		" dob " : input("Enter the DOB of Employee3 : "),
		"height" : input("Enter the Height of the Employee3 : "),
		"City "  : input("Enter the City of Employee3 : "),
		"State" : input("Enter the State of Employee3 : ")
	},  
	{

		"Name" : input("Enter the name of Employee4 : "),
		" dob " : input("Enter the DOB of Employee4 : "),
		"height" :input("Enter the Height of the Employee4 : "),
		"City "  : input("Enter the City of Employee4 : "),
		"State" : input("Enter the State of Employee4 : ")
	},    
	{

		"Name" : input("Enter the name of Employee5 : "),
		" dob " : input("Enter the DOB of Employee5 : "),
		"height" :input("Enter the Height of the Employee5 : "),
		"City "  : input("Enter the City of Employee5 : "),
		"State" : input("Enter the State of Employee5 : ")
    },

}    

json_string = json.dumps(mydict)
with open('mydata.json', 'w') as f:
    f.write(json_string)