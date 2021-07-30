
f = open("data.txt", "r")
data = f.readlines()
count = []
for line in data:
    if '1' not in line:                        #skippina jei jokia nedege
    	continue
    line = line.replace(',', "")               #ismetam comma
    count.append(line.index('1'))              # gaunam vienetuko pozicija a.k.a kokia sviesa dbr 
for i in range(len(count)-1):
	move = count[i]-count[i+1]
	if abs(move) in range(0,2):
		continue
	if count[i]==1 and count[i+1]:             #zalia rodykle
		continue
	print("NOT WORKING, ERROR IN POSITION" + i)
	break
print("All good")


