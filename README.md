![](https://github.com/laidy3/fintech/blob/master/photos/title.png)

# 招商银行财经新闻分析
队伍名：SYSU-laidy  
最终成绩：0.1361 排名第1  
算法模型：BM25+去停用词+动态权重  
## 赛题背景  

[赛题连接](https://www.nowcoder.com/activity/2018cmbchina/bigdata/2)

财经新闻作为重要却海量的投资数据，无时无刻不在影响着投资者们的投资决策，为了更好地提示客户当下新闻事件对应的投资机会和投资风险，本课以研发“历史事件连连看”为目的，旨在根据当前新闻内容从历史事件中搜索出相似新闻报道，后期可以结合事件与行情，辅助客户采取相应投资策略。  
该赛题是让参赛者为每一条测试集数据寻找其最相似的TOP 20条新闻（不包含测试新闻本身），我们会根据参赛者提交的结果和实际的数据进行对比，采用mAP值作为评价指标。

# 主要思路
使用bm25算法+去停用词+动态权重  
bm25经过调参成绩是0.12+，去停用词后成绩是0.129+
去停用词时不要去掉数字和字母。  
动态权重思路来自论文《A SIMPLE BUT TOUGH-TO-BEAT BASELINE FOR SEN- TENCE EMBEDDINGS》——[作者代码](https://github.com/PrincetonML/SIF)  
权重分配思路：对每条测试样例，分词的的权重都是0.5, 再针对性的给部分分词给于较高权重(0.8、0.9)如德国地质、美国纽约联储Nowcast，部分分词给于较低权重(0、0.1)，如陈茂波。

# 一些尝试
* 分词+tfidf+各种调参 成绩0.091左右 效果不好 对比过几种不同分词如哈工大、清华、jieba等，结巴是最好的
* Simhash算法 成绩0.07左右
* doc2vec、sentence2vec效果都不好
* bm25 原始的bm25线上成绩是0.115+ 调过参后是0.12+ 修改的参数为（k=2 b=0.87 e=0.21）

# 文件说明
* simhash.py  
使用simhash算法进行文本相似度分析
* tfidf_1.py  
使用TF-IDF算法进行文本相似度分析 参考Roc-J分享的[代码](https://github.com/Roc-J/zhaoshang_economic_news)
* tfidf_2.py  
去停用词 使用TF-IDF算法进行文本相似度分析
* model.py   
bm25模型定义
* main.py
使用bm25进行文本相似性分析
* stop_words.txt
停用词表

# 结果
![](https://github.com/laidy3/fintech/blob/master/photos/result.png)

