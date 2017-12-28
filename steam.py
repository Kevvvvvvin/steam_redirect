#!usr/bin/env python

import os,sys,stat
import re
import urllib
import socket
import dns.resolver

with open('C:\Windows\System32\drivers\etc\hosts','r+') as f:
    print("hosts open!")
    lines=f.readlines()
    flag=0
    for line in lines:
        if(line=="127.0.0.1 steamcommunity.com\n"):
            flag=1
            break
    if(flag==0):
        f.write("\n127.0.0.1 steamcommunity.com\n")
        f.flush()
        print("hosts set ready!")
    else:print("existed!")

addr1 = socket.gethostbyname('steamcommunity.com')
print(addr1)

my_resolver=dns.resolver
my_resolver.nameservers=['208.67.222.222:5353']
ans = my_resolver.query('steamcommunity.com', 'A')
for i in ans.response.answer:
    for j in i.items:
        print(j.address)

def redirect():
    host = '127.0.0.1'#Local Server IP
    host2 = '127.0.0.1'#Real Server IP
    port = 80 #Local Server Port
    port2 = 443 #Real Server Port
    #def ProcData(data):
    #return data
    #add more code....
    print("Map Server start from " + host + ":" + str(port) +" to " + host2 + ":" + str(port2) +"\r\n")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',port))
    print("127.0.0.1 Server start at "+ str(port) +"\r\n")
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    client.connect((host2,port2))
    print(host +" Client connect to " + host2 + ":"+str(port2)+"\n")
    server.listen(5)
    ss, addr = server.accept()
    print('got connected from',addr)
    while 1:
        msg = ss.recv(20480)
        print ("Get:"+repr(msg)+"\r\n")
        client.send(msg)
        #print "Client send data %s to "%repr(msg)
        buf=client.recv(20480)
        #print "Client recv data %s from "%repr(buf)
        ss.send(buf)
        print( "Send:"+repr(buf)+"\r\n")