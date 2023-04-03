#!/usr/bin/python3
import login

print('<body>')

print('<link rel="stylesheet" href="styles.css">')

#Boat Management System Web Application Prototype
print('<h1> Boat Management System</h1>')
print('<img src=https://static.wixstatic.com/media/00c674_b8a26bce17d64671a94c9bdb647826cb~mv2_d_4032_2268_s_2.jpg/v1/fill/w_640,h_458,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/00c674_b8a26bce17d64671a94c9bdb647826cb~mv2_d_4032_2268_s_2.jpg" style=width:350px;height:250px>')

#List, create and remove sailors (including junior and senior)
print('<div class="main">')
print('<a href="sailors.cgi">Sailors</a>')
print('</div>')

#List, create and remove reservations
print('<div class="main">')
print('<a href="reservations.cgi">Reservations and respective Trips</a>')
print('</div>')   

#Queries output
print('<div class="main">')
print('<a href="queries.cgi">Queries Output</a>')
print('</div>')

print('</body>')
print('</html>')
