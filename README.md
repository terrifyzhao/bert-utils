# bert-utils

本文基于Google开源的[BERT](https://github.com/google-research/bert)代码进行了进一步的简化，方便生成句向量与做文本分类

---

***** New July 1st, 2019 *****
+ 修改句向量`graph`文件的生成方式，提升句向量启动速度。不再每次以临时文件的方式生成，首次执行extract_feature.py时会创建`tmp/result/graph`，
再次执行时直接读取该文件，如果`args.py`文件内容有修改，需要删除`tmp/result/graph`文件
+ 修复同时启动两个进程生成句向量时代码报错的bug
+ 修改文本匹配数据集为QA_corpus，该份数据相比于蚂蚁金服的数据更有权威性

---

1、下载BERT中文模型 

下载地址: https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip

2、把下载好的模型添加到当前目录下

3、句向量生成

生成句向量不需要做fine tune，使用预先训练好的模型即可，可参考`extract_feature.py`的`main`方法，注意参数必须是一个list。

首次生成句向量时需要加载graph，并在output_dir路径下生成一个新的graph文件，因此速度比较慢，再次调用速度会很快
```
from bert.extrac_feature import BertVector
bv = BertVector()
bv.encode(['今天天气不错'])
```

4、文本分类

文本分类需要做fine tune，首先把数据准备好存放在`data`目录下，训练集的名字必须为`train.csv`，验证集的名字必须为`dev.csv`，测试集的名字必须为`test.csv`，
必须先调用`set_mode`方法，可参考`similarity.py`的`main`方法，

训练：
```
from similarity import BertSim
import tensorflow as tf

bs = BertSim()
bs.set_mode(tf.estimator.ModeKeys.TRAIN)
bs.train()
```

验证：
```
from similarity import BertSim
import tensorflow as tf

bs = BertSim()
bs.set_mode(tf.estimator.ModeKeys.EVAL)
bs.eval()
```

测试：
```
from similarity import BertSim
import tensorflow as tf

bs = BertSim()
bs.set_mode(tf.estimator.ModeKeys.PREDICT)
bs.test()
```

5、DEMO中自带了QA_corpus数据集，这里给出[地址](http://icrc.hitsz.edu.cn/info/1037/1162.htm)，
该份数据的生成方式请参阅附件中的论文`The BQ Corpus.pdf`