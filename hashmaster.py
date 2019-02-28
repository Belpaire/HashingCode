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
	#print(tagsSame,tags1diff,tags2diff)
	return min(tagsSame,tags1diff,tags2diff)

def get_next_greedy(prev, hor, ver, seed):
	intout = 30

	best_hor_int = -1	# score
	best_hor_nb = -1	# idx in list
	best_hor = None		# slide
	for i in range(0, min(intout, len(hor))):
		sid = randint(0, len(hor)-1)
		#while sid < 0:
		#	(sidt, seed) = lfsr(seed) # change with pseudorandom int
		#	# print(sidt)
		#	if sidt < len(hor):
		#		sid = sidt

		shor = hor[sid]
		et = eval_tags(prev, shor)
		# print(et)
		if et > best_hor_int:
			best_hor_int = et
			best_hor_nb = sid
			best_hor = shor
	
	best_ver_int = -1
	best_ver_nb = (-1 -1)
	best_ver = None
	for i in range(0, min(intout, (len(ver))*(len(ver)))):
		if len(ver) < 2:
			break

		sid = -1
		while sid < 0:
			sidt = randint(0, (len(ver))*(len(ver)))
			# (sidt, seed) = lfsr(seed) # change with pseudorandom int
			(x, y) = inv_cantor(sidt)
			if not(x == y or x >= len(ver) or y >= len(ver)):
				sid = sidt
		
		if sid < 1:
			break

		sverp = ver[x].merge(ver[y])
		et = eval_tags(prev, sverp)
		if et > best_ver_int:
			best_ver_int = et
			best_ver_nb = (x, y)
			best_ver = sverp
	
	return (best_hor, [best_hor_nb], best_hor_int, seed) if best_hor_int >= best_ver_int else (best_ver, best_ver_nb, best_ver_int, seed)
		

def output(slideshow):
	print(slideshow)

def main():
	fname = "e_shiny_selfies"
	data = parse('./input/%s.txt' % fname)
	hor = [x for x in data if x.ishorizontal]
	ver = [x for x in data if not x.ishorizontal]
	oname = './output/%s_sol.txt' % (fname)
	
	# ss = []
	previd = randint(0, len(hor)-1)
	prev = hor[previd]
	del hor[previd]
	# ss.append(previd)
	
	
	seed = [0]*17
	score = 0
	cnt = 0
	print("%i: %i -- %s" % (0, score, prev.tags))

	
	f = open(oname,"w")
	f.write("%s\n" % -1)
	f.close()	

	while True:
		(slide, ids, sc, seed) = get_next_greedy(prev, hor, ver, seed)
		next = slide
		if next is None:
			break

		# print(prev)
		# print(next)
		# print(sc)
		
		score = score + sc
		if len(ids) == 1:
			del hor[ids[0]]
			# ss.append(ids[0])	
		else:
			print("%s %i" % (ids, len(ver)))
			del ver[ids[0]]

			if ids[1] > ids[0]:
				del ver[ids[1]-1]
			else:
				del ver[ids[1]]
			# ss.append(ids)
		f = open(oname,"a")
		f.write("%s\n" % slide.id)
		f.close()
		
		cnt += 1
		if cnt > len(data)+1:
			break

		print("%i: %i -- %s" % (cnt, score, next))
		prev = next
		
	# print(ss)
	print(score)

if __name__ == '__main__':
    main()
