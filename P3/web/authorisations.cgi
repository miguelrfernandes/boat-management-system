#!/usr/bin/python3
import cgi
import psycopg2
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#Authorise and deauthorise sailors
print('<h1>Authorisations</h1>')

#Go back to the main page
print('<div class="go_initial">')
print('<a href="app.cgi">Go back to the initial page</a>')
print('</div>')

#Go back to the reservations page
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

    start_date = login.datetime.datetime.strptime(str(form.getvalue('start_date')), '%Y-%m-%d').date()
    end_date = login.datetime.datetime.strptime(str(form.getvalue('end_date')), '%Y-%m-%d').date()
    cni = form.getvalue('cni')
    boat_country = form.getvalue('boat_country')
    responsible = form.getvalue('responsible')
    
    if action == 'authorise_sailor':
        sailor = form.getvalue('sailor')
        sql = """
            INSERT INTO authorised (start_date, end_date, boat_country, cni, sailor)
            VALUES (%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s);
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': boat_country, 'param_4': cni, 'param_5': sailor}
        cursor.execute(sql, data)
        connection.commit()
        print('<p>Sailor authorisation created successfully.</p>')
    
    elif action == 'deauthorise_sailor':
        sailor = form.getvalue('sailor')
        sql = """
            DELETE FROM authorised
            WHERE start_date = %(param_1)s AND end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s AND sailor = %(param_5)s;
        """
        data = {'param_1': start_date, 'param_2': end_date, 'param_3': boat_country, 'param_4': cni, 'param_5': sailor}
        cursor.execute(sql, data)
        connection.commit()
        print('<p>Sailor deauthorisation created successfully.</p>')
    
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
    print('<td>{}</td>'.format(start_date))
    print('<td>{}</td>'.format(end_date))
    print('<td>{}</td>'.format(boat_country))
    print('<td>{}</td>'.format(cni))
    print('<td>{}</td>'.format(responsible))
    print('<tr>')
    print('</table>')
    print('<br>')

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #List the authorised sailors for that reservation
    sql = """
        SELECT firstname, surname, email 
        FROM authorised a JOIN sailor s 
            ON a.sailor = s.email 
        WHERE start_date = %(param_1)s AND end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s
        ORDER by firstname;
    """
    data = {'param_1': start_date, 'param_2': end_date, 'param_3': boat_country, 'param_4': cni}
    cursor.execute(sql, data)
    authorised = cursor.fetchall()
   
    authorised_emails = []

    print('<h3>Authorised sailors for this reservation</h3>')
    print('<table>')
    print('<tr>')
    print('<th>First Name</th>')
    print('<th>Surname</th>')
    print('<th>Email</th>')
    print('</tr>')
    for index, row in enumerate(authorised):
        authorised_emails.append(row[2])
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<tr>')
    print('</table>')
    print('<br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #List all sailors
    sql = """
        SELECT * 
        FROM sailor
        ORDER BY firstname
    """
    cursor.execute(sql)
    sailors = cursor.fetchall()

    sql = """
        SELECT skipper, takeoff
        FROM trip
        WHERE reservation_start_date = %(param_1)s AND reservation_end_date = %(param_2)s AND boat_country = %(param_3)s AND cni = %(param_4)s;
    """
    data = {'param_1': start_date, 'param_2': end_date, 'param_3': boat_country, 'param_4': cni}
    cursor.execute(sql, data)
    skippers = cursor.fetchall()
    skipper_emails = []

    for row in skippers:
        skipper_emails.append(row[0])
    skipper_emails = list(set(skipper_emails))
    
    print('<h3>All sailors</h3>')
    print('<table>')
    print('<tr>')
    print('<th>First name</th>')
    print('<th>Surname</th>')
    print('<th>Email</th>')
    print('<th>Is Authorised</th>')
    print('</tr>')
    for row in sailors:
        status = "Yes" if row[2] in authorised_emails else "No"
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')

        print('<td>')
        print('<form action="authorisations.cgi" method="post">')
        print('<div class=radio>')
        
        if status == 'Yes':
            print('<input type="hidden" name="action" value="deauthorise_sailor">')
            print('<input type="radio" id="yes" name="{}_status" value="yes" checked>'.format(row[2]))
            print('<label for="yes">Yes</label>')
            if row[2] not in skipper_emails and row[2] != responsible:
                print('<input type="radio" id="no" name="{}_status" value="no" onchange="this.form.submit()">'.format(row[2]))
            else:
                print('<input type="radio" id="no" name="{}_status" value="no" disabled>'.format(row[2]))
            print('<label for="no">No</label>')
        else:
            print('<input type="hidden" name="action" value="authorise_sailor">')
            print('<input type="radio" id="yes" name="{}_status" value="yes" onchange="this.form.submit()">'.format(row[2]))
            print('<label for="yes">Yes</label>')
            print('<input type="radio" id="no" name="{}_status" value="no" checked>'.format(row[2]))
            print('<label for="no">No</label>')
            
        print('<input type="hidden" name="start_date" value="{}">'.format(start_date))
        print('<input type="hidden" name="end_date" value="{}">'.format(end_date))
        print('<input type="hidden" name="boat_country" value="{}">'.format(boat_country))
        print('<input type="hidden" name="cni" value="{}">'.format(cni))
        print('<input type="hidden" name="responsible" value="{}">'.format(responsible))
        print('<input type="hidden" name="sailor" value="{}">'.format(row[2]))
        
        print('</div>')
        print('</form>')
        print('</td>')
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
