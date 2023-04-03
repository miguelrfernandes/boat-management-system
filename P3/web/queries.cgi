#!/usr/bin/python3
import cgi
import psycopg2
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#List, create and remove reservations
print('<h1>Queries Output</h1>')
    
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    print('<script>')
    print('function q1() {')
    print('var x = document.getElementById("query1");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')

    print('<script>')
    print('function q2() {')
    print('var x = document.getElementById("query2");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')

    print('<script>')
    print('function q3() {')
    print('var x = document.getElementById("query3");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')

    print('<script>')
    print('function q4() {')
    print('var x = document.getElementById("query4");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')

    print('<script>')
    print('function q5() {')
    print('var x = document.getElementById("query5");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')

    print('<script>')
    print('function analytics1() {')
    print('var x = document.getElementById("analytics1");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')

    print('<script>')
    print('function analytics2() {')
    print('var x = document.getElementById("analytics2");')
    print('if (x.style.display === "none") {')
    print('    x.style.display = "block";')
    print('} else {')
    print('   x.style.display = "none";')
    print('}')
    print('}')
    print('</script>')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Query 1
    cursor.execute("""
        SELECT country, COUNT(*)
        FROM boat
        GROUP by country
        HAVING COUNT(*) >= ALL(
            SELECT COUNT(*)
            FROM boat
            GROUP by country
        );
    """)
    query1 = cursor.fetchall()

    print('<button onclick="q1()">Which country has more boats registered than any other?</button>')

    print('<div id="query1" style="display:none">')
    print('<table>')
    print('<tr>')
    print('<th style="width:50%;">Country</th>')
    print('<th style="width:50%;">Number of Boats</th>')
    print('</tr>')
    for row in query1:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')
    print('</div>')
    print('<br><br>')
 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Query 2
    cursor.execute("""
        SELECT sailor, COUNT(*)
        FROM sailing_certificate 
        GROUP by sailor
        HAVING COUNT(*) >= 2;
    """)
    query2 = cursor.fetchall()

    print('<button onclick="q2()">Who are the sailors that have at least two certificates?</button>')

    print('<div id="query2" style="display:none">')
    print('<table>')
    print('<tr>')
    print('<th style="width:50%;">Sailor Email</th>')
    print('<th style="width:50%;">Number of Certificates</th>')
    print('</tr>')
    for row in query2:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')
    print('</div>')
    print('<br><br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Query 3
    cursor.execute("""
        SELECT DISTINCT skipper
        FROM trip t1
        WHERE NOT EXISTS(
            SELECT (latitude, longitude)
            FROM location
            WHERE country_name = 'Portugal'
            EXCEPT(
                SELECT (to_latitude, to_longitude)
                FROM trip t2
                WHERE t2.skipper = t1.skipper
            )
        );
    """)
    query3 = cursor.fetchall()

    print('<button onclick="q3()">Who are the sailors that have sailed to every location in Portugal?</button>')
    
    print('<div id="query3" style="display:none">')
    print('<table>')
    print('<tr>')
    print('<th>Sailor Email</th>')
    print('</tr>')
    for row in query3:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')
    print('</div>')
    print('<br><br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Query 4
    cursor.execute("""
        SELECT skipper, COUNT(*)
        FROM trip
        GROUP by skipper
        HAVING COUNT(*) >= ALL(
            SELECT COUNT(*)
            FROM trip
            GROUP by skipper
        );
    """)
    query4 = cursor.fetchall()

    print('<button onclick="q4()">Who are the sailors with the most skipped trips?</button>')

    print('<div id="query4" style="display:none">')
    print('<table>')
    print('<tr>')
    print('<th>Sailor Email</th>')
    print('<th>Number of skipped trips</th>')
    print('</tr>')
    for row in query4:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('</tr>')
    print('</table>')
    print('<br>')
    print('</div>')
    print('<br><br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Query 5
    cursor.execute("""
        SELECT reservation_start_date, reservation_end_date, boat_country, cni, skipper, sum(arrival-takeoff) AS total
        FROM trip t1
        GROUP BY (reservation_start_date, reservation_end_date, boat_country, skipper, cni)
        HAVING SUM(t1.arrival - t1.takeoff) >= ALL(
            SELECT SUM(t2.arrival-t2.takeoff)
            FROM trip t2
            WHERE t2.reservation_start_date = t1.reservation_start_date AND t2.reservation_end_date = t1.reservation_end_date AND t2.boat_country = t1.boat_country AND t2.cni = t1.cni
            GROUP BY (reservation_start_date, reservation_end_date, boat_country, skipper, cni)
        )
        ORDER BY reservation_start_date;
    """)
    query5 = cursor.fetchall()

    print('<button onclick="q5()">Who are the sailors with the longest duration of trips for the same single reservation?</button>')

    print('<div id="query5" style="display:none">')
    print('<table>')
    print('<tr>')
    print('<th>Reservation Start Date</th>')
    print('<th>Reservation End Date</th>')
    print('<th>Boat Country</th>')
    print('<th>CIN</th>')
    print('<th>Skipper</th>')
    print('<th>Duration</th>')
    print('</tr>')
    for row in query5:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('<td>', row[1], '</td>')
        print('<td>', row[2], '</td>')
        print('<td>', row[3], '</td>')
        print('<td>', row[4], '</td>')
        print('<td>', row[5], '</td>')
        print('</tr>')
    print('</table>')
    print('<br><br>')
    print('</div>')
    print('<br><br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Data Analytics - Query 1
    cursor.execute("""
        SELECT
            EXTRACT (YEAR FROM trip_start_date) AS year,
            EXTRACT (MONTH FROM trip_start_date) AS month,
            EXTRACT (DAY FROM trip_start_date) AS day,
            COUNT (*)
        FROM trip_info
        GROUP BY GROUPING SETS((year), (month), (year, month, day))
        ORDER BY year, month, day;
    """)
    analytics1 = cursor.fetchall()

    print('<button onclick="analytics1()">Analysis of the total number of trips depending on the start date </button>')
    
    print('<div id="analytics1" style="display:none">')

    print('<table>')
    print('<tr>')
    print('<th style="width:25%;">Year</th>')
    print('<th style="width:25%;">Month</th>')
    print('<th style="width:25%;">Day</th>')
    print('<th style="width:25%;">Number of trips</th>')
    print('</tr>')
    for row in analytics1:
        row = list(row)

        if row[0] is not None:
            row[0] = int(row[0])
        
        if row[1] is not None:
            row[1] = int(row[1])

        if row[2] is not None:
            row[2] = int(row[2])
        
        print('<tr>')

        if row[0] is not None and row[1] is None and row[2] is None:
            row[1] = ''
            row[2] = ''
            print('<td style="background-color: #B0C4DE;">', row[0], '</td>')
            print('<td style="background-color: #B0C4DE;">', row[1], '</td>')
            print('<td style="background-color: #B0C4DE;">', row[2], '</td>')
            print('<td style="background-color: #B0C4DE;">', row[3], '</td>')
            
        
        elif row[0] is None and row[1] is not None and row[2] is None:
            row[0] = ''
            row[2] = ''
            print('<td style="background-color: white">', row[0], '</td>')
            print('<td style="background-color: #FAF0E6">', row[1], '</td>')
            print('<td style="background-color: #FAF0E6">', row[2], '</td>')
            print('<td style="background-color: #FAF0E6">', row[3], '</td>')
        
        elif row[0] is None and row[1] is None and row[2] is None:
            row[0] = ''
            row[1] = ''
            row[2] = ''
            print('<td style="background-color: #D3D3D3">', row[0], '</td>')
            print('<td style="background-color: #D3D3D3">', row[1], '</td>')
            print('<td style="background-color: #D3D3D3">', row[2], '</td>')
            print('<td style="background-color: #D3D3D3">', row[3], '</td>')
        
        else:
            print('<td>', row[0], '</td>')
            print('<td>', row[1], '</td>')
            print('<td>', row[2], '</td>')
            print('<td>', row[3], '</td>')
        
        print('</tr>')

    print('</table>')
    print('<br>')

    
    print('</div>')
    print('<br><br>')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Data Analytics - Query 2
    cursor.execute("""
        SELECT
            country_name_origin,
            loc_name_origin,
            COUNT (*)
        FROM trip_info
        GROUP BY ROLLUP(country_name_origin, loc_name_origin)
        ORDER BY country_name_origin, loc_name_origin;
    """)
    analytics2 = cursor.fetchall()

    print('<button onclick="analytics2()">Analysis of the total number of trips depending on the location of origin</button>')
    
    print('<div id="analytics2" style="display:none">')

    print('<table>')
    print('<tr>')
    print('<th style="width:33%;">Country</th>')
    print('<th style="width:33%;">Location</th>')
    print('<th style="width:33%;">Number of trips</th>')
    print('</tr>')
    
    for row in analytics2:
        row = list(row)
        
        print('<tr>')
        
        if row[0] is not None and row[1] is None:
            row[1] = ''
            print('<td style="background-color: #B0C4DE;">', row[0], '</td>')
            print('<td style="background-color: #B0C4DE;">', row[1], '</td>')
            print('<td style="background-color: #B0C4DE;">', row[2], '</td>')
            
        
        elif row[0] is None and row[1] is None:
            row[0] = ''
            row[1] = ''
            print('<td style="background-color: #D3D3D3">', row[0], '</td>')
            print('<td style="background-color: #D3D3D3">', row[1], '</td>')
            print('<td style="background-color: #D3D3D3">', row[2], '</td>')
        
        else:
            print('<td>', row[0], '</td>')
            print('<td>', row[1], '</td>')
            print('<td>', row[2], '</td>')

        print('</tr>')
        
    print('</table>')
    print('<br>')
    
    print('</div>')
    print('<br><br>')
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
