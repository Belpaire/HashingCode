from picture import Picture
import random
import threading
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

def convertTagsToSparseMatrix(list_pictures):
    dictionarytags=dict()
    for pic in list_pictures:
        for  tag in pic.tags:
            if tag not in dictionarytags.keys():
                dictionarytags[tag]=[pic.id]
            else:
                dictionarytags[tag].append(pic.id)
    dictionaryidtotag=dict()
    for pic in list_pictures:
        dictionaryidtotag[pic.id]=pic.tags
    return dictionaryidtotag,dictionarytags


class myThread (threading.Thread):
   def __init__(self,  data,int):
      threading.Thread.__init__(self)
      self.data = data
      self.nb=int
   def run(self):
      print ("Starting " + str(self.nb))
      makelist(self.data,self.nb)



def makelist(data,nb):
    picturelist= sorted(data, key= lambda x: x.nbtags)
    max_score_this_iteration=0
    nextSlide=0
    f  = open("output/solutionb"+str(nb)+".txt", "w")
    score_found=False
    try :
        while len(picturelist)>3:
            for x in range(len(picturelist[1:])):
                calc_score=interest_tags(picturelist[0].tags,picturelist[1:][x].tags)
                if max_score_this_iteration< calc_score:
                        score_found=True
                        max_score_this_iteration =calc_score
                        nextSlide=x

            f.write(str(picturelist[0].id)+"\n")
            del picturelist[0]
            if(not score_found):
                nextSlide=len(picturelist)-2
            picturelist[0],picturelist[nextSlide]=picturelist[nextSlide],picturelist[0]
            max_score_this_iteration=0
            score_found=False
        f.write(str(picturelist[0].id)+"\n")
        f.close()
    except:
        print (nextSlide,len(picturelist))
        f.close()
def write_to_file(data):
    dict_id_to_tag,dict_tag_to_id=convertTagsToSparseMatrix(data)
    max_score_this_iteration=0
    currSlide=0
    nextSlide=1
    f  = open("output/solutionb.txt", "w")
    score_found=False
    try :
        while len(dict_id_to_tag)>1:
            tags_to_match=dict_id_to_tag[currSlide]
            for tag in tags_to_match:
                for id in dict_tag_to_id[tag]:
                    if id in dict_id_to_tag.keys():
                        curr_calc=interest_tags(dict_id_to_tag[currSlide],dict_id_to_tag[id])
                        if max_score_this_iteration< curr_calc:
                            max_score_this_iteration=curr_calc
                            nextSlide=id
            if max_score_this_iteration==0:
                nextSlide= random.choice(list(dict_id_to_tag.keys()))
                while nextSlide == currSlide:
                    nextSlide= random.choice(list(dict_id_to_tag.keys()))

            f.write(str(currSlide)+"\n")
            dict_id_to_tag.pop(currSlide)
            currSlide=nextSlide
            max_score_this_iteration=0

        f.write(str(nextSlide)+"\n")
        f.close()
    except:
        print ("error")
        f.close()

def main():
    data = parse('./input/b_lovely_landscapes.txt')
    write_to_file(data)

if __name__ == '__main__':
    main()

