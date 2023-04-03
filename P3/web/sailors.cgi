#!/usr/bin/python3
import cgi
import psycopg2
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#List, create and remove sailors (including junior and senior)
print('<h1>Sailors</h1>')

#Go back to the main page
print('<div class="go_initial">')
print('<a href=app.cgi>Go back to the initial page</a>')
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

    if action == 'create_sailor':
        first_name = form.getvalue('first_name')
        surname = form.getvalue('surname')
        email = form.getvalue('email')
        seniority = form.getvalue('seniority')

        sql = """
            INSERT INTO sailor (firstname, surname, email)
            VALUES (%(param_1)s, %(param_2)s, %(param_3)s);
        """
        data = {'param_1': first_name, 'param_2': surname, 'param_3': email}
        cursor.execute(sql, data)

        if seniority == 'senior':
            sql = """
                INSERT INTO senior (email)
                VALUES (%(param_1)s);
            """
            data = {'param_1': email}
            cursor.execute(sql, data)
        
        elif seniority == 'junior':
            sql = """
                INSERT INTO junior (email)
                VALUES (%(param_1)s);
            """
            data = {'param_1': email}
            cursor.execute(sql, data)
                
        connection.commit()
        print('<p>Sailor created successfully.</p>')
    
    elif action == 'remove_sailor':
        email = form.getvalue('email')
        
        sql = """
            DELETE FROM junior
            WHERE email = %(param_1)s;
        """
        data = {'param_1': email}
        cursor.execute(sql, data)

        sql = """
            DELETE FROM senior
            WHERE email = %(param_1)s;
        """
        data = {'param_1': email}
        cursor.execute(sql, data)
        
        connection.commit()
        print('<p>Sailor removed successfully.</p>')
  
  #-----------------------------------------------------------------------------------------------------------------------------------------------------------     
  
    #List all sailors
    sql = """
        SELECT * 
        FROM sailor
        ORDER BY firstname
    """
    cursor.execute(sql)
    sailors = cursor.fetchall()

    print('<h3>Registered sailors</h3>')
    print('<table>')
    print('<tr>')
    print('<th>Sailor First Name</th>')
    print('<th>Sailor Surname</th>')
    print('<th>Sailor Email</th>')
    print('<th>Sailor Seniority</th>')
    print('<th></th>')
    print('</tr>')
    for row in sailors:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')

        sql = 'SELECT * FROM senior WHERE email = %(param_1)s;'
        data = {'param_1': row[2]}
        cursor.execute(sql, data)
        seniority = "Senior" if cursor.fetchall() != [] else "Junior"
        print('<td>', seniority, '</td>')

        print('<td>')
        print('<form action="sailors.cgi" method="post">')
        print('<input type="hidden" name="action" value="remove_sailor">')
        print('<input type="button" value="Remove this sailor" onclick="this.form.submit()">')
        print('<input type="hidden" name="email" value="{}">'.format(row[2]))
        print('</form>')
        print('</td>')

        print('</tr>')
    print('</table>')
    print('<br>')

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------     

    #Create a new sailor
    print('<h3>Add a sailor</h3>')
    print('<form action="sailors.cgi" method="post">')
    print('<input type="hidden" name="action" value="create_sailor">')
    print('<table>')
    print('<tr>')
    print('<th><label for="first_name">First Name</label></th>')
    print('<th><label for="surname">Surname</label></th>')
    print('<th><label for="email">Email</label></th>')
    print('<th><label for="seniority">Seniority</label></th>')
    print('</tr>')
    print('<tr>')
    print('<td><input type="text" id="first_name" name="first_name"></td>')
    print('<td><input type="text" id="surname" name="surname"></td>')
    print('<td><input type="text" id="email" name="email"></td>')
    print('<td><select id="seniority" name="seniority">')
    print('<option value=""></option>')
    print('<option value="junior">Junior</option>')
    print('<option value="senior">Senior</option>')
    print('</select></td>')
    print('</tr>')
    print('</table>')
    print('<input type="submit" value="Submit">')
    print('</form>')
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


