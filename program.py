scores = {
	'a':1,
	'b':2,
	'c':3,
	'd':4,
	'e':5,
	'f':6,
	'g':7,
	'h':8,
	'i':9,
	'j':10,
	'k':11,
	'l':12,
	'm':13,
	'n':14,
	'o':15,
	'p':16,
	'q':17,
	'r':18,
	's':19,
	't':20,
	'u':21,
	'v':22,
	'w':23,
	'x':24,
	'y':25,
	'z':26,
	'"':0,
	

}

with open('names.txt','r') as f:
	names = f.read()
	names = names.split(',')
	names.sort()
	total = 0
	i = 0
	while i < len(names):
		name_total = 0
		current_name = names[i].lower()
		for char in current_name:
			name_total += scores[char]
		total += (name_total *(i+1))
		i += 1

print total



