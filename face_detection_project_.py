'''SINCE DATABASE IS GIVING US QUICK ACCESS TO PICTURES AND GETTING DATA IS MUCH EASIER IN DATABASE THAN  LISTS
THAT'S WHY  WE ARE USING MYSQL DATABSE TO STORE USERS DATA LIKE IMAGES,NAME,ID AND ATTENDENCE DATA'''


import mysql.connector as sql
import os 
import cv2
import  numpy  as np
from datetime import date
from datetime import datetime
import face_recognition
import csv
#connecting with MYSQL DATABASE

connection=sql.connect(
    host='localhost',
    user='root',
    password='*****'
    )
cursor=connection.cursor(buffered=True)

#CREATING DATABASE AND TABLES TO STORE DATA
'''
cursor.execute('CREATE DATABASE pics_of_permitted_users ')
cursor.execute('USE pics_of_permitted_users')
cursor.execute('CREATE TABLE permitted_users_inform(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),image_path VARCHAR(1024))')
cursor.execute('CREATE TABLE Attendence_Record_Table(date VARCHAR(255),name VARCHAR(255),time VARCHAR(255))')
'''

# STORING NAMES AND IMAGES PATH INTO TABLE
'''
path='  write your location of images of permitted users'
for name in mylist:
    pic_path= path+'/'+name
    name_of_user=os.path.splitext(name)[0]
    query='INSERT INTO permitted_users_inform(name,image_path) VALUES(%s,%s)'
    val=(name_of_user,pic_path)
    cursor.execute(query,val)

cursor.execute("SELECT * FROM permitted_users_inform")
'''


# READING AND ENCODING ALL THE IMAGES OF USERS

cursor.execute('USE pics_of_permitted_users')
cursor.execute("SELECT * FROM permitted_users_inform")
# ENCODING THE IMAGES

encoded_images_list=[]
for touple in cursor:
    curr_img=cv2.imread(touple[2]) # GETTING THE INFORMATION OF IMAGES

    curr_img=cv2.cvtColor(curr_img,cv2.COLOR_BGR2RGB)#CONVERTING THE IMAGES INO rgb

    encode=face_recognition.face_encodings(curr_img)[0]
    encoded_images_list.append(encode)    
# getting data from webcam
print('encoding has been done') 
# CREATING FUNCTION WHICH WILL RECORD THE ATTENDENCE DATA

def Attendence(user_name) :
    cursor.execute(' USE pics_of_permitted_users')
       
    dt=date.today()
    dtt=dt.strftime("%Y-%m-%d")
    now=datetime.now()
    tt=now.strftime("%H:%M:%S")
    query='SELECT name FROM Attendence_Record_Table WHERE  name= %s AND date=%s'
    val=(user_name,dtt)
    cursor.execute(query,val)
    result=cursor.fetchone()
    if result is None:
        query='INSERT INTO Attendence_Record_Table(date,name,time) VALUES(%s,%s,%s)'
        val=(dtt,user_name,tt)
        cursor.execute(query,val)
        print('Attendence Recorded')
    connection.commit()
    


cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    reduced_size_img=cv2.resize(img,(0,0),None,0.25,0.25)  # RESIZING THE IMAGE CAPTURED BY WEBCAM
    reduced_size_imag=cv2.cvtColor(reduced_size_img,cv2.COLOR_BGR2RGB)#CONVERTING IT INTO RGB SINCE COLOURS ARE NOT REQUIRED IN IMAGE

    
    face_frame=face_recognition.face_locations(reduced_size_imag)
    encodedframe=face_recognition.face_encodings(reduced_size_imag,face_frame)#ENCODINGS THE IMAGE CAPTURED BY WEBCAM

                                             
                                                     
    for encodeface,faceloc in zip(encodedframe,face_frame):
        matching=face_recognition.compare_faces(encoded_images_list,encodeface)
        
        faceDis=face_recognition.face_distance(encoded_images_list,encodeface)
        matchingindex=np.argmin(faceDis)
        matching_index=matchingindex
        matchingindex+=1

        if  matching[matching_index]:
            
            query='SELECT name FROM permitted_users_inform WHERE id = %s'
            match_index1=matchingindex.item()
            cursor.execute(query,(match_index1,))
            name_of_user=cursor.fetchone()[0]
            name=str(name_of_user).upper() # STORING ATTENDENCE OF PERSON IN ATTENDENCE TABLE

            print(name) 
             # CREATING RECTANGLE OVER THE FACE OF PREDICTED USER AND SHOWING HIS/HER NAME        
   
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4 # multiplying with 4 because we are restoring the size
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2) 
            Attendence(name)
            connection.commit()
            

    cv2.imshow('webcam',img)
    cv2.waitKey(1)
    
''''   
# WE CAN ALSO MAKE A EXCEL FILE AFTER COMPLETING THE ATTENDENCE
cursor.execute('SELECT * FROM Attendence_Record_Table')
with open ("Attendencefile.csv",'w',newline='')as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)
'''     
''' we can also use twilio to message the users when they enter.So that if somehow wrong person enter in the room 
instead of authorised person than the authorised person will came to know through message and report the issue
'''   
''' 
import twilio
from twilio.rest import Client
account_sid = '******2bc5988a68276815ddae526ef7b4'
auth_token = '*******77934b8be9963b22cdac9a74c'
client = Client(account_sid,auth_token )
message = client.messages.create(body ="Your attendence is marked", from_ = '+***8491', to ='+*****9898')    
'''    
    
    
    
    
    