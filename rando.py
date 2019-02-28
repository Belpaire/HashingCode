

file_name = "input/d_pet_pictures.txt"

file_v = "stef/d_pet_pictures_v.txt"
file_h = "stef/d_pet_pictures_h.txt"

def main():

    f = open(file_name, "r")
    v = open(file_v, "w")
    h = open(file_h, "w")

    nb = int(f.readline())

    for i in range(nb):
        line = f.readline()
        content = line.split()

        if content[0] == "H":
            h.write(line)
        else:
            v.write(line)

if __name__ == '__main__':
    main()