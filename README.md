# Population-Monitor
Created on Raspbian Buster with desktop 2019-09-26 v4.19. 
Tested with Azure DB. 
Only Tested running script with **sudo**. 
Main.py is the most updated file

**About**

This script will scan the Local Network using nmap and output the results to a file in XML format. The information gathered will consist of the IP addresses, Mac addresses and Vendor name. The data will then be parsed and send to specified azuzre database. This information is readily available to anyone on the LAN and hold no risk to the users information or privacy. 

**Requirements**
1. nmap
2. pymssql
3. Azure DB

**Installing nmap**
```
apt-get install nmap
```

**Installing pymssql with prerequisites**
```
sudo pip install cython
sudo pip install --upgrade cython
sudo apt-get install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc
sudo apt-get install python-pymssql
```
Created myalias in freetds.conf file http://www.pymssql.org/en/stable/azure.html
"freetds.conf" at the path /etc/freetds/.
```
[myalias]
host = yourServer.database.windows.net
port = 1433
tds version = 7.3
```

Use this in vim when trying to save the code since its a readonly file
```
:w !sudo tee % >/dev/null
```

**Database Design**
```SQL
CREATE TABLE tbl_nmapDATA(
DeviceID int not null identity(1,1),
IPAddress VARCHAR(15) not null,
Vendor VARCHAR(17) not null,
MACAddress VARCHAR(17) not null,
DateLogged Date NOT NULL default GETDATE(),
CONSTRAINT nmapDATA_PK PRIMARY KEY(DeviceID)
);
 
INSERT INTO [dbo].[tbl_nmapDATA] (IPAddress, Vendor, MACAddress)
VALUES (p.listofIP[i], p.listofVendor[i], p.listofMAC[i]);
 
CREATE TABLE tbl_nmapDATA(
DeviceID int not null identity(1,1),
IPAddress VARCHAR(15) not null,
Vendor VARCHAR(17) not null,
MACAddress VARCHAR(17) not null,
DateLogged Datetime NOT NULL default GETDATE(),
CONSTRAINT nmapDATA_PK PRIMARY KEY(DeviceID)
);

```

