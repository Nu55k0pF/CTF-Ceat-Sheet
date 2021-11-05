#### Mr_Robot ###

### Recon

# HOST IP:

192.168.178.34 

# Nmap Scan

80/tcp  open  http     Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
443/tcp open  ssl/http Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03

# Nikto
wordpress
/wp-login
/wb-admin

# Dirbuster

# wpscan

/robots.txt <- Hint for Flag
	found in robots.txt
	http://192.168.178.34/fsocity.dic <- lools like a wordlist maybe Passwords?

second Scan with fsocity.dic

trying to find accounts for admin login @
http://192.168.178.34/wp-login.php


### Gaining Accses
!! Wordpress reactes differently if a wrong user is input then a real user
-> build a python script to exploit that
-> script found Elliot is a valid user
-> try to find Elliots password  

# Hydra
use Username Elliot with fsocity.dic as Password list

hydra -l Elliot -P fsocity.dic 192.168.178.3 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:login_error"

-> this did not get anything usefule and a lot of errors, there is probably something wrong with the post request, further study needed
-> Did some research on HTTP Post and got it working

# Paralel second wpscan

wpscan --url http://192.168.178.34 -U 'Elliot' -P ./fsocity.dic -o ./wps/password.log 

form password.log
[!] Valid Combinations Found:
 | Username: Elliot, Password: ER28-0652


Note that the proces was aborted at the end. Also shlould have used verbouse option to have an idea of what wpscan is doing atm

# Inspecting Wordpress Admin

unpached version of Wordpress searching for wordpress exploit with google and metasploit to gain acces to host

After a view failed attempts using Metasploit module /uploade revers shell for wp I found

http://pentestmonkey.net/tools/php-reverse-shell/php-reverse-shell-1.0.tar.gz
to get a revers shell 

-> have to learn more php first

found git repo to generate malicious plugin 
https://github.com/JavaRockstar/malicious-wordpress-plugin/blob/master/ 

see also https://docs.j7k6.org/wordpress-malicious-plugin-reverse-shell-metasploit/

generated the plugin, and activated it. no connection, need to find out why not
After some more research i'm guessing the problem here is that the attacker machine is in another subnet then the
victim. 

swiched kali box to proper subnet but still no succes, trying with another script

https://github.com/wetw0rk/malicious-wordpress-plugin

-> this script worked and i got a meterpreter session. Not shure if the subnet swich was neccesary. 
-> will test this later. 

### Escalating

Searching around the machine i found /home/robot/ wich contains two files. one of which is key 2. 
However the Key can not be opend or downloaded. But there is a file called Password
-> Try to crack password file

password seems to be Hashed with MD5
trying out john the ripper, using fsociy.dic did not result in a cracked hash, trying with default wordlist

-> While John is rung i check if the hash is in a MD5 rainbow Table and it is

abcdefghijklmnopqrstuvwxyz

I can start a shell with meterpreter but after some research I found out that I dont get a pty because I came in via PHP.

-> found a lot of usefull info on how to get a better shell here 
https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/

-> with a proper shell I can su into robot with his pw and read the flag

Now its time to do some research on priv escalation from user to root

Linux linux 3.13.0-55-generic #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

-----
with the stabilized shell or meterpreter try to upload linpeas, further research for "stabilizing shells" mabey make or download a scrit

I did some more reseach and instead I did more enumeration first

-> checked processes runing as root
 
-> checked programs that are executable

find / -perm -u=s -type f 2>/dev/null  

-> found nmap can run as root

nmpat --interactive 
!sh
-> root

found last flag in /root


### Findings
#Creds Elliot
Usr:Passwd
Elliot:ER28-0652
Name: Elliot Alderson	
elliot@mrrobot.com

#Creds robot
Usr:Passwd
robot:abcdefghijklmnopqrstuvwxyz

#Flags
Key 1= 073403c8a58a1f80d943455fb30724b9
Key 2= 822c73956184f694993bede3eb39f959
Key 3= 04787ddef27c3dee1ee161b21670b4e4

