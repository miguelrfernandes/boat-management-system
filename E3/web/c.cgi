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
    if action == 'authorise_sailor':
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        boat_country = form.getvalue('boat_country')
        cni = form.getvalue('cni')
        sailor = form.getvalue('sailor')
        cursor.execute('''
            INSERT INTO authorised
            VALUES (%s, %s, %s, %s, %s);
        ''', (start_date, end_date, boat_country, cni, sailor))
        connection.commit()
        print('<p>Sailor authorisation created successfully.</p>')
    elif action == 'deauthorise_sailor':
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        boat_country = form.getvalue('boat_country')
        cni = form.getvalue('cni')
        sailor = form.getvalue('sailor')
        cursor.execute('''
            DELETE FROM authorised
            WHERE start_date = %s AND end_date = %s AND boat_country = %s AND cni = %s AND sailor = %s;
        ''', (start_date, end_date, boat_country, cni, sailor))
        connection.commit()
        print('<p>Sailor deauthorisation created successfully.</p>')
    
    # Page
    # Go back to the main page
    print('<a href="http://web.tecnico.ulisboa.pt/ist192836/app.cgi"><h1>Go back to the main page</h1></a>')

    # c) Authorise and deauthorise sailors
    print('<h1>c) Authorise and deauthorise sailors</h1>')

    # c.1) Authorise sailor
    print('<h2>c.1) Authorise sailor</h2>')
    print('<form action="c.cgi" method="post">')
    print('<input type="hidden" name="action" value="authorise_sailor">')
    print('<label for="start_date">Start Date:</label>')
    print('<input type="date" id="start_date" name="start_date">')
    print('<label for="end_date">End Date:</label>')
    print('<input type="date" id="end_date" name="end_date">')
    print('<label for="boat_country">Boat Country:</label>')
    print('<input type="text" id="boat_country" name="boat_country">')
    print('<label for="cni">CIN:</label>')
    print('<input type="text" id="cni" name="cni">')
    print('<label for="sailor">Sailor:</label>')
    print('<input type="text" id="sailor" name="sailor">')
    print('<input type="submit" value="Submit">')
    print('</form>')

    # c.2) Deauthorise sailor
    print('<h2>c.2) Deauthorise sailor</h2>')
    print('<form action="c.cgi" method="post">')
    print('<input type="hidden" name="action" value="deauthorise_sailor">')
    print('<label for="start_date">Start Date:</label>')
    print('<input type="date" id="start_date" name="start_date">')
    print('<label for="end_date">End Date:</label>')
    print('<input type="date" id="end_date" name="end_date">')
    print('<label for="boat_country">Boat Country:</label>')
    print('<input type="text" id="boat_country" name="boat_country">')
    print('<label for="cni">CIN:</label>')
    print('<input type="text" id="cni" name="cni">')
    print('<label for="sailor">Sailor:</label>')
    print('<input type="text" id="sailor" name="sailor">')
    print('<input type="submit" value="Submit">')
    print('</form>')

    #Closing connection
    cursor.close()
    connection.close()

    print('<p>Connection closed.</p>')
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>', e, '</p>')

print('</body>')
print('</html>')
