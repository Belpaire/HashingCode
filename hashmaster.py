from picture import Picture
from random import randint
from cantor import *

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

def get_next_greedy(prev, hor, ver):
	best_hor_int = -1
	best_hor_nb = -1
	best_hor = None
	for i in range(0, min(100, len(hor))):
		sid = i # change with pseudorandom int
		shor = hor[i]
		et = eval_tags(prev, shor)
		# print(et)
		if et > best_hor_int:
			best_hor_int = et
			best_hor_nb = sid
			best_hor = shor
	
	best_ver_int = -1
	best_ver_nb = (-1 -1)
	best_ver = None
	for i in range(0, min(100, (len(ver))*(len(ver)))):
		sid = i
		(x, y) = inv_cantor(sid)
		if x == y or x >= len(ver) or y >= len(ver):
			continue
		sverp = ver[x].merge(ver[y])
		et = eval_tags(prev, sverp)
		if et > best_ver_int:
			best_ver_int = et
			best_ver_nb = (x, y)
			best_ver = sverp
	
	return (best_hor, [best_hor_nb], best_hor_int) if best_hor_int >= best_ver_int else (best_ver, best_ver_nb, best_ver_int)
		

def output(slideshow):
	print(slideshow)

def main():
	fname = "c_memorable_moments"
	hor = parse('./stef/%s_h.txt' % (fname))
	ver = parse('./stef/%s_v.txt' % (fname))
	oname = './output/%s_sol.txt' % (fname)
	
	ss = []
	previd = randint(0, len(hor)-1)
	prev = hor[previd]
	del hor[previd]
	ss.append(previd)
	
	f = open(oname,"w")

	score = 0
	cnt = 0
	print("%i: %i -- %s" % (0, score, prev.tags))
	while True:
		(slide, ids, sc) = get_next_greedy(prev, hor, ver)
		next = slide
		if next is None:
			break
		
		score = score + sc
		if len(ids) == 1:
			del hor[ids[0]]
			ss.append(ids[0])	
			f.write("%s\n" % slide.id)
		else:
			del ver[ids[0]]
			del ver[ids[1]]
			ss.append(ids)
			f.write("%s\n" % slide.id)
		
		cnt += 1
		if cnt > 100:
			break

		print("%i: %i" % (cnt, score))
		prev = next
		
	f.close()
	# print(ss)
	print(score)

if __name__ == '__main__':
    main()
