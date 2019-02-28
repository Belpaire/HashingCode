import random

file_name = "input/b_lovely_landscapes.txt"

#file_v = "stef/d_pet_pictures_v.txt"
#file_h = "stef/d_pet_pictures_h.txt"

output_file = "output/b_lovely_landscapes_sol.txt"

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
    #print(tagsSame,tags1diff,tags2diff)
    return min(tagsSame,tags1diff,tags2diff)

def main():

    #f = open(file_name, "r")
    #v = open(file_v, "w")
    #h = open(file_h, "w")

    #nb = int(f.readline())

    #for i in range(nb):
    #    line = f.readline()
    #    content = line.split()
    #
    #    if content[0] == "H":
    #        h.write(line)
    #    else:
    #        v.write(line)

    f = open(file_name, "r")

    f.readline()

    tags = [0] * 80000

    for i in range(80000):

        line = f.readline()
        content = line.split()

        nb = int(content[1])

        tags[i] = content[2:1+nb]

    count = 0

    highest_score = 36

    

    while(count < 0):

        sol = [i for i in range(80000)]

        random.shuffle(sol)

        score = 0

        for i in range(1, 80000):
            score += interest_tags(tags[sol[i-1]],tags[sol[i]])

        #print("The score of this random set is: " + str(score))

        if score > highest_score:
            out = open(output_file, "w")
            out.write("80000" + "\n")

            for nb in sol:

                out.write(str(nb) + "\n")

            highest_score = score

            print("New highscore: " + str(highest_score))

        count += 1

    print("Finished!")


if __name__ == '__main__':
    main()