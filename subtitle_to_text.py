from sys import argv


for file in argv[1:]:
	state = -1
	text_lines = []
	fname = file.split('.srt')[0]
	with open(file,"r") as f:
		k = 0
		for line in f.readlines():
			k+=1
			if (line=="\n"):
				state = -1
				continue
			elif state==1:
				text_lines.append(line.strip())
			else:
				state += 1
			if k%14==0:
				text_lines.append("\n\n")


	with open(fname+'.txt', 'w') as f:
		f.write(" ".join(text_lines))
