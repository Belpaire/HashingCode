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

def interest_tags(tags1,tags2):
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
    return min(tagsSame,tags1diff,tags2diff)



def makelist(data):
    picturelist=data
    max_score_this_iteration=0
    nextSlide=0
    f  = open("solution", "w")
    while len(picturelist)>1:
        for x in range(len(picturelist[1:])):
            calc_score=interest_tags(picturelist[0].tags,picturelist[1:][x].tags)
            if max_score_this_iteration< calc_score:
                    max_score_this_iteration =calc_score
                    print (max_score_this_iteration)
                    nextSlide=x

        f.write(str(picturelist[0].id))
        del picturelist[0]
        picturelist[0]=picturelist[nextSlide]
        max_score_this_iteration=0

def main():
   data = parse('./input/b_lovely_landscapes.txt')
   makelist(data)

if __name__ == '__main__':
    main()
