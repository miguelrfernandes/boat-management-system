#!/usr/bin/python3
import cgi
import psycopg2
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#List, register, and remove trips 
print('<h1>Trips</h1>')

#Go back to the main page
print('<div class="go_initial">')
print('<a href="app.cgi">Go back to the initial page</a>')
print('</div>')

#Go to the reservations page
print('<div class="go_reservations">')
print('<a href="reservations.cgi">Go back to the reservations page</a>')
print('</div>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

connection = None
try:
    connection = psycopg2.connect(login.dsn)
    print('<footer>Connected to Postgres on ', login.host, ' as user ', login.IST_ID, ' on database ', login.db_name, ' at ', login.datetime.datetime.now(), '</footer>')
    connection.autocommit = False
    cursor = connection.cursor()

    form = cgi.FieldStorage()
    action = form.getvalue('action')

    reservation_start_date = login.datetime.datetime.strptime(str(form.getvalue('start_date')), '%Y-%m-%d').date()
    reservation_end_date = login.datetime.datetime.strptime(str(form.getvalue('end_date')), '%Y-%m-%d').date()
    boat_country = form.getvalue('boat_country')
    cni = form.getvalue('cni')
    responsible = form.getvalue('responsible')

    if action == 'create_trip':
        takeoff = form.getvalue('takeoff')
        arrival = form.getvalue('arrival')
        insurance = form.getvalue('insurance')
        from_latitude = form.getvalue('from_latitude')
        from_longitude = form.getvalue('from_longitude')
        to_latitude = form.getvalue('to_latitude')
        to_longitude = form.getvalue('to_longitude')
        skipper = form.getvalue('skipper')

        sql = """
            INSERT INTO trip (takeoff, arrival, insurance, from_latitude, from_longitude, to_latitude, to_longitude, skipper, reservation_start_date, reservation_end_date, boat_country, cni)
            VALUES (%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s, %(param_6)s, %(param_7)s, %(param_8)s, %(param_9)s, %(param_10)s, %(param_11)s, %(param_12)s);
        """
        data = {'param_1': takeoff, 'param_2': arrival, 'param_3': insurance, 'param_4': from_latitude, 'param_5': from_longitude, 'param_6': to_latitude, 'param_7': to_longitude, 'param_8': skipper, 'param_9': reservation_start_date, 'param_10': reservation_end_date, 'param_11': boat_country, 'param_12': cni}
        cursor.execute(sql, data)
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

        sql = """
            DELETE FROM trip
            WHERE takeoff = %(param_1)s AND arrival = %(param_2)s AND insurance = %(param_3)s AND from_latitude = %(param_4)s AND from_longitude = %(param_5)s AND to_latitude = %(param_6)s AND to_longitude = %(param_7)s AND skipper = %(param_8)s AND reservation_start_date = %(param_9)s AND reservation_end_date = %(param_10)s AND boat_country = %(param_11)s AND cni = %(param_12)s;
        """
        data = {'param_1': takeoff, 'param_2': arrival, 'param_3': insurance, 'param_4': from_latitude, 'param_5': from_longitude, 'param_6': to_latitude, 'param_7': to_longitude, 'param_8': skipper, 'param_9': reservation_start_date, 'param_10': reservation_end_date, 'param_11': boat_country, 'param_12': cni}
        cursor.execute(sql, data)
        connection.commit()
        print('<p>Trip deleted successfully.</p>')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Info about the current reservation
    print('<h3>Reservation info</h3>')
    print('<table>')
    print('<tr>')
    print('<th>Start Date</th>')
    print('<th>End Date</th>')
    print('<th>Boat Country</th>')
    print('<th>CIN</th>')
    print('<th>Responsible</th>')
    print('</tr>')
    print('<tr>')
    print('<td>{}</td>'.format(reservation_start_date))
    print('<td>{}</td>'.format(reservation_end_date))
    print('<td>{}</td>'.format(boat_country))
    print('<td>{}</td>'.format(cni))
    print('<td>{}</td>'.format(responsible))
    print('<tr>')
    print('</table>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------    

    #List the trips for that reservation
    sql = """
        SELECT takeoff, arrival, insurance, from_latitude, from_longitude, to_latitude, to_longitude, skipper, arrival-takeoff
        FROM trip 
        WHERE reservation_start_date = %(param_1)s AND reservation_end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s
        ORDER by takeoff;
    """
    data = {'param_1': reservation_start_date, 'param_2': reservation_end_date, 'param_3': boat_country, 'param_4': cni}
    cursor.execute(sql, data)
    trips = cursor.fetchall()

    print('<h3>Trips for this reservation</h3>')
    print('<table>')
    print('<tr>')
    print('<th>Takeoff</th>')
    print('<th>Arrival</th>')
    print('<th>Duration</th>')
    print('<th>Insurance</th>')
    print('<th>From Latitude</th>')
    print('<th>From Longitude</th>')
    print('<th>To Latitude</th>')
    print('<th>To Longitude</th>')
    print('<th>Skipper</th>')
    print('<th></th>')
    print('<th></th>')
    print('</tr>')
    for row in trips:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[8], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('<td>', row[4], '</td>')
        print('<td>', row[5], '</td>')
        print('<td>', row[6], '</td>')
        print('<td>', row[7], '</td>')
        
        print('<td><a style="color:#1674d1; text-decoration:underline; width:auto;" href="view.cgi?start_date={}&end_date={}&boat_country={}&cni={}&responsible={}&takeoff={}"> Important Info </a></td>'.format(reservation_start_date, reservation_end_date, boat_country, cni, responsible, row[0]) )

        print('<td>')
        print('<form action="trips.cgi" method="post">')
        print('<input type="hidden" name="action" value="delete_trip">')
        print('<input type="button" value="Remove this trip" onclick="this.form.submit()">')
        print('<input type="hidden" name="start_date" value="{}">'.format(reservation_start_date))
        print('<input type="hidden" name="end_date" value="{}">'.format(reservation_end_date))
        print('<input type="hidden" name="boat_country" value="{}">'.format(boat_country))
        print('<input type="hidden" name="cni" value="{}">'.format(cni))
        print('<input type="hidden" name="takeoff" value="{}">'.format(row[0]))
        print('<input type="hidden" name="arrival" value="{}">'.format(row[1]))
        print('<input type="hidden" name="insurance" value="{}">'.format(row[2]))
        print('<input type="hidden" name="from_latitude" value="{}">'.format(row[3]))
        print('<input type="hidden" name="from_longitude" value="{}">'.format(row[4]))
        print('<input type="hidden" name="to_latitude" value="{}">'.format(row[5]))
        print('<input type="hidden" name="to_longitude" value="{}">'.format(row[6]))
        print('<input type="hidden" name="skipper" value="{}">'.format(row[7]))
        print('</form>')
        print('</td>')
        
        print('<tr>')
    print('</table>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #Create trip
    cursor.execute("""
        SELECT latitude 
        FROM location 
        ORDER by latitude;
    """)
    latitude = cursor.fetchall()

    cursor.execute("""
        SELECT longitude 
        FROM location 
        ORDER by longitude;
    """) 
    longitude = cursor.fetchall()

    sql = """
        (SELECT firstname, surname, email 
        FROM authorised a JOIN sailor s 
            ON a.sailor = s.email 
        WHERE start_date = %(param_1)s AND end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s
        )
        INTERSECT
        (SELECT firstname, surname, email 
        FROM sailing_certificate sc JOIN sailor s 
            ON sc.sailor = s.email 
        WHERE boat_class = (
            SELECT boat_class 
            FROM boat
            WHERE country = %(param_5)s AND cni = %(param_6)s
        ));
    """
    data = {'param_1': reservation_start_date, 'param_2': reservation_end_date, 'param_3': boat_country, 'param_4': cni, 'param_5': boat_country, 'param_6': cni}
    cursor.execute(sql, data)    
    skippers = cursor.fetchall()

    print('<h3>Create trip</h3>')
    print('<form action="trips.cgi" method="post">')
    print('<input type="hidden" name="action" value="create_trip">')
    print('<input type="hidden" name="start_date" value="{}">'.format(reservation_start_date))
    print('<input type="hidden" name="end_date" value="{}">'.format(reservation_end_date))
    print('<input type="hidden" name="boat_country" value="{}">'.format(boat_country))
    print('<input type="hidden" name="cni" value="{}">'.format(cni))
    print('<table>')
    print('<tr>')
    print('<th><label for="takeoff">Takeoff</label></th>')
    print('<th><label for="arrival">Arrival</label></th>')
    print('<th><label for="insurance">Insurance</label></th>')
    print('<th><label for="from_latitude">From Latitude</label></th>')
    print('<th><label for="from_longitude">From Longitude</label></th>')
    print('<th><label for="to_latitude">To Latitude</label></th>')
    print('<th><label for="to_longitude">To Longitude</label></th>')
    print('<th><label for="skipper">Skipper Email</label></th>')
    print('</tr>')
    print('<tr>')
    print('<td><input type="date" id="takeoff" name="takeoff"></td>')
    print('<td><input type="date" id="arrival" name="arrival"></td>')
    print('<td><input type="text" id="insurance" name="insurance"></td>')
    
    print('<td><select id="from_latitude" name="from_latitude">')
    print('<option value=""></option>')
    for row in latitude:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')

    print('<td><select id="from_longitude" name="from_longitude">')
    print('<option value=""></option>')
    for row in longitude:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')

    print('<td><select id="to_latitude" name="to_latitude">')
    print('<option value=""></option>')
    for row in latitude:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')

    print('<td><select id="to_longitude" name="to_longitude">')
    print('<option value=""></option>')
    for row in longitude:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')

    print('<td><select id="skipper" name="skipper">')
    print('<option value=""></option>')
    for row in skippers:
        print('<option value="{}">{}</option>'.format(row[2], row[2]))
    print('</select>')
    print('</td>')
    
    print('</tr>')
    print('</table>')
    print('<input type="submit" value="Create Trip">')
    print('</form>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #List available locations
    cursor.execute("""
        SELECT * 
        FROM location
        ORDER by country_name, name;
    """)
    locations = cursor.fetchall()

    print('<h3>All available locations</h3>')
    print('<table>')
    print('<tr>')
    print('<th>Latitude</th>')
    print('<th>Longitude</th>')
    print('<th>Name</th>')
    print('<th>Country Name</th>')
    print('</tr>')
    for row in locations:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('</tr>')
    print('</table>')
    print('<br><br>')
    
    cursor.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

except Exception as e:
    print('<h1>An error has occurred:</h1>')
    print('<p>', e, '</p>')

finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')
