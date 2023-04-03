#!/usr/bin/python3
import cgi
import psycopg2
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#View
print('<h3>Summary of the most important information about this trip</h3>')

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
    takeoff = form.getvalue('takeoff')

    #Go to the trips page
    print('<div class="go_trips">')
    print('<a href="trips.cgi?start_date={}&end_date={}&boat_country={}&cni={}&responsible={}">Go back</a>'.format(reservation_start_date, reservation_end_date, boat_country, cni, responsible))
    print('</div>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #Trip info (obtained from the created view)
    sql = """
        SELECT *
        FROM trip_info
        WHERE trip_start_date = %(param_1)s AND country_name_boat = %(param_2)s AND cni_boat = %(param_3)s;
    """
    data = {'param_1': takeoff, 'param_2': boat_country, 'param_3': cni}
    cursor.execute(sql, data)
    trip = cursor.fetchall()

    print('<table>')
    print('<tr>')
    print('<th colspan="3">Origin</th>')
    print('<th colspan="3">Destination</th>')
    print('<th colspan="3">Boat</th>')
    print('<th>Dates</th>')
    print('</tr>')

    print('<tr>')
    print('<th>Country ISO</th>')
    print('<th>Country Name</th>')
    print('<th>Location Name</th>')
    print('<th>Country ISO</th>')
    print('<th>Country Name</th>')
    print('<th>Location Name</th>')
    print('<th>CNI</th>')
    print('<th>Country ISO</th>')
    print('<th>Name</th>')
    print('<th>Takeoff</th>')
    print('</tr>')
    
    for row in trip:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[4], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('<td>', row[5], '</td>')
        print('<td>', row[6], '</td>')
        print('<td>', row[7], '</td>')
        print('<td>', row[8], '</td>')
        print('<td>', row[9], '</td>')
        print('</tr>')

    print('</table>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

except Exception as e:
    print('<h1>An error has occurred:</h1>')
    print('<p>', e, '</p>')

finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')
