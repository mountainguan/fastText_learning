import jieba

inFile = 'data/data.txt'
outFile = 'data/trained.txt'

f = open(inFile,'r')
writer = open(outFile,'w')
for line in f.readlines():
    splitor = line.split()
    # 默认切割方法
    text = jieba.cut_for_search(splitor[0])
    text = " ".join(text) + " " + splitor[1] + '\n'
    writer.writelines(text)

f.close()
writer.close()
