from sys import argv

state = -1
text_lines = []
with open(argv[1],"r") as f:
	for line in f.readlines():
		if (line=="\n"):
			state = -1
			continue
		elif state==1:
			text_lines.append(line.strip())
		else:
			state += 1


with open("converted_" + argv[1], 'w') as f:
	f.write(" ".join(text_lines))