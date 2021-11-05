#### basic_2 ####

IP = 192.168.25.130

# nmap #

ftp ProFTPD 1.3.2c
open ssh OpenSSH 5.3p1 Debian 3ubuntu4 (Ubuntu Linux; protocol 2.0)
http Apache httpd 2.2.14
https?

# web interface #

after a little bit of looking around i tried some standard passwords for admin

since I already did a DVWA i will first look into the FTP side first

# ftp #

seems to be vulnarable. See

searchsploit:

ProFTPd 1.3.2 rc3 < 1.3.3b (FreeBSD) - Telnet IAC Buffer Overflow (Metasploit)   | linux/remote/16878.rb
ProFTPd 1.3.2 rc3 < 1.3.3b (Linux) - Telnet IAC Buffer Overflow (Metasploit)     | linux/remote/16851.rb

# Metasploit #

tried first exploit. But had no anonymouse user



### findings ###
http://192.168.25.130/index.php

admin:password
