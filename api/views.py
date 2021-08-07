from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

# Create your views here.
# 20 ids 
ids = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
]
# 20 firstnames
firstnames = [
'John', 
'Jane', 
'Corey', 
'Travis', 
'Dave', 
'Kurt', 
'Neil', 
'Sam', 
'Steve', 
'Tom', 
'James', 
'Robert', 
'Michael', 
'Charles', 
'Joe', 
'Mary', 
'Maggie', 
'Nicole', 
'Patricia',
'Linda', ]
# 20 lastnames
lastnames = [
'Smith', 
'Doe', 
'Jenkins', 
'Robinson', 
'Davis', 
'Stuart', 
'Jefferson', 
'Jacobs', 
'Wright', 
'Patterson', 
'Wilks', 
'Arnold', 
'Johnson', 
'Williams',
'Jones', 
'Brown', 
'Davis', 
'Miller', 
'Wilson', 
'Moore', ]
# 20 emails
emails = [
'inico@me.com',
'squirrel@att.net',
'drolsky@hotmail.com',
'rohitm@outlook.com',
'earmstro@aol.com',
'pappp@yahoo.com',
'mkearl@live.com',
'tubesteak@msn.com',
'sopwith@mac.com',
'johnbob@msn.com',
'muzzy@me.com',
'bescoto@msn.com',
'rfisher@msn.com',
'wortmanj@yahoo.ca',
'niknejad@optonline.net',
'mhouston@hotmail.com',
'dbrobins@msn.com',
'helger@me.com',
'redingtn@sbcglobal.net',
'goresky@msn.com',
]
# 20 phone numbers
phonenumbers = [
'9916516439',
'9938054898',
'9179763151',
'9560596714',
'9196481151',
'8241384247',
'8685890358',
'8071227748',
'8315297029',
'9659075392',
'9385776177',
'8140537952',
'9218066277',
'9819827827',
'9458872640',
'8845364329',
'9214729348',
'9363836694',
'9748259479',
'8925714988',
]
# 20 date of birth
dob = [
'5/6/2000',
'6/3/1999',
'2/28/1999',
'3/3/1999',
'5/6/1998',
'2/28/1998',
'3/3/1998',
'5/6/1997',
'2/28/1997',
'3/3/1997',
'5/6/1996',
'2/28/1996',
'3/3/1996',
'5/6/1995',
'2/28/1995',
'3/3/1995',
'5/6/1994',
'2/28/1994',
'3/3/1994',
'5/6/1993',
]
age =[]
for i in dob :
    age.append(int(2021)-int(i[-4:]))

class userList (APIView):


    def get(self, request):
        pk = request.query_params.get('id', None)
        first = request.query_params.get('firstname', None)
        last = request.query_params.get('lastname', None)
        emailid = request.query_params.get('email', None)
        phone = request.query_params.get('phonenumber', None)
        date = request.query_params.get('dob', None)
        old = request.query_params.get('age', None)

        users = zip(ids,firstnames, lastnames, emails, phonenumbers, dob, age)

        if pk==None and first==None and last==None and emailid==None and phone==None and date==None and old==None:
            #Return all users information 
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users] 

        elif pk!=None and first==None and last==None and emailid==None and phone==None and date==None and old==None:
            #Return a single user information
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if ids==int(pk)]

        elif pk==None and first!=None and last==None and emailid==None and phone==None and date==None and old==None:
            #Return all users information with a specific firstname
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if firstnames==first]
        
        elif pk==None and first==None and last!=None and emailid==None and phone==None and date==None and old==None:
            #Return all users information with a specific lastname
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if lastnames==last]
        
        elif pk==None and first==None and last==None and emailid!=None and phone==None and date==None and old==None:
            #Return all users information with a specific emailid
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if emails==emailid]
        
        elif pk==None and first==None and last==None and emailid==None and phone!=None and date==None and old==None:
            #Return all users information with a specific phone number
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if phonenumbers==phone]
        
        elif pk==None and first==None and last==None and emailid==None and phone==None and date!=None and old==None:
            #Return all users information with a specific date of birth
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if dob==date]
        
        elif pk==None and first==None and last==None and emailid==None and phone==None and date==None and old!=None:
            #Return all users information with a specific age
            users = [{"id": ids, "firstname": firstnames, "lastname": lastnames, "email": emails, "phonenumber": phonenumbers, "dob": dob, "age": age} for ids, firstnames, lastnames, emails, phonenumbers, dob, age in users if age==int(old)]

        if users == []:
            return Response({"message": "No user found"})

        return Response(users, status=status.HTTP_200_OK)
    
    def post(self, request):
        #Adding a new user
        first = request.data.get('firstname', None)
        last = request.data.get('lastname', None)
        emailid = request.data.get('email', None)
        phone = request.data.get('phonenumber', None)
        date = request.data.get('dob', None)
        new_user = [first, last, emailid, phone, date]

        if first == None or last == None or emailid == None or phone == None or date == None:
            return Response({"message": "Please provide all the details"}, status=status.HTTP_400_BAD_REQUEST)

        if len(new_user) != 5:
            return Response({"message": "Please provide all the details"}, status=status.HTTP_400_BAD_REQUEST)

        firstnames.append(first)
        lastnames.append(last)
        emails.append(emailid)
        phonenumbers.append(phone)
        dob.append(date)
        age.append(int(2021)-int(date[-4:]))
        ids.append(len(ids)+1)
        return Response({"message": "User added successfully"}, status=status.HTTP_201_CREATED)

    
    def delete(self, request):
        #Deleting a user
        pk = int(request.query_params.get('id', None))-1
        if pk == None:
            return Response({"message": "Please provide ID of user to be deleted"}, status=status.HTTP_400_BAD_REQUEST)

        del firstnames[pk]
        del lastnames[pk]
        del emails[pk]
        del phonenumbers[pk]
        del dob[pk]
        del age[pk]
        ids= []
        for i in range(len(age)):
            ids.append(i+1)
            
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)

    def put(self, request):
        #Editing a user
        pk = int(request.query_params.get('id', None))-1
        if pk == None:
            return Response({"message": "Please provide ID of user to be edited"}, status=status.HTTP_400_BAD_REQUEST)

        first = request.data.get('firstname', None)
        last = request.data.get('lastname', None)
        emailid = request.data.get('email', None)
        phone = request.data.get('phonenumber', None)
        date = request.data.get('dob', None)

        if first == None or last == None or emailid == None or phone == None or date == None:
            return Response({"message": "Please provide all the details"}, status=status.HTTP_400_BAD_REQUEST)


        firstnames[pk] = first
        lastnames[pk] = last
        emails[pk] = emailid
        phonenumbers[pk] = phone
        dob[pk] = date
        age[pk] = int(2021)-int(date[-4:])
        
        return Response({"message": "User edited successfully"}, status=status.HTTP_200_OK)