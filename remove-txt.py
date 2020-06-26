infile = "./train_list.txt"
outfile = "./list.txt"

delete_list = ["cat_12_train/"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()