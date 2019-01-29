# bert_feature

how to use Bert generate the sentence vector

1、download the model 

model path: https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip

2、Move the model in the same directory

3、init BertVector object and invokes the encode method, the param must be list
```
from bert.extrac_feature import BertVector
bv = BertVector()
bv.encode(['你好'])
```
