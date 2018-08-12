# -*- coding: utf-8 -*-
import jieba,time
import pandas as pd
from model import Model
from gensim import corpora, models, similarities

jieba.enable_parallel(4)

def start():

	# 读取训练集
    all_doc = []
    datas = pd.read_csv("./dataset/train_data.csv")
    titles = datas['title']
    for title in titles:
        all_doc.append(title)

    # 对训练集进行分词
    all_doc_list = []
    for doc in all_doc:
        doc_list = [word for word in jieba.cut(doc)]
        all_doc_list.append(doc_list)

	#字典过滤
    dictionary = corpora.Dictionary(all_doc_list)
    dictionary.filter_extremes(no_below=2, no_above=1, keep_n=180000)
	
	# 读取并对测试集进行分词
    test_doc = []
    test_datas = pd.read_csv("./dataset/test_data.csv", encoding="gbk")
    test_titles = test_datas["title"]
    for title in test_titles:
        test_doc.append(title)
    test_doc_list = []
    for doc in test_doc:
        doc_list = [word for word in jieba.cut(doc)]
        test_doc_list.append(doc_list)
	
	#数据转换为字典
	train_doc_id_list = [dictionary.doc2idx(doc) for doc in all_doc_list]
	test_doc_id_list = [dictionary.doc2idx(doc) for doc in test_doc_list]
	
	#加载模型
    model = Model(train_doc_id_list) 
    average_idf = sum(map(lambda k: float(model.idf[k]), model.idf.keys())) / len(model.idf.keys())

	#预测
    results = []
    for doc_test_list in test_doc_id_list:
        scores = model.get_scores(doc_test_list,average_idf)
        similiar_sorted = sorted(enumerate(scores), key=lambda item: -item[1])[:21]
        indexs = [str(item[0]+1) for item in similiar_sorted]
        results.append(" ".join(indexs))
	
	#读取中间文件(加权结果)
	# with open("fine.txt", "r") as g:
		# cache = g.readlines()
	# g.close()
	
    with open("./final.txt", "w") as f:  #写入结果文件
        f.write('source_id'+'\t'+'target_id' + '\t' +'target_title\n')
        for item in results[:]:
            item = item.strip().split()
            for i in range(1, 21):
                f.write(str(item[0]) + "\t" + str(item[i])  + "\t" + datas['title'][int(item[i]) - 1] + "\n")

    f.close()

if __name__ == "__main__":
	t=time.time()
	start()
	print('cost: ', time.time()-t)

