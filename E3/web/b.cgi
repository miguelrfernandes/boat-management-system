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
    if action == 'create_reservation':
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        boat_country = form.getvalue('country')
        cni = form.getvalue('cni')
        responsible = form.getvalue('responsible')
        cursor.execute('''
            INSERT INTO reservation
            VALUES (%s, %s, %s, %s, %s);
        ''', (start_date, end_date, boat_country, cni, responsible))
        connection.commit()
        print('<p>Reservation created successfully.</p>')
    elif action == 'remove_reservation':
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')
        cursor.execute('''
            DELETE FROM reservation
            WHERE start_date = %s AND end_date = %s AND country = %s AND cni = %s;
        ''', (start_date, end_date, country, cni))
        connection.commit()
        print('<p>Reservation removed successfully.</p>')
        
        
    # Page
    # Go back to the main page
    print('<a href="http://web.tecnico.ulisboa.pt/ist192836/app.cgi"><h1>Go back to the main page</h1></a>')

    # b) List, create and remove reservations
    print('<h1>b) List, create and remove reservations</h1>')
    
    # b.1) List all reservations
    print('<h2>b.1) List all reservations</h2>')
    cursor.execute('SELECT * FROM reservation;')
    print('<table border="1" style="width:100%" align="center">')
    print('<tr>')
    print('<th>Start Date</th>')
    print('<th>End Date</th>')
    print('<th>Country</th>')
    print('<th>CNI</th>')
    print('<th>Responsible</th>')
    print('</tr>')
    for row in cursor:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('<td>', row[4], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')
    
    # b.2) Create a reservation
    print('<h2>b).2 Create a reservation</h2>')
    print('<form action="http://web.tecnico.ulisboa.pt/ist192836/b.cgi" method="get">')
    print('<input type="hidden" name="action" value="create_reservation">')
    print('<label for="start_date">Start Date</label>')
    print('<input type="date" id="start_date" name="start_date">')
    print('<label for="end_date">End Date</label>')
    print('<input type="date" id="end_date" name="end_date">')
    print('<label for="country">Country</label>')
    print('<input type="text" id="country" name="country">')
    print('<label for="cni">CNI</label>')
    print('<input type="text" id="cni" name="cni">')
    print('<label for="responsible">Responsible</label>')
    print('<input type="text" id="responsible" name="responsible">')
    print('<input type="submit" value="Submit">')
    print('</form>')
    print('<br>')
    
    # b.3) Remove a reservation
    print('<h2>b.3) Remove a reservation</h2>')
    print('<form action="http://web.tecnico.ulisboa.pt/ist192836/b.cgi" method="get">')
    print('<input type="hidden" name="action" value="remove_reservation">')
    print('<label for="start_date">Start Date</label>')
    print('<input type="date" id="start_date" name="start_date">')
    print('<label for="end_date">End Date</label>')
    print('<input type="date" id="end_date" name="end_date">')
    print('<label for="country">Country</label>')
    print('<input type="text" id="country" name="country">')
    print('<label for="cni">CNI</label>')
    print('<input type="text" id="cni" name="cni">')
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
