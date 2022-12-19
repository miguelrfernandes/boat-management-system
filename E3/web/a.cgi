#!/usr/bin/python3
import psycopg2
import cgi

IST_ID = 'ist192836'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = 'jpsm4756'
db_name = IST_ID

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Boat Management Systems</title>')
print('<style> body { padding-top: 70px; text-align: center; } </style>')
print('</head>')
print('<body>')

try:
    
    # Creating connection
    connection = psycopg2.connect('host=' + host + ' port=' + str(port) + ' user=' + IST_ID + ' password=' + password + ' dbname=' + db_name)
    print('<p>Connected to Postgres on ', host, ' as user ', IST_ID, ' on database ', db_name, '.</p>')
    cursor = connection.cursor()
    
    form = cgi.FieldStorage()
    # Script
    action = form.getvalue('action')
    if action == 'create_sailor':
        first_name = form.getvalue('first_name')
        surname = form.getvalue('surname')
        email = form.getvalue('email')
        cursor.execute('''
            INSERT INTO sailor
            VALUES (%s, %s, %s);
        ''', (first_name, surname, email))
        connection.commit()
        print('<p>Sailor created successfully.</p>')
    elif action == 'remove_sailor':
        email = form.getvalue('email')
        cursor.execute('''
            DELETE FROM sailor
            WHERE email = %s;
        ''', (email,))
        connection.commit()
        print('<p>Sailor removed successfully.</p>')
        
    # Page
    # Go back to the main page
    print('<a href="http://web.tecnico.ulisboa.pt/ist192836/app.cgi"><h1>Go back to the main page</h1></a>')

    # a) List, create and remove sailors (including junior and senior)
    print('<h1>a) List, create and remove sailors (including junior and senior)</h1>')



    # a.1) List all sailors
    print('<h2>a.1) List all sailors</h2>')
    cursor.execute('SELECT * FROM sailor;')
    print('<table border="1" style="width:100%" align="center">')
    print('<tr>')
    print('<th>Sailor First Name</th>')
    print('<th>Sailor Surname</th>')
    print('<th>Sailor Email</th>')
    print('</tr>')
    for row in cursor:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')
    
    # a.2) Create a new sailor
    print('<h2>a.2) Create a new sailor</h2>')
    print('<form action="http://web.tecnico.ulisboa.pt/ist192836/a.cgi" method="post">')
    print('<input type="hidden" name="action" value="create_sailor">')
    print('<label for="first_name">First Name:</label>')
    print('<input type="text" id="first_name" name="first_name"><br><br>')
    print('<label for="surname">Surname:</label>')
    print('<input type="text" id="surname" name="surname"><br><br>')
    print('<label for="email">Email:</label>')
    print('<input type="text" id="email" name="email"><br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    print('<br>')

    # a.3) Remove a sailor
    print('<h2>a.3) Remove a sailor</h2>')
    print('<form action="http://web.tecnico.ulisboa.pt/ist192836/a.cgi" method="post">')
    print('<input type="hidden" name="action" value="remove_sailor">')
    print('<label for="email">Email:</label>')
    print('<input type="text" id="email" name="email"><br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    print('<br>')
    
    #Closing connection
    cursor.close()
    connection.close()

    print('<p>Connection closed.</p>')
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>', e, '</p>')



print('</body>')
print('</html>')
