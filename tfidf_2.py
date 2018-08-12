# -*- coding: utf-8 -*-
# Roc-J

import jieba.posseg as pseg
import codecs
import pandas as pd
from gensim import corpora, models, similarities


# 构建停用词表
stop_words = './stop_words.txt'
stopwords = codecs.open(stop_words,'r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]
stop_flag = [ 'c','d', 'p', 't', 'uj', 'u', 'f', 'r']  #保留数字和百分号

def tokenization(title):
    result = []
    words = pseg.cut(title)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

def train_text():
    # 训练文本数据
    all_doc = []
    datas = pd.read_csv("./dataset/train_data.csv")
    titles = datas['title']
    for title in titles:
        all_doc.append(title)

    # 对目标文档进行分词
    all_doc_list = []
    for doc in all_doc:
        doc_list = tokenization(doc)
        all_doc_list.append(doc_list)
# jieba.cut_for_search

    # 测试文档进行分词
    test_doc = []
    test_datas = pd.read_csv("./dataset/test_data.csv")
    test_titles = test_datas["title"]
    for title in test_titles:
        test_doc.append(title)
    test_doc_list = []
    for doc in test_doc:
        doc_list = tokenization(doc)
        test_doc_list.append(doc_list)

    # 制作语料库
    dictionary = corpora.Dictionary(all_doc_list)
    dictionary.keys()
    print('-----',dictionary.keys())
    return 
    dictionary.token2id
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    tfidf = models.TfidfModel(corpus)
    results = []
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    for doc_test_list in test_doc_list:
        doc_test_vec = dictionary.doc2bow(doc_test_list)
    
        sim = index[tfidf[doc_test_vec]]
        similiar_sorted = sorted(enumerate(sim), key=lambda item: -item[1])[:21]
        indexs = [str(item[0]+1) for item in similiar_sorted]
        results.append(" ".join(indexs))

    with open("./result_bl2/results_quchong.txt", "w") as f:
        f.write('source_id'+'\t'+'target_id'+'\t' + 'sim' + '\t' +'target_title\n')
        for item in results:
            item = item.strip().split()
            for i in range(1, 21):
                f.write(str(item[0]) + "\t" + str(item[i]) + "\t" + str(sim[1]) + "\t" + datas['title'][int(item[i]) - 1] + "\n")
    f.close()
	
if __name__ == "__main__":
    train_text()
    # with open("./result_bl2/results_quchong.txt", "r") as f, open("./result_bl2/5.5_submisson_bl2.txt", "w") as wf:
        # datas = f.readlines()
        # wf.write('source_id'+'\t'+'target_id'+'\t'+'target_title\n')
        # for data in datas:
            # data = data.strip().split("\t")
            # wf.write(data[0] + "\t" + data[1] + "\n")

