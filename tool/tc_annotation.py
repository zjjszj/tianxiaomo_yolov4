import json
from collections import defaultdict
from tqdm import tqdm
import os



# adjust annotation of Tian Chi street char dataset to this model.
# source annotation(json): img_name height label left top width
# target annotation(txt):image_path1 x1,y1,x2,y2,id x1,y1,x2,y2,id x1,y1,x2,y2,id ...


train_img='/kaggle/input/streetclassify/input/input/train'
train_json='/kaggle/input/streetclassify/input/input/train.json'
val_img='/kaggle/input/streetclassify/input/input/val'
val_json='/kaggle/input/streetclassify/input/input/val.json'


def tc2annotation(source_path, img_path, output_path):
    # load json file
    name_box_id = defaultdict(list)
    id_name = dict()
    with open(source_path, encoding='utf-8') as f:
        data = json.load(f)

    for k,v in data.items():
        path=os.path.join(img_path, k)
        height=v['height']
        label=v['label']
        x1=v['left']
        y1=v['top']
        width=v['width']
        x2=x1+width
        y2=y1+height
        for i in range(len(x1)):
            name_box_id[path].append(x1[i])
            name_box_id[path].append(y1[i])
            name_box_id[path].append(x2[i])
            name_box_id[path].append(y2[i])
            name_box_id[path].append(label[i])
    # print(name_box_id)

    # write to train.txt
    with open(output_path, 'w') as f:
        for key in tqdm(name_box_id.keys()):
            f.write(key)
            box_infos = name_box_id[key]
            for i in range(0, len(box_infos), 5):
                f.write(" ")
                s=",".join([str(box_infos[i]), str(box_infos[i+1]), str(box_infos[i+2]), str(box_infos[i+3]), str(box_infos[i+4])])
                f.write(s)
            f.write('\n')

if __name__ == '__main__':
    # tc2annotation(val_json, val_img, 'val.txt')
    tc2annotation('../test.json', 'file_path',  'train.txt')