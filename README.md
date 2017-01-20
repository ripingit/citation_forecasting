### Citation Forecasting

####1.简介
论文引用次数预测Demo，基于微软学术图历史数据预测论文引用次数上升趋势, 同时包含前端、后台、模型算法。

####2.目录结构

项目基于Tornado，一个高速便捷的Web服务器。

./main.py 主文件

./common.py 相当于全局配置文件，可以在这里修改项目配置

./controller/* 提供后端各个request handler

./service/* 负责基于训练好的模型预测论文引用次数

./preprocess/*  如果模型没有实现训练好，那么需要运行这个目录中的程序训练模型

./static/* CSS、JS等静态文件

./view/* Tornado模板文件


####3.部署需求

1. python 2.7.10
2. numpy 1.7.1
3. tornado 4.3
4. Java 1.8 （需要Oracle官方版本）
5. solr 6.0
6. pysolr 3.3




####4.部署方法：


######第一步：

首先要下载整个项目，解压到“全英文路径”中，如果有中文则不能正常运行。

确保项目包含数据集文件.csv等文件， 如果没有，需要运行 ./preprocess/ldp_fea.py 生成


######第二步：

确保项目中./model目录包含params.json文件，如果没有,需要运行 ./preprocess/train.py 生成.

######第三步：

启动solr引擎，然后在solr中新建一个文档集 http://localhost:8983/solr/paper

启动
$ bin/solr start -cloud -noprompt


建立索引：
$ bin/solr create -c paper

关闭：
$ bin/solr stop -all
$ rm -Rf example/cloud/

全文检索：
$ bin/post -c gettingstarted docs/

######第四步：

建立用于搜索引擎的索引，需要params.json文件，并在终端输入 
$ python ./preprocess/build_index.py。

如果项目中没有./preprocess/academic.db文件，需要运行build_index.py中的select_paper()函数生成

######第五步：

运行程序，在终端输入

$ python ./main.py

然后在浏览器打开

http://localhost:8911

####5.截图

![](./doc/citation.png)


####6.Reference

X Liu, J Yan, S Xiao, X Wang, H Zha, S Chu. On Predictive Patent Valuation: Forecasting Patent Citations and Their Types. AAAI 2017.


S Xiao, J Yan, C Li, B Jin, X Wang, H Zha, X Yang, MC Stephen. On modeling and predicting individual paper citation count over time. IJCAI 2016.



