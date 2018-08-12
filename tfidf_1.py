# -*- coding: utf-8 -*-


import jieba
import pandas as pd
from gensim import corpora, models, similarities

jieba.enable_parallel(4)
jieba.load_userdict("userdict.txt")

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
        doc_list = [word for word in list(jieba.cut(doc))]
        all_doc_list.append(doc_list)


    # 测试文档进行分词
    test_doc = []
    test_datas = pd.read_csv("./dataset/test.csv")
    test_titles = test_datas["title"]
    for title in test_titles:
        test_doc.append(title)
    test_doc_list = []
    for doc in test_doc:
        doc_list = [word for word in list(jieba.cut(doc))]
        test_doc_list.append(doc_list)
	
    # 制作语料库
    dictionary = corpora.Dictionary(all_doc_list)
    dictionary.keys()
    dictionary.token2id
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    tfidf = models.TfidfModel(corpus)
    #corpus_tfidf = tfidf[corpus]
	
    #lsi = models.LsiModel(corpus_tfidf)  
    #corpus_lsi = lsi[corpus_tfidf]
	
    #lda = models.LdaModel(corpus, id2word=dictionary, num_topics=100)
    results = []
	
    index = similarities.SparseMatrixSimilarity(tfidf[corpus]))
    #index = similarities.SparseMatrixSimilarity(corpus_lsi, num_features=len(dictionary.keys()))
    for doc_test_list in test_doc_list[-1:]:
        doc_test_vec = dictionary.doc2bow(doc_test_list)

        sim = index[tfidf[doc_test_vec]]
        similiar_sorted = sorted(enumerate(sim), key=lambda item: -item[1])[:201]
        indexs = [str(item[0]+1) for item in similiar_sorted]
        results.append(" ".join(indexs))

    #print('length', len(test_doc), len(test_titles))
    # 制作语料库

    with open("./result_bl1/5.8results_50-500.txt", "w") as f:
        f.write('source_id'+'\t'+'target_id'+'\t' +'target_title\n')
        for item in results:
            item = item.strip().split()
            for i in range(1, 301):
                f.write(str(item[0]) + "\t" + str(item[i]) + "\t" + datas['title'][int(item[i]) - 1] + "\n")
    f.close()

if __name__ == "__main__":
    train_text()
    print('end')

