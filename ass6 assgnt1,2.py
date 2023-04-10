states = dict()
n = int(input("How many states are there : "))
for i in range(n):
    state = input("Enter name of the state : ")
    capital = input("Enter name of the capital : ")
    states[state] = capital
print("Created dictionary is :",states)    

import json

[
  {
    
    "state": "Telangana",
    "capital": "Hyderabad"
  },
  {
    
    "state": "Andhra Pradesh",
    "capital": "Amaravati"
  },
  {
    
    "state": "Manipur",
    "capital": "Imphal"
  },
  {
    
    "state": "Assam",
    "capital": "Dispur"
  },
  {
    
    "state": "Goa",
    "capital": "Panaji"
  },
  {
    
    "state": "Tamilnadu",
    "capital": "Chennai"
  },
  {
    
    "state": "Rajasthan",
    "capital": "Jaipur"
  },
]