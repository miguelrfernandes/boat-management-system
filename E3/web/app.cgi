#!/usr/bin/python3
import psycopg2

IST_ID = 'ist192836'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = 'jpsm4756'
db_name = IST_ID

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Boat Management System Web Application Prototype</title>')
print('<style> body { padding-top: 70px; text-align: center; } </style>')
print('</head>')
print('<body>')

# Boat Management System Web Application Prototype
print('<h1>Boat Management System Web Application Prototype</h1>')

# a) List, create and remove sailors (including junior and senior)
print('<a href="http://web.tecnico.ulisboa.pt/ist192836/a.cgi"><h1>1. List, create and remove sailors (including junior and senior)</h1></a>')

# b) List, create and remove reservations
print('<a href="http://web.tecnico.ulisboa.pt/ist192836/b.cgi"><h1>2. List, create and remove reservations</h1></a>')

# c) Authorise/De-authorise sailors for reservations
print('<a href="http://web.tecnico.ulisboa.pt/ist192836/c.cgi"><h1>3. Authorise/De-authorise sailors for reservations</h1></a>')

# d) List, register, and remove trips (including listing the available locations)
print('<a href="http://web.tecnico.ulisboa.pt/ist192836/d.cgi"><h1>4. List, register, and remove trips (including listing the available locations)</h1></a>')


print('</body>')
print('</html>')
