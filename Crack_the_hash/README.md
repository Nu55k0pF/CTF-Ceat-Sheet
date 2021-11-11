# Crack the Hash

## 1

### 1

48bb6e862e54f2a795ffc4e541caed4d

used hascat

MD5

easy

### 2

CBFDAC6008F9CAB4083784CBD1874F76618D2A97

sha1

password123

found https://hashcat.net/wiki/doku.php?id=example_hashes

### 3

1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

sha2

C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

letmein

### 4

figured out it was bcrypt but I couldn't get hashcat to run on it
so I installed john the ripper

from the hints it says to filter for 4 character words, so i googled how to accomplish that with john

made a copy of rockyou with

	grep -o -w '\w\{1,4\}'

where \w\ is shorthand for regex [a-zA-Z0-9] then I ran

	john --format=bcrypt --wordlist=./rockyou.short ./hash1_4
	john --show hash1_4 
	?:bleh


### 5

279412f945939ba78ce0758d3fd83daa

Hint: MD4

	hashcat -m 900 --force 279412f945939ba78ce0758d3fd83daa
	
Did not find anything in rockyou

trying with John

	echo '279412f945939ba78ce0758d3fd83daa' > hash1_5.MD4
	john hash1_5.MD4

I need to Intall better drivers for my MacBook so hashcat stops complaining and i get better speed

Maybe I'm not smart enough why its not found in the rockyou.txt but now
I let hashcat run a brute force attack. This will take some time though

Since this took so long, and I'm shure this will decrypt eventualy, I dont want to fry me Laptop.
So I read up on a walkthrough how others have solfed this. This lead me to an online Hash identifier -> Very usefull, need to add to my recources

https://hashes.com/en/decrypt/hash

Then googling for an MD4 cracker

https://md5decrypt.net/

provided the correct answer 

Eternity22

## Level 2

For level 2 the challange says that all answers are in the rockyou list!

Now that it gets a little more serious, I'll up my game a bit two

-> make hashfiles for each challange
-> Since everything is in the rockyou.txt I don't think I'll need to optimize hardware utilisation yet
-> tring to only use hashcat from here to learn the tool better.

### 1

hash2_1

Checking hash in online tool
-> sha256

	hashcat -m 1400 --force hash2_1 ~/ctf/opt/wordlists/KaliLists/rockyou.txt -o answer2_1
	cat answer2_1
	paule

### 2

hash2_2

Checking hash in online toll
Possible algorithms: NTLM

referencing hashcat wiki https://hashcat.net/wiki/doku.php?id=example_hashes
-> NTLM = -m 1000

	hashcat -m 1000 --force hash2_2 ~/ctf/opt/wordlists/KaliLists/	rockyou.txt -o answer2_2
	cat answer2_2
	n63umy8lkf4i

### 3

hash2_3

Checking hash in online toll
Possible algorithms: Possible algorithms: sha512crypt $6$, SHA512 (Unix)

referencing hashcat wiki
-> SHA512 (Unix) = -m 1800

runing the usual comands from above gives an error

	$ hashcat -m 1800 --force hash2_3 ~/ctf/opt/wordlists/KaliLists/rockyou.txt -o answer2_3
	hashcat (v4.0.1) starting...

	OpenCL Platform #1: The pocl project
	====================================
	* Device #1: pthread-Intel(R) Core(TM) i7-2720QM CPU @ 2.20GHz, 1024/2892 MB allocatable, 8MCU

	Hashfile 'hash2_3' on line 1 (WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.): Signature unmatched
	Parsing Hashes: 0/1 (0.00%)...No hashes loaded.

So I'm checking how the hashfile needs to be formated
-> after checking the file again, i did not copy the hash correcktly :/
now it works

	$ hashcat -m 1800 --force hash2_3 ~/ctf/opt/wordlists/KaliLists/rockyou.txt -o answer2_3








