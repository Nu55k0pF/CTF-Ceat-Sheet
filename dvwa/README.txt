#### DVWA ####
### 10.12.2020 ###

## 1. Recon ##
# Nmap Scan #

found:
ssh
http
mysql

-> checking out webpage while nikto and gobuster are runing

# Nikto #

Intresting findings:
- Server may leak inodes via ETags, header found with file /robots.txt
- OpenSSL/0.9.8l appears to be outdated (current is at least 1.1.1)
- PHP/5.3.1 appears to be outdated
- /config/: Configuration information may be available remotely.
- /login.php: Admin login page/section found.
	- 
- /phpmyadmin/: phpMyAdmin directory found:
	- does not require login!!!
	- Your configuration file contains settings (root with no password) that correspond to the default MySQL privileged account. Your MySQL server is running with this default, is open to intrusion, and you really should fix this security hole by setting a password for user '.root'.
	- found user data in dvwa db and downloaded users.cvs (all users and password hashes)

# John # 

Trying to get the passwords from users.cvs
convert .CSV to something usable

-> made a littel python script to convert the file (just for practicing python)
after a littel bit of fidling john decrypted the md5 encrypted passwords

#### Gaining access ####

With the craced passwords I want to try to ssh into the machine
Sadly that did not work got "Connection reset by 192.168.178.43 port 22"

Instead the passwords worked for the weblogin on 192.168.178.43/index.php


#### Findings ####
Target IP:
export IP=192.168.178.43

http://192.168.178.43/phpmyadmin/

users.cvs

password         (admin)
abc123           (gordonb)
letmein          (pablo)
charley          (1337)


MySQl:
root: #nopassword#
