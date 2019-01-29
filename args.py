import os
from enum import Enum

file_path = os.path.dirname(__file__)

model_dir = os.path.join(file_path, 'chinese_L-12_H-768_A-12/')
config_name = os.path.join(model_dir, 'bert_config.json')
ckpt_name = os.path.join(model_dir, 'bert_model.ckpt')

output_dir = os.path.join(model_dir, '../tmp/result/')

vocab_file = os.path.join(model_dir, 'vocab.txt')
data_dir = os.path.join(model_dir, '../data/')

max_seq_len = 32

layer_indexes = [-2, -3, -4]

batch_size = 128

gpu_memory_fraction = 0.8

learning_rate = 0.00005

num_train_epochs = 10

use_gpu = False
if use_gpu:
    device_id = '0'
else:
    device_id = '-1'
