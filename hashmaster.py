from picture import Picture

def parse(filename):
	pics = []
	with open(filename) as fp:  
		lines = int(fp.readline())
		line = fp.readline()
		cnt = 0
		while line:
			line = line[0:-1]
			data = line.split(' ')
			pics.append(Picture(cnt, data[0] == "H", int(data[1]), data[2:]))
			line = fp.readline()
			cnt += 1
		fp.close()
	return pics
		
def output(slideshow):
	print(slideshow)

def main():
	data = parse('./input/a_example.txt')    

if __name__ == '__main__':
    main()
