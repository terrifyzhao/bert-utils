import pickle
from graph import set_logger
from termcolor import colored

logger = set_logger(colored('BERT_VEC', 'yellow'))
bert_file_name = 'bert_data.pkl'


class BertData:
    def __init__(self):
        self.dic = {}
        self._read_dic()

    # 批量插入数据
    def add_batch_data(self, keys, values):
        for key, value in zip(keys, values):
            self.dic[key] = value

    # 插入单条数据
    def add_data(self, key, value):
        self.dic[key] = value

    # 根据key删除数据
    def delete_data(self, key):
        if self.dic and self.dic.get(key, ''):
            self.dic.pop(key)

    # 根据key获取数据
    def get_data(self, key):
        return self.dic.get(key, '')

    # 获取全部数据
    def get_all_data(self):
        return self.dic

    # 提交
    def commit(self):
        self._save_dic()

    def _save_dic(self):
        try:
            with open(bert_file_name, 'wb')as file:
                pickle.dump(self.dic, file)
            logger.info('bert data saved successfully')
        except:
            logger.info('save bert data failed')

    def _read_dic(self):
        try:
            with open(bert_file_name, 'rb')as file:
                self.dic = pickle.load(file)
        except FileNotFoundError:
            logger.info('local bert data is none')


if __name__ == '__main__':
    bd = BertData()
    data = []
    vec = []
    import numpy as np

    for i in range(30000):
        data.append('阿迪和考虑就鞍山市会计法哈三联空间和福利卡就很烦' + str(i))
        vec.append(np.random.rand(768))
    bd.add_batch_data(data, vec)
    # 增删改需要调用commit方法才会修改本地缓存的内容，查询不需要调用该方法
    bd.commit()
    # bd.delete_data('上午好啊天气真的不错0')
    # res = bd.get_data('上午好啊天气真的不错1')
    # bd.add_data('上午好啊天气真的不错test', [1, 2, 3])
    # res = bd.get_all_data()
    # print(res.keys())
    # for i in res.items():
    #     print(i[0], ':', i[1])
    # print(res.values())
