import picture

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
    print(tagsSame,tags1diff,tags2diff)
    return min(tagsSame,tags1diff,tags2diff)

picturelist=
picturelist.sort(key=nbtags)
max_score_this_iteration=0
indexes_chose=[0,0]
f  = open("solution", "w")
while len(picturelist)>0:
    for i in range(len(picturelist)):
        for x in range(len(picturelist[i:])):
            calc_score=interest_tags(picturelist[i],picturelist[i:][x])
            if max_score_this_iteration< calc_score:
                max_score_this_iteration =calc_score
                indexes_chose[0]=i
                indexes_chose[1]=x
    index1=indexes_chose[0].id
    index2=indexes_chose[1].id
    picturelist.remove(indexes_chose[0])
    picturelist.remove(indexes_chose[1])
    f.write(index1)
    f.write(index2)





