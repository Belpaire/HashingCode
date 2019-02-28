import random

file_name = "input/b_lovely_landscapes.txt"

#file_v = "stef/d_pet_pictures_v.txt"
#file_h = "stef/d_pet_pictures_h.txt"

input_file = "output/b_lovely_landscapes_sol_old.txt"
output_file = "output/b_lovely_landscapes_sol_2.txt"

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
    f2 = open(input_file, "w")
    f3 = open(output_file, "r")

    for line in f3:
        f2.write(line)

    f2.close()
    f3.close()

    f.readline()

    tags = [0] * 80000

    for i in range(80000):

        line = f.readline()
        content = line.split()

        nb = int(content[1])

        tags[i] = content[2:1+nb]

    count = 0

    f2 = open(input_file, "r")

    f2.readline()

    sol = [0] * 80000

    for i in range(80000):
        sol[i] = int(f2.readline())

    score = 0

    for i in range(1, 80000):
        score += interest_tags(tags[sol[i-1]],tags[sol[i]])

    highest_score = score

    while(count < 1):

        attempts = 0
        idx = range(1, len(sol)-1)

        while(attempts < 2000000):
            i1, i2 = random.sample(idx, 2)

            new_score = score
            new_score -= interest_tags(tags[sol[i1-1]],tags[sol[i1]])
            new_score -= interest_tags(tags[sol[i1]],tags[sol[i1+1]])
            new_score -= interest_tags(tags[sol[i2-1]],tags[sol[i2]])
            new_score -= interest_tags(tags[sol[i2]],tags[sol[i2+1]])

            sol[i1], sol[i2] = sol[i2], sol[i1]

            new_score += interest_tags(tags[sol[i1-1]],tags[sol[i1]])
            new_score += interest_tags(tags[sol[i1]],tags[sol[i1+1]])
            new_score += interest_tags(tags[sol[i2-1]],tags[sol[i2]])
            new_score += interest_tags(tags[sol[i2]],tags[sol[i2+1]])

            if(new_score <= score):
                sol[i1], sol[i2] = sol[i2], sol[i1]
            else:
                print("Score increased by swap: " + str(new_score))
                score = new_score

            attempts += 1

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

def main2():

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
    f2 = open(input_file, "w")
    f3 = open(output_file, "r")

    for line in f3:
        f2.write(line)

    f2.close()
    f3.close()

    f.readline()

    tags = [0] * 80000

    for i in range(80000):

        line = f.readline()
        content = line.split()

        nb = int(content[1])

        tags[i] = content[2:1+nb]

    count = 0

    f2 = open(input_file, "r")

    f2.readline()

    sol = [0] * 80000

    for i in range(80000):
        sol[i] = int(f2.readline())

    score = 0

    for i in range(1, 80000):
        score += interest_tags(tags[sol[i-1]],tags[sol[i]])

    highest_score = score

    while(count < 1):

        attempts = 0
        idx = range(1, len(sol)-1)

        while(attempts < 2000000):
            i1, i2 = random.sample(idx, 2)

            new_score = score
            new_score -= interest_tags(tags[sol[i1-1]],tags[sol[i1]])
            new_score -= interest_tags(tags[sol[i1]],tags[sol[i1+1]])
            new_score -= interest_tags(tags[sol[i2-1]],tags[sol[i2]])
            new_score -= interest_tags(tags[sol[i2]],tags[sol[i2+1]])

            sol[i1], sol[i2] = sol[i2], sol[i1]

            new_score += interest_tags(tags[sol[i1-1]],tags[sol[i1]])
            new_score += interest_tags(tags[sol[i1]],tags[sol[i1+1]])
            new_score += interest_tags(tags[sol[i2-1]],tags[sol[i2]])
            new_score += interest_tags(tags[sol[i2]],tags[sol[i2+1]])

            if(new_score <= score):
                sol[i1], sol[i2] = sol[i2], sol[i1]
            else:
                print("Score increased by swap: " + str(new_score))
                score = new_score

            attempts += 1

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

def lfsr(seed):

    for i in range(1,taps):
        feedback_bit = seed[2] ^ seed[16]

        if feedback_bit == 1:
            feedback_bit = 0
        else:
            feedback_bit = 1

        for j in range(0, 17):
            seed[j] = seed[j+1]

        seed[16] = feedback_bit

        seed_string = ""

        #for j in seed:
        #    seed_string += str(j)

    seed_string = ''.join([str(j) for j in seed])

    return (int(seed_string, 2), seed)

if __name__ == '__main__':
    main()