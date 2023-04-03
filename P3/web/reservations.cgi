#!/usr/bin/python3
import cgi
import psycopg2
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#List, create and remove reservations
print('<h1>Reservations</h1>')
    
#Go back to the main page
print('<div class="go_initial">')
print('<a href="app.cgi">Go back to the initial page</a>')
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

    if action == 'create_reservation':
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        boat_country = form.getvalue('country')
        cni = form.getvalue('cni')
        responsible = form.getvalue('responsible')

        sql = """
            INSERT INTO date_interval (start_date, end_date)
            SELECT * FROM (SELECT CAST(%(param_1)s AS DATE) AS start_date, CAST(%(param_2)s AS DATE) AS end_date) AS d
            WHERE NOT EXISTS(
                SELECT start_date, end_date FROM date_interval WHERE start_date = %(param_3)s AND end_date = %(param_4)s
            );
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': start_date, 'param_4': end_date}
        cursor.execute(sql, data)
        
        sql = """
            INSERT INTO reservation (start_date, end_date, country, cni, responsible)
            VALUES (%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s);
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': boat_country, 'param_4': cni, 'param_5': responsible}
        cursor.execute(sql, data)

        sql = """
            INSERT INTO authorised (start_date, end_date, boat_country, cni, sailor)
            VALUES (%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s);
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': boat_country, 'param_4': cni, 'param_5': responsible}
        cursor.execute(sql, data)

        connection.commit()
        print('<p>Reservation created successfully.</p>')
    
    elif action == 'remove_reservation':
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')

        sql = """
        SELECT firstname, surname, email 
        FROM authorised a JOIN sailor s 
            ON a.sailor = s.email 
        WHERE start_date = %(param_1)s AND end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s
        ORDER by firstname;
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': country, 'param_4': cni}
        cursor.execute(sql, data)
        authorised = cursor.fetchall()
        num_authorised = 0

        sql = """
            DELETE FROM authorised
            WHERE start_date = %(param_1)s AND end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s;
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': country, 'param_4': cni}

        for row in authorised:
            num_authorised += 1
        
        if(num_authorised == 1):
            cursor.execute(sql, data)
        
        sql = """
            DELETE FROM reservation
            WHERE start_date = %(param_1)s AND end_date = %(param_2)s AND country = %(param_3)s AND cni = %(param_4)s;
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': country, 'param_4': cni}
        cursor.execute(sql, data)
        
        connection.commit()
        print('<p>Reservation removed successfully.</p>')
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #List all reservations
    cursor.execute("""
        SELECT * FROM reservation
        ORDER by start_date;
    """)
    reservations = cursor.fetchall()
    
    print('<h3>Registered reservations</h3>')
    print('<table>')
    print('<tr>')
    print('<th>Start Date</th>')
    print('<th>End Date</th>')
    print('<th>Boat Country</th>')
    print('<th>CNI</th>')
    print('<th>Responsible</th>')
    print('<th>Authorised Sailors</th>')
    print('<th>Associated Trips</th>')
    print('<th></th>')
    print('</tr>')
    for row in reservations:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('<td>', row[4], '</td>')
        print('<td><a style="color:#1674d1;text-decoration: underline" href="authorisations.cgi?start_date={}&end_date={}&boat_country={}&cni={}&responsible={}">Click to see</a></td>'.format(row[0],row[1],row[2],row[3],row[4]) )
        print('<td><a style="color:#1674d1;text-decoration: underline" href="trips.cgi?start_date={}&end_date={}&boat_country={}&cni={}&responsible={}">Click to see</a></td>'.format(row[0],row[1],row[2],row[3],row[4]) )

        print('<td>')
        print('<form action="reservations.cgi" method="post">')
        print('<input type="hidden" name="action" value="remove_reservation">')
        print('<input type="button" value="Remove this reservation" onclick="this.form.submit()">')
        print('<input type="hidden" name="start_date" value="{}">'.format(row[0]))
        print('<input type="hidden" name="end_date" value="{}">'.format(row[1]))
        print('<input type="hidden" name="country" value="{}">'.format(row[2]))
        print('<input type="hidden" name="cni" value="{}">'.format(row[3]))
        print('</form>')
        print('</td>')
        print('<tr>')
    print('</table>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #Create a reservation
    cursor.execute("""
        SELECT name, country, cni, boat_class
        FROM boat 
        ORDER BY country;
    """)
    boats = cursor.fetchall()

    cursor.execute("""
        SELECT DISTINCT country
        FROM boat;
    """)
    boat_countries = cursor.fetchall()

    cursor.execute("""
        SELECT DISTINCT cni
        FROM boat;
    """)
    boat_cni = cursor.fetchall()

    cursor.execute("""
        SELECT email 
        FROM senior;
    """)
    responsibles = cursor.fetchall()

    print('<h3>Create a reservation</h3>')
    print('<form action="reservations.cgi" method="post">')
    print('<input type="hidden" name="action" value="create_reservation">')
    print('<table>')
    print('<tr>')
    print('<th><label for="start_date">Start Date</label></th>')
    print('<th><label for="end_date">End Date</label></th>')
    print('<th><label for="country">Boat Country</label></th>')
    print('<th><label for="cni">CIN</label></th>')
    print('<th><label for="responsible">Responsible Email</label></th>')
    print('</tr>')
    print('<tr>')
    print('<td><input type="date" id="start_date" name="start_date"></td>')
    print('<td><input type="date" id="end_date" name="end_date"></td>')

    print('<td><select id="country" name="country">')
    print('<option value=""></option>')                                
    for row in boat_countries:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')

    print('<td><select id="cni" name="cni">')
    print('<option value=""></option>')
    for row in boat_cni:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')
    
    print('<td><select id="responsible" name="responsible">')
    print('<option value=""></option>')
    for row in responsibles:
        print('<option value="{}">{}</option>'.format(row[0], row[0]))
    print('</select>')
    print('</td>')

    print('</tr>')
    print('</table>')
    print('<input type="submit" value="Submit">')
    print('</form>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #List boats info
    print('<h3>Available boats</h3>')
    print('<table>')
    print('<tr>')
    print('<th>Name</th>')
    print('<th>Country</th>')
    print('<th>CIN</th>')
    print('<th>Class</th>')
    print('</tr>')
    for row in boats:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('</tr>')
    print('</table>')
    print('<br><br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    cursor.close()

except Exception as e:
    print('<h1>An error has occurred:</h1>')
    print('<p>', e, '</p>')

finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')
