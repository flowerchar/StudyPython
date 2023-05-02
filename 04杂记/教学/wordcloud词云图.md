# 词云图

### 一.什么是wordcloud?

> wordcloud是优秀的词云展示第三方库，以词语为基本单位，通过图形可视化的方式，更加直观和艺术的展示文本。

![wordcloud](D:\markdown\python\教学\pictures\20180610220951808)

所谓词云图就是统计大量词汇，并以频率大小来展示词汇



### 二. 基本使用

#### 1. 常规方法

 	1. w.generate(value:str)   向WordCloud对象加载文本
 	2. w.to_file(filename:str)   将图云生成为图像，格式为.png或者.jpg

#### 2.WordCloud参数配置

|参数|	描述|
|----|---|
|width	|指定词云对象生成图片的宽度,默认400像w=wordcloud.WordCloud(width=600)|
|height	|指定词云对象生成图片的高度,默认200像素w=wordcloud.WordCloud(height=400)|
|min_font_size|指定词云中字体的最小字号，默认4号w=wordcloud.WordCloud(min_font_size=10)|
| max_font_size |  指定词云中字体的最大字号，根据高度自动调节w=wordcloud.WordCloud（max_font_size=20） |
|font_step	| 指定词云中字体字号的步进间隔，默认为1 w=wordcloud.WordCloud(font_step=2) |
|font_path	|指定文体文件的路径，默认None   w=wordcloud.WordCloud(font_path="msyh.ttc")|
|max_words	|指定词云显示的最大单词数量,默认200w=wordcloud.WordCloud(max_words=20)|
|stop_words	|指定词云的排除词列表，即不显示的单词列表w=wordcloud.WordCloud(stop_words="Python")|
|mask	|指定词云形状，默认为长方形，需要引用imread()函数、<br>from scipy.msc import imread<br>mk=imread("pic.png")<br>w=wordcloud.WordCloud(mask=mk)|
| background_color | 指定词云图片的背景颜色，默认为黑色w=wordcloud.WordCloud(background_color="white") |

#### 3.搭配jieba分词使用

- #####  jieba库是什么？

  jieba是一款用于中文分词的第三方库

- ##### jieba三大模式：

  - 精确模式：把文本精确的切分开，不存在冗余单词；
  - 全模式：把文本中所有可能的词语都扫描出来，有冗余；
  - 搜索引擎模式：在精确模式基础上，对长词再切分。

  |常用api|说明|
  |-----|-----|
  |jieba.lcut(s)|**精确模式**，返回一个列表类型的分词结果 <br>jieba.lcut(“中国是一个伟大的国家”) <br>[‘中国’，‘是’，‘一个’，’伟大‘，’的‘，’国家‘]|
  |jieba.lcut(s,cut_all=True)|**全模式**，返回一个列表类型的分词结果，存在冗余<br> >>>jieba.lcut(“中国是一个伟大的国家”)<br> [‘中国’，‘国是’，‘一个’，’伟大‘，’的‘，’国家‘]|
|jieba.lcut_for_search(s)|**搜索引擎模式**，返回一个列表类型的分词结果，存在冗余 <br>>>>jieba.lcut_for_search(“中华人民共和国是伟大的”) <br>[‘中华’，‘华人’，’人民‘，’共和‘，’共和国‘，’中华人民共和国‘，’是‘，’伟大‘，’的‘]|
|jieba.add_word(w)|向词库增加一个**自定义词语**<br>>>>jieba.add_word(“蟒蛇语言”)|

- #####  jieba使用的坑

  - ###### SyntaxError: Non-UTF-8 code starting with ‘\xe5‘ 

    - 在py文件开头写入：  #coding:utf-8



#### 4. WordCloud的坑

- ##### 中文显示乱码

  - 临时办法：在C:\Windows\Fonts下选择一个font_path,比如华文新魏常规（STXINWEI.TTF）
  - 一劳永逸：进入解释器\Lib\site-packages\wordcloud，修改此目录下wordcloud.py第28行内容，修改为os.path.join(FILE,'STXINWEI.TTF')，并把STXINWEI.TTF放置在此目录下

- ##### ImportError: cannot import name 'imread' from 'scipy.misc' 

  - 改为 from imageio import imread
  - 将scipy库的版本还原至1.2.0版本

  ​	







*calendar*

contacts  **external**

location ->access_fine_location access_coarse 













