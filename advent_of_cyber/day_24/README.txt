### Day 24 ###

# Read instructions #

Recaping all the lessons from the past 23 challanges

# Client side filter #

setting up burp suit

# nmap # 

See nmap Scan

found hidden page under port 65000

-> dirbusting that page
	-> found uploads.php
-> paralel nikto

# What is the name of the hidden directory where file uploads are saved?

Dirbuster also found the upload location at /grid/



# Bypass the filters. Upload and execute a reverse shell

-> like described in the intro I need to drop the clientside filter with burbsuit and upload a suitible php 
   reverse shell

-> droped the filter with burpsuit
-> also hat to trick the site with .jpg.php

-> forgot to edit the reverse shell first :(
-> startet NC reverse listener and uploaded php script again

-> got response back! (closing burpsuit)

# What is the value of the web.txt flag?

stabilizing shell with python

-> hint its in var/www (should remember that!-> webserver content normaly goes here)

THM{ENTER_THE_GRID}

# Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password

-> found username:password of SQL DB in /var/www/TheGrid/includes/dbauth.php
        $dbuser = "tron";
        $dbpass = "IFightForTheUsers" 

# connect to sql db and find encrypted Password

mysql -utron -pIFightForTheUsers

-> learn better SQL!!!!

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| tron               |
+--------------------+

..

mysql> SELECT * FROM users;
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | flynn    | edc621628f6d19a13a00fd683f5e3ff7 |
+----+----------+----------------------------------+

got the Password, but its encrypted

-> used john the ripper to crack the above password

@computer@ 

# What is the value of the user.txt flag?

in ~/user.txt

THM{IDENTITY_DISC_RECOGNISED}

# Escalate

User is part of lxd group (Container)
-> researched priv esc lxd and found https://www.hackingarticles.in/lxd-privilege-escalation/

followed the instructions there and build the alpine image

-> create an container and mount the root directory inside the container
-> in the container we are root and can view the contets of the mounted file system from the host
-> root/root.txt

THM{FLYNN_LIVES}

