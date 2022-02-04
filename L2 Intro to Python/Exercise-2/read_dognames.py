dognames_dic = dict()
with open("dognames.txt") as f:
    for line in f:
        line = line.strip()
        if line not in dognames_dic.keys():
            dognames_dic[line]=1
        # print(line)

# print(len(dognames_dic))
print(dognames_dic)

if 'golden retriever' in dognames_dic.keys():
    print('present - golden')
