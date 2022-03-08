from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sqlite3


@api_view(['GET', 'POST'])
def create_admin(request):
    if request.method == "GET":
        conn = sqlite3.connect('users')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Userlogin where firstname='kal' ")
        allTable = cur.fetchall()
        print(allTable)
        return Response(data={'data': allTable})
    else:
        req_data = request.data
        conn = sqlite3.connect('users')
        cur = conn.cursor()
        Values = [req_data['UserID'],req_data['FirstName'],req_data['LastName'],
                   req_data['Email'],req_data['Password']]
        cur.execute("INSERT INTO Userlogin VALUES (?,?,?,?,?)", Values)
        conn.commit()
        conn.close()
        return Response(data={"data": Values})

