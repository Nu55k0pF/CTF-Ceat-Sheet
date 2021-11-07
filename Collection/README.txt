Task 2:

VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==

String is Base64 encoded

THM{ju57_d3c0d3_7h3_b453} 


Task 3:

Download findme.jpg

file does not yield anything

In the EXIF date we find the Flag

THM{3x1f_0r_3x17}


Task 4:

download file Extinction.jpg

exif tool does not return anything

file does not return anything

Hint: steghide -> which means the flag must be embeded in the image itself

I installed stegheide and used
steghide --extract -sf Extinction.jpg:

It going to be over soon. Sleep my child.

THM{500n3r_0r_l473r_17_15_0ur_7urn}


Task 5:

Flag is in white text directly next to the question, just mark it with the mouse

THM{wh173_fl46}


Task 6:

Download file QR.img

its a QR code Scanned with https://webqr.com/

It reads THM{qr_m4k3_l1f3_345y}


Task 7:

download file

file is not readable with nano, but cat reveals the flag but its not easy to copy

THM{345y_f1nd_345y_60}Hello there, wish you have a nice dayD


Task 8:

decode this string

3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L

cyberchef magic finds from base58 to base64 is the flag

THM{17_h45_l3553r_l3773r5}


Task 9:

seems like a ceaser cypher

https://www.dcode.fr/caesar-cipher decodes with +19

THM{hail_the_caesar}


Task 10:

no file no cypher

-> inspect element shows

THM{4lw4y5_ch3ck_7h3_c0m3mn7}


Task 11:

download spoil.png

strings reveals XML data but not the flag. Further reaserch needed here

hint: look at the file header

checking the file in a Metadata reader https://www.metadata2go.com/ the header contains:

23 33 44 5F 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 00 00
03 20 00 00 03 20 08 06 00 00 00 DB 70 06 68 00 00 00 
01 73 52 47 42 00 AE CE 1C E9 00 00 00 09 70 48 59 73 
00 00 0E C4 00 00 0E C4 01 95 2B 0E 1B 00 00 20 00 49 
44 41 54 78 9C EC DD 79 9C 9C 55 9D EF F1 CF 79 9E 5A 
BB 7A 5F 92 74 77 F6 40 48 02 09 20 11 50 C4 20 BB A2 
88 A8 80 5C 19 06 7C 5D 64 C0 79 E9 75 2E 03 CE 38 E3 
0E 8E

check that with cyber-chef:
nothing

after having another look the header states:


Mime Type
application/octet-stream
Category
application
Type
octet-stream

so this is an executable:

change with chmod +x

file still not executable
zsh: exec format error:

Couldn't figure it out.

Solution: make a hexdump of the file with xxd

xxd -p spoil.png > spoil_hex_data

and convert the hexdump with cyber-chef (which lets you render images form raw data input)

there is a magic number in the header that indicates what file this should be. This number is wrong! and needs to be replaced

for png it should be 89 50 4E 47

after editing the magic number cyberchef can display the real image
-> spoil_fixed.png


Task 12:

after looking around on twitter and facebook I found nothing. The hint points to reddit

browsing reddit did't yeald much, so I took a little hint from a write up. I googled:

tryhackme reddit "THM{"

and found a page https://www.reddit.com/r/tryhackme/comments/eizxaq/new_room_coming_soon/
under the image ther is a flag

THM{50c14l_4cc0un7_15_p4r7_0f_051n7} 

which turns out to be the right flag


Task 13:

Hint: binaryfuck
took another hint from a write up. Its written in the programing language brainfuck

Luckily there is an online brainfuck interpreter which when given the code


++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++++.
------------.+++++.>+++++++++++++++++++++++.<<++++++++++++++++++.
>>-------------------.---------.++++++++++++++.++++++++++++.<+++
+++++++++++++++.+++++++++.<+++.+.>----.>++++.

will return the flag

THM{0h_my_h34d}


Task 14:

we get two strings:

S1: 44585d6b2368737c65252166234f20626d
S2: 1010101010101010101010101010101010

the title suggests that we are to XOR both numbers and that will result in the flag. I suspect it is base64
but my first trys didn't yield anything.

But using the XOR and Magic recepie I found:

From_Hex('None')
XOR({'option':'Hex','string':'10'},'Standard',false)

THM{3xclu51v3_0r}


Task 15:

another fil hell.jpg
hint says "binwalk" which is a tool for searching a given binary image for embedded files. 
So I check binwalk -h

first run suggest ther is an archive embeded named hello_there

$binwalk -e hell.jpg 

gives _hell.jpg.extracted directory. It contains hello there.txt wich in turn contains the flag

THM{y0u_w4lk_m3_0u7}


Task 16:

Download the file

└─$ file dark.png           
dark.png: PNG image data, 968 x 300, 8-bit/color RGB, non-interlaced

I have the suspicion that there is some text hidden in the image but its very dark, so I installed gimp.

Shure enough, after adusting the brightess input and balance, the flag is revield in dark_edited.png

THM{7h3r3_15_h0p3_1n_7h3_d4rkn355}


Task 17:

download QRCTF.png
its a qr code

the QR code links to a soundcloud

Flag as heard is:
SOUNDINGQR



Task 18:

we need to find what was on 

https://www.embeddedhacker.com/

Targetted time: 2 January 2020

going to wayback machin and there is a snapshot of the page and date. A little scrowling and there is the flag

THM{ch3ck_th3_h4ckb4ck} 


Task 19

Hint find the Key of viginere cypher

MYKAHODTQ{RVG_YVGGK_FAL_WXF}

I read about the vigenere cypher and figured this could be a fun programing challange but would take me a while. so I found an online solver https://www.dcode.fr/vigenere-cipher

with the help of the known part in the beginning it was fast

TRYHACKME{YOU_FOUND_THE_KEY}


Task 20
Decode this:

581695969015253365094191591547859387620042736036246486373595515576333693

nothing on cyberchef

Hint mentions 
dec -> hex -> ascii

I googled how to convert dec to hex in the shell but this is not right. 



$printf '%x\n' 581695969015253365094191591547859387620042736036246486373595515576333693
50b9fe04c44ede92


https://www.rapidtables.com/ gives the right conversions 

581695969015253365094191591547859387620042736036246486373595515576333693  DEC
54484D7B31375F6A7535375F346E5F307264316E3472795F62343533357D  HEX
THM{17_ju57_4n_0rd1n4ry_b4535}  ASCII



Task 21

download the packet capture and open with wireshark

after following the TCP Stream for a while there is some unencryptet traffic with a URL

ocsp.digicert.com

upon going there you download a file
MTnsCiWB.ors

this file was a red herring. After fiddling around for a bit i decided to look for something else. After landing onthe last stream, there is some unecrypted traffic with a get request to get flag.txt in the response I found the flag

THM{d0_n07_574lk_m3}


