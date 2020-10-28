import torch
from tqdm import tqdm
import time

# epochs=3
# batchs=10000
# batch_size=3
# nums_img=batchs*batch_size
# for e in range(3):
#     with tqdm(total=nums_img, desc=f'Epoch { e+1}/{epochs}', unit='img', ncols=None) as pbar:  # ncols:显示的列宽度
#         for i in range(batchs):
#             time.sleep(0.1) # 单位：s
#             pbar.set_postfix(**{'one':1, 'two':2})  # 在bar的末尾添加额外信息
#             pbar.set_description('aaa')  # 设置bar的描述信息，显示在bar前
#             pbar.update(batch_size)  # 更新进度条

# epochs=3
# batchs=10
# # batch_size=3
# # nums_img=batchs*batch_size
# dataloader=[i for i in range(batchs)]
# pbar = tqdm(enumerate(dataloader), total=batchs)
# for e in range(epochs):
#     for i, v in pbar:
#         time.sleep(1)
#         s=('%5s' )%('%g/%g' % (e+1, epochs))
#         pbar.set_description(s)


