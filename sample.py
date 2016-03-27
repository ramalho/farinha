import itertools

def sample(filename):
	lines = open(filename, encoding='ASCII').readlines()[7:]
	print(len(lines))
	with open('SoFarinha30Kp.txt', 'wt', encoding='ASCII') as output:
		for line in itertools.islice(lines, None, None, 100):
			output.write(line)


if __name__=='__main__':
	source = '../SoFarinha.ply'
	sample(source)