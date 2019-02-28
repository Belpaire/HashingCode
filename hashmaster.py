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
			pics.append(Picture(str(cnt), data[0] == "H", int(data[1]), data[2:]))
			line = fp.readline()
			cnt += 1
		fp.close()
	return pics

def eval_tags(pic1, pic2):
	assert pic1.ishorizontal and pic2.ishorizontal

	tags1 = pic1.tags
	tags2 = pic2.tags

	tagsSame=0
	tags1diff=0
	tags2copy=tags2[:]
	for i in tags1:
		if i in tags2:
			tagsSame+=1
			tags2copy.remove(i)
		else:
			tags1diff+=1
	tags2diff=len(tags2copy)
	return min([tagsSame,tags1diff,tags2diff])
		
def output(slideshow):
	print(slideshow)

def main():
	data = parse('./input/a_example.txt')
	print(data[1])
	print(data[2])
	print(data[1].merge(data[2]))
	print(data[0])
	print(eval_tags(data[0], data[1].merge(data[2])))

if __name__ == '__main__':
    main()
