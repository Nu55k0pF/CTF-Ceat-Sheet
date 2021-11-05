import csv

# file to convert
i = './users4john.csv'

# file to convert to
o = './users4john_converted.csv'



with open(i, 'r') as fi, open(o, 'w+') as fo :
	l = ''
	read_data = csv.reader(fi, delimiter=";")
	for row in read_data:
		fo.write(':'.join(row) + '\n')




