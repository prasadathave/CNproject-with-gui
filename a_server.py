import socket
import os
import time
import pickle
import mysql.connector
from classes import *
# import lepl.apps.rfc3696

UniqueTweets = 1

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = int(input('Enter desired port --> '))

server_socket.bind((ip,port))

server_socket.listen(100)
BUFFERSIZE = 64000
print('Running on IP: '+ip)
print('Running on port: '+str(port))

# Connecting with database
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="123456789",
                                database="Minitweet",
                                )

def SignUp(conn, addr, data):
    # emailchecker = lepl.apps.rfc3696.Email()
    # if not emailchecker(email):
    #     return "Invalid email"
    # if len(data.password)<3:
    #     #Tell client that signup was not succesful due to weak password
    #     reply=signup("","","","","",0)
    #     msg=pickle.dumps(reply)
    #     conn.send(msg)
    #     return "Bad password"
    
    query = "INSERT INTO Users (Username, Password, Email, Name, Age, Gender, Status, City, Institute) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (data.username, data.password, data.email, data.name, data.age, data.gender, data.status, data.city, data.institute)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    mydb.commit()

    mycursor = mydb.cursor() 
    query = "CREATE TABLE "+ str(data.username)+" (Username varchar(20), FollowBack INT)"
    # val = tuple(data.username,)
    mycursor.execute(query)
    mydb.commit()
    
    #Tell client if signup was succesful
    reply=signup("","","","","","","","","","",1)
    msg=pickle.dumps(reply)
    conn.send(msg)
    return "Done"

def Login(conn, loginData):
    query = "SELECT * FROM Users where Username=" + "'" +str(loginData.username)+ "'" +" AND Password ="+ "'"+ str(loginData.password)+"'"
    # val = (loginData.username, loginData.password)
    print(query)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()

    if(len(result)==0):#not sure how to see if result is empty or not
        reply=login("","","",0)
    else:
        reply=login("","","",1)
    
    data=pickle.dumps(reply)
    conn.send(data)
    # server side
    return_arr = [loginData]
    if len(result)==0:
        return_arr.append(0)
    else:
        return_arr.append(1)
    return return_arr

def NewTweet(conn, addr,username, msg):
    #getting tweet ID
    query = "Select TweetID from Tweets"
    mycursor = mydb.cursor()
    mycursor.execute(query)
    arr = mycursor.fetchall()

    num = arr[-1][0]
    tweetid = int(num)+1
    tweet_id = str(tweetid)
    
    tag_arr = msg.hashtags
    while(len(tag_arr)<5):
        tag_arr.append("NULL")            
    query = "INSERT INTO Tweets (Username, TweetID, TweetMessage, Hashtag1, Hashtag2, Hashtag3, Hashtag4, Hashtag5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (username, tweet_id, msg.message, msg.hashtags[0], msg.hashtags[1], msg.hashtags[2], msg.hashtags[3], msg.hashtags[4])
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    mydb.commit()

    dic={}
    query = "SELECT * from Hashtags"
    mycursor = mydb.cursor()
    mycursor.execute(query)
    results = mycursor.fetchall()

    for j in results:
        dic[j[0]] = j[1]
    for tag in tag_arr:
        if (tag!="NULL"):
            if tag in dic:
                count = dic[tag] + 1
                query = "UPDATE Hashtags SET Count = %s where Tag=%s"
                mycursor = mydb.cursor()
                val = (str(count), str(tag))
                mycursor.execute(query, val)
                mydb.commit()
            else:
                count = 1
                query = "INSERT INTO Hashtags (Tag, Count) VALUES (%s, %s)"
                mycursor = mydb.cursor()
                val = (str(tag),str(count))
                mycursor.execute(query, val)
                mydb.commit()
                print("Tag added")
    #Tell the client that Tweet was succesful
    reply=newtweet("","","",1)
    data=pickle.dumps(reply)
    conn.send(data)
    print("Done tweet")
    
def DeleteFollower(conn, addr,username, data):
    follower=data.follower
    query="DELETE FROM "+str(username)+" WHERE Username ='" + str(data.follower) +"'"
    mycursor=mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    
    #Tell client that follower was succesfully deleted
    reply=deletefollower("","",1)
    data=pickle.dumps(reply)
    conn.send(data)
    print("Deleted follower")

def ShowAllFollowers(conn, username, data):
    query="SELECT Username FROM %s" #select all entries from Username column in the database of requesting user
    val=(username,)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    arr=mycursor.fetchall()
    results=showallfollowers("",arr)
    data=pickle.dumps(results)
    conn.send(data)
    print("Followers list sent")
    
def Refresh(conn, username, data):
    query="SELECT Username FROM %s"
    val=(username,)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    
    names=mycursor.fetchall()
    dic={}
    for name in names:
        dic[name]=1
        
    query="SELECT * FROM Tweets ORDER BY TweetID DESC" #sort by tweet id in descending order
    val=() #not sure about syntax
    mycursor=mydb.cursor()
    mycursor.execute(query,val) 
    results=mycursor.fetchall()
    
    ls=list()
    count=0
    for row in results:
        if(count==5):
            break
        if(dic[row[0]]==1):
            ls.append(row)
            count+=1   
    if count==0:
        reply=refresh("",ls,0)
    else:
        reply=refresh("",ls,5)
    data=pickle.dumps(reply)
    conn.send(data)
    

def SearchPerson(conn, addr, username, data):
    query="SELECT Username, Name, Age, Gender, Status, City, Institute FROM Users where Username = %s or Name = %s"
    val = (data.username, data.name)
    mycursor = mydb.cursor()
    mycursor.execute(query,val)
    results = mycursor.fetchall()
    if len(results)==0:
        message = searchperson("SearchPerson", "", "", "", "", "", "", "", 0)
    else:
        results = results[0]
        print(results)
        message = searchperson("SearchPerson", results[0], results[1], results[2], results[3], results[4], results[5], results[6], 1)
    data=pickle.dumps(message)
    conn.send(data)
    print("Data of the searched person sent")
    return message.flag

def Follow(conn, addr, username, data):
    available = SearchPerson(conn, addr, username, data)
    if (available==1):
        query = "INSERT INTO "+ str(username) + " (Username)" + " VALUES("+ "'"+str(data.username)+"'" ")"
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print("Following ", data.username)
    else:
        print("person not found")

def SearchByHashtag(conn,data):
    hashtag=data.hashtag
    query="SELECT * FROM Tweets where Hashtag1=%s or Hashtag2=%s or Hashtag3=%s or Hashtag4=%s or Hashtag5=%s"
    val=(hashtag,hashtag,hashtag,hashtag,hashtag)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    results=mycursor.fetchall() 

    #send data to client

    reply=searchbyhashtag("","",results)
    data=pickle.dumps(reply)
    conn.send(data)

def TrendingHashtags(conn, data):
    query = "SELECT Tag from Hashtags ORDER BY Count DESC"
    mycursor=mydb.cursor()
    mycursor.execute(query)
    results=mycursor.fetchall()
    arr = list() 
    print(results)
    counter = 0
    for j in results:
        if counter==5:
            break
        counter+=1
        arr.append(j[0])
    reply = trendinghashtags("", arr)
    data = pickle.dumps(reply)
    conn.send(data)
    print("trending hashtags sent")

conn, addr = server_socket.accept()

while True:
    # print(conn)
    # data = conn.recv(BUFFERSIZE)
    # received_msg = data.decode('ascii')
    # print("message received is ", received_msg)

    # response = "Welcome to the Mini Twitter"
    # data = response.encode('ascii')
    # conn.send(data)
    msg = conn.recv(BUFFERSIZE)
    while(len(msg)==0):
        msg=conn.recv(BUFFERSIZE)
    data=pickle.loads(msg)
    query = data.func

    if(query=="SignUp"):
        SignUp(conn,addr,data)
        # result = Login(conn)
        # continue
        # conn.close()
    else:
        flag = 0
        while(flag==0):
            if(query=="Login"):
                returnedArr = Login(conn, data)
                if (returnedArr[-1]==1):
                    flag=1
                    break
            else:
                print("please login first")
                msg = conn.recv(BUFFERSIZE)
                data=pickle.loads(msg)
                query = data.func
        username = returnedArr[0].username
        print(username)
        while True:
            msg = conn.recv(BUFFERSIZE)
            while len(msg)==0:
                msg = conn.recv(BUFFERSIZE)
            # print(msg)
            data=pickle.loads(msg)
            query = data.func
            if(query=="NewTweet"):
                NewTweet(conn,addr,username, data)
                # conn.close()
            elif(query == "DeleteFollower"):
                print("deleting follower")
                DeleteFollower(conn,addr,username,data)
            elif(query == "ShowAllFollowes"):
                ShowAllFollowers(conn, addr, username, data)
            elif(query == "Refresh"):
                Refresh(conn, addr, username, data)
            elif(query == "SearchPerson"):
                SearchPerson(conn, addr, username, data)
            elif(query =="Follow"):
                Follow(conn, addr, username, data)
            elif(query == "SearchByHashtag"):
                SearchByHashtag(conn,data)
            elif(query == "TrendingHashtags"):
                TrendingHashtags(conn, data)
            elif(query == "Logout"):
                # Logout(conn, addr, username, data)
                conn.send(bytes("bye"))
                conn.close()
                break
    # result = SignUp(conn, addr)
    # print(result)
    # NewTweet(conn, addr, "prasad")
    # conn.shutdown(socket.SHUT_RDWR)
    # conn.close()
server_socket.close()
