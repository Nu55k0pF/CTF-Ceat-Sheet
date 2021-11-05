#### Basic Pen Testing (Vuln Hub) ####

## Recon ##

# nmap #

Nmap scan report for 192.168.25.131
Host is up (0.00021s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     ProFTPD 1.3.3c
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d6:01:90:39:2d:8f:46:fb:03:86:73:b3:3c:54:7e:54 (RSA)
|   256 f1:f3:c0:dd:ba:a4:85:f7:13:9a:da:3a:bb:4d:93:04 (ECDSA)
|_  256 12:e2:98:d2:a3:e7:36:4f:be:6b:ce:36:6b:7e:0d:9e (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel


-> checking out webpage
found default web page, try nikto and gobuster

# Nikto #

Uncommon header 'link' found, with contents: <http://vtcsec/secret/index.php/wp-json/>; rel="https://api.w.org/"
Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). 
Apache 2.2.34 is the EOL for the 2.x branch.
/secret/

	-> leads to http://192.168.25.131/secret/#content
	page is realy slow the Browser Debuger tells me that it cannot resolve 

# Dirbuster #

Is runing in the Backg

# (1) Looking around the Page  #

http://vtcsec/secret/wp-content/themes/...

This leads me to belive, that I cant load the files because of DNS resolution. Doing research on that.

-> after some research I was relativly shure that it is indeed a DNS problem. I edited /etc/hosts and added

---
192.168.25.131	vtcsec
---

The Page now loades correctly, like suspected from nikto and dirbuster it is a Wordpress installation.
From Dirbuster I know there is a /secrets/wp-login and /secrets/wp-admin

The default admin account seems to be admin (wp response indicates if a username is correct or not)

Befor trieng to brute force the password I want to look around a bit more

-> trying stupid passwords rusulted in finding the password is also admin

Wordpress Version is Version 4.9

Looking for possible explploits with searchsploit

-> found a suitible exploit in metasploit, after setting all parameters and changing the LHOST form 127.... to public ip adress
-> I got a meterpreter session as www-data

# Enumeration #

Computer    : vtcsec
OS          : Linux vtcsec 4.10.0-28-generic #32~16.04.2-Ubuntu SMP Thu Jul 20 10:19:48 UTC 2017 x86_64


1. Stabilizing shell

2. looking for processes running as root

3. Found the "backdoored"-proftp installation in marlinspikes user folder (have to check that out later)

4. After a lot of looking around, a lot of fiddling and trying I found lots of stuf but could not make much use
of anything (need to learn way more about linux) so I decided to upload unix-privesc-check. Maybe that would
make it a bit easyer

-> privesc findings in report.txt

WARNING: /etc/passwd is a critical config file. World write is set for /etc/passwd

-> this is basicly the same my manual enumeration yealded. Have to do more reaserch into the topic

	* this link helped me understand what and how to do it 
	* https://security.stackexchange.com/questions/151700/privilege-escalation-using-passwd-file

-> created a password hash (aded instead of x)  and added root2 with uid 0 in passwd file (username must be used as salt)
perl -le 'print crypt("root", "root")'
roK20XGbWEsSM
-> droped into a shell, stabilized to a terminal with python -c 'import pty; pty.spawn("/bin/bash")'
su root2 worked!

-> victory!

time to explore another path.


# FTP #

From the nmap scan the FTP version is known. apperently the ProFTPD Version 1.3.3c has a remote root acces backdoor
installed

Apperently you just have to netcat to the server on the FTP port and you are root

After stabilizing the shell -> win

## Attack Vectors ##

1. Wordpress -> Wind
3. FTP

#### Findings ####

IP = 192.168.25.131

Wordpress Version 4.9

# Creds #

-- wp-admin --
admin:admin

-- local user --
marlinspike

-- new root user --
root2:root
