#!/usr/bin/python3
import pymssql
from Parse import *

def SendToServer():
    # Parses the file that nmap produces which is called nmapScan.xml
    filename = 'nmapScan.xml'
    p = Parse()
    p.ParseXML(filename)

    # Azure Log-in information
    server = "yourServer.database.windows.net"
    print(server)
    user = "yourUsername@yourServer"
    print(user)
    password = "yourPassword"
    print(password)

    # uses credentials to connect to specifed server in myalias (See README.md)
    # with the database name NmapData
    conn = pymssql.connect("myalias", user, password, "yourDatabase")
    cursor = conn.cursor()

    # you must call commit() to persist your data if you don't set autocommit to True
    conn.commit()

    # p.hostUP represents how many devices are on the network. 
    # This loop will run once for each host on the network then insert
    # that devices data into the database
    for i in range(int(p.hostsUP)):
        # SQL codes used to insert the data
        query = (
            'INSERT INTO [dbo].[tbl_nmapDATA] (IPAddress, Vendor, MACAddress) VALUES (' + '' + p.listofIP[i] + '' + ');')
        # Executes the SQL code
        cursor.execute(query)
        # Returns the next row of data or None if there are no more rows.
        row = cursor.fetchone()

    while row:
        print(row)
        row = cursor.fetchone()
    # close connection
    conn.close()