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
    if action == 'create_trip':
        takeoff = form.getvalue('takeoff')
        arrival = form.getvalue('arrival')
        insurance = form.getvalue('insurance')
        from_latitude = form.getvalue('from_latitude')
        from_longitude = form.getvalue('from_longitude')
        to_latitude = form.getvalue('to_latitude')
        to_longitude = form.getvalue('to_longitude')
        skipper = form.getvalue('skipper')
        reservation_start_date = form.getvalue('reservation_start_date')
        reservation_end_date = form.getvalue('reservation_end_date')
        boat_country = form.getvalue('boat_country')
        cin = form.getvalue('cin')
        cursor.execute('''
            INSERT INTO trip
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        ''', (takeoff, arrival, insurance, from_latitude, from_longitude, to_latitude, to_longitude, skipper, reservation_start_date, reservation_end_date, boat_country, cin))
        connection.commit()
        print('<p>Trip created successfully.</p>')
    elif action == 'delete_trip':
        takeoff = form.getvalue('takeoff')
        arrival = form.getvalue('arrival')
        insurance = form.getvalue('insurance')
        from_latitude = form.getvalue('from_latitude')
        from_longitude = form.getvalue('from_longitude')
        to_latitude = form.getvalue('to_latitude')
        to_longitude = form.getvalue('to_longitude')
        skipper = form.getvalue('skipper')
        reservation_start_date = form.getvalue('reservation_start_date')
        reservation_end_date = form.getvalue('reservation_end_date')
        boat_country = form.getvalue('boat_country')
        cin = form.getvalue('cin')
        cursor.execute('''
            DELETE FROM trip
            WHERE takeoff = %s AND arrival = %s AND insurance = %s AND from_latitude = %s AND from_longitude = %s AND to_latitude = %s AND to_longitude = %s AND skipper = %s AND reservation_start_date = %s AND reservation_end_date = %s AND boat_country = %s AND cin = %s;
        ''', (takeoff, arrival, insurance, from_latitude, from_longitude, to_latitude, to_longitude, skipper, reservation_start_date, reservation_end_date, boat_country, cin))
        connection.commit()
        print('<p>Trip deleted successfully.</p>')
    
    
    # Page
    # Go back to the main page
    print('<a href="http://web.tecnico.ulisboa.pt/ist192836/app.cgi"><h1>Go back to the main page</h1></a>')

    # d) List, register, and remove trips (including listing the available locations)
    print('<h1>4. List, register, and remove trips (including listing the available locations)</h1>')

    # d.1) List trips
    print('<h2>d.1) List trips</h2>')
    cursor.execute('SELECT * FROM trip;')
    print('<table border="1" style="width:100%" align="center">')
    print('<tr>')
    print('<th>Takeoff</th>')
    print('<th>Arrival</th>')
    print('<th>Insurance</th>')
    print('<th>From latitude</th>')
    print('<th>From longitude</th>')
    print('<th>To latitude</th>')
    print('<th>To longitude</th>')
    print('<th>Skipper</th>')
    print('<th>Reservation Start Date/th>')
    print('<th>Reservation End Date</th>')
    print('<th>Boat Country/th>')
    print('<th>CIN</th>')
    print('</tr>')
    for row in cursor:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('<td>', row[4], '</td>')
        print('<td>', row[5], '</td>')
        print('<td>', row[6], '</td>')
        print('<td>', row[7], '</td>')
        print('<td>', row[8], '</td>')
        print('<td>', row[9], '</td>')
        print('<td>', row[10], '</td>')
        print('<td>', row[11], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')

    # d.2) Create trip
    print('<h2>d.2) Create trip</h2>')
    print('<form action="d.cgi" method="post">')
    print('<input type="hidden" name="action" value="create_trip">')
    print('<label for="takeoff">Takeoff:</label>')
    print('<input type="date" id="takeoff" name="takeoff"><br><br>')
    print('<label for="arrival">Arrival:</label>')
    print('<input type="date" id="arrival" name="arrival"><br><br>')
    print('<label for="insurance">Insurance:</label>')
    print('<input type="text" id="insurance" name="insurance"><br><br>')
    print('<label for="from_latitude">From latitude:</label>')
    print('<input type="text" id="from_latitude" name="from_latitude"><br><br>')
    print('<label for="from_longitude">From longitude:</label>')
    print('<input type="text" id="from_longitude" name="from_longitude"><br><br>')
    print('<label for="to_latitude">To latitude:</label>')
    print('<input type="text" id="to_latitude" name="to_latitude"><br><br>')
    print('<label for="to_longitude">To longitude:</label>')
    print('<input type="text" id="to_longitude" name="to_longitude"><br><br>')
    print('<label for="skipper">Skipper:</label>')
    print('<input type="text" id="skipper" name="skipper"><br><br>')
    print('<label for="reservation_start_date">Reservation Start Date:</label>')
    print('<input type="date" id="reservation_start_date" name="reservation_start_date"><br><br>')
    print('<label for="reservation_end_date">Reservation End Date:</label>')
    print('<input type="date" id="reservation_end_date" name="reservation_end_date"><br><br>')
    print('<label for="boat_country">Boat Country:</label>')
    print('<input type="text" id="boat_country" name="boat_country"><br><br>')
    print('<label for="cin">CIN:</label>')
    print('<input type="text" id="cin" name="cin"><br><br>')
    print('<input type="submit" value="Create trip">')
    print('</form>')

    # d.3) Remove trip
    print('<h2>d.3) Remove trip</h2>')
    print('<form action="d.cgi" method="post">')
    print('<input type="hidden" name="action" value="remove_trip">')
    print('<label for="takeoff">Takeoff:</label>')
    print('<input type="date" id="takeoff" name="takeoff"><br><br>')
    print('<label for="arrival">Arrival:</label>')
    print('<input type="date" id="arrival" name="arrival"><br><br>')
    print('<label for="insurance">Insurance:</label>')
    print('<input type="text" id="insurance" name="insurance"><br><br>')
    print('<label for="from_latitude">From latitude:</label>')
    print('<input type="text" id="from_latitude" name="from_latitude"><br><br>')
    print('<label for="from_longitude">From longitude:</label>')
    print('<input type="text" id="from_longitude" name="from_longitude"><br><br>')
    print('<label for="to_latitude">To latitude:</label>')
    print('<input type="text" id="to_latitude" name="to_latitude"><br><br>')
    print('<label for="to_longitude">To longitude:</label>')
    print('<input type="text" id="to_longitude" name="to_longitude"><br><br>')
    print('<label for="skipper">Skipper:</label>')
    print('<input type="text" id="skipper" name="skipper"><br><br>')
    print('<label for="reservation_start_date">Reservation Start Date:</label>')
    print('<input type="date" id="reservation_start_date" name="reservation_start_date"><br><br>')
    print('<label for="reservation_end_date">Reservation End Date:</label>')
    print('<input type="date" id="reservation_end_date" name="reservation_end_date"><br><br>')
    print('<label for="boat_country">Boat Country:</label>')
    print('<input type="text" id="boat_country" name="boat_country"><br><br>')
    print('<label for="cin">CIN:</label>')
    print('<input type="text" id="cin" name="cin"><br><br>')
    print('<input type="submit" value="Remove trip">')
    print('</form>')
    
    # d.4) List available locations
    print('<h2>d.4) List all locations</h2>')
    cursor.execute('SELECT * FROM reservation;')
    print('<table border="1" style="width:100%" align="center">')
    print('<tr>')
    print('<th>Latitude</th>')
    print('<th>Longitude</th>')
    print('<th>Name</th>')
    print('<th>Country Name</th>')
    print('</tr>')
    for row in cursor:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('</tr>')
    print('</table>')
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
