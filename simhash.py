# -*- coding: utf-8 -*-
from simhash import Simhash
import pandas as pd
all_doc = []
datas = pd.read_csv("./dataset/train_data.csv", encoding='utf-8')
titles = datas['title']
for title in titles:
    all_doc.append(title)

test_doc = []
test_datas = pd.read_csv("./dataset/test.csv", encoding='utf-8')
test_titles = test_datas["title"]
for title in test_titles:
    test_doc.append(title)


for s in test_doc[0:1]:
	sim = []
	results = []
	for d in all_doc[30]:
		sim.append(Simhash(s).distance(Simhash(d)))
	similiar_sorted = sorted(enumerate(sim), key=lambda item: -item[1])[:21]
	indexs = [str(item[0]+1) for item in similiar_sorted]
	
	results.append(" ".join(indexs))

	with open("./results.txt", "w") as f:
		f.write('source_id'+'\t'+'target_id' + '\t'+'target_title\n')
        for item in results:
            item = item.strip().split()
            for i in range(1, 21):
                f.write(item[0] + "\t" + item[i] + '\t' + datas['title'][int(item[i]) - 1] + "\n")
	f.close()
print('--------------end------------')
# print Simhash(s).distance(Simhash(s))
# print Simhash('aa').distance(Simhash('aa'))