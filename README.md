### Academic Searcher

####1.部署需求

1. python 2.7.10
2. numpy 1.7.1
3. tornado 4.3
4. Java 1.8 （需要官方版本，而不能是Cent OS自带的版本）
5. solr 6.0
6. pysolr 3.3







####2.部署使用方法：

总的来说，整个系统的构建需要四个阶段：预处理数据集 》》训练模型参数》》建立文章索引》》运行系统.

######第一步：

首先要下载整个项目，解压到“全英文路径”中，如果有中文讲不能正常运行。

确保项目包含数据集文件.csv等文件， 如果没有，需要运行 ./preprocess/ldp_fea.py 生成


######第二步：

确保项目中./model目录包含params.json文件，如果没有,需要运行 ./preprocess/train.py 生成.

######第三步：

在solr中新建一个文档集 http://localhost:8983/solr/paper

######第四步：

如果项目中没有./model/academic.db文件，需要运行build_index.py中的select_paper()函数生成

然后为了建立用于搜索引擎的索引，需要params.json文件，并在终端输入 
$ python ./model/build_index.py。


######第五步：

运行程序，在终端输入

$ python ./main.py

然后在浏览器打开 

http://localhost:8911

