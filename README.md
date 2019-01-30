# bert-utils

本文基于Google开源的[BERT](https://github.com/google-research/bert)代码进行了进一步的简化，方便生成句向量与做文本分类

1、下载BERT中文模型 

下载地址: https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip

2、把下载好的模型添加到当前目录下

3、句向量生成

生成句向量不需要做fine tune，使用预先训练好的模型即可，可参考`extract_feature.py`的`main`方法，注意参数必须是一个list
```
from bert.extrac_feature import BertVector
bv = BertVector()
bv.encode(['你好'])
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
bs.test
```

5、DEMO中自带了蚂蚁金服的测试数据供大家使用