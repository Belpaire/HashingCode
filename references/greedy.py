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


#picturelist.sort(key=nbtags)
#for i in range(len(picturelist)):
 #   for x in range(len(picturelist[i:])):
  #      max(min())

print(interest_tags(["zee","cat"],["cat","hond"]))