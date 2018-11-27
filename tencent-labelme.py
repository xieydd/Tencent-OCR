# -*- coding: utf-8 -*-

import json
import codecs
import glob
import os
import copy


if __name__ == '__main__':

    #insert your own configuration
    img_path = "/Users/xieyuandong/Downloads/photo/"
    tencent_json = "/Users/xieyuandong/Downloads/photo/json/"
    label_json = "/Users/xieyuandong/Workspace/python/label/"
    label_template_json = "/Users/xieyuandong/Workspace/python/Tencent-OCR/templete.json"

    for files in glob.glob(tencent_json+ '*'):
        with open(label_template_json) as f:
            dic = json.load(f)
        if not os.path.exists(label_json):
            os.mkdir(label_json)
        num = files.split("/")[-1]
        json_path = label_json + num + ".json"
        dic['imagePath'] = img_path + num + ".jpg"
        
        for file in glob.glob(files + "/*"):
            x_min = 0
            y_min = 0
            x_max = 0
            y_max = 0

            dic_copy = copy.deepcopy(dic["shapes"][0])
            temp = dic_copy
            with open(file) as f:
                dict = json.load(f)
                width = dict['width']
                height = dict['height']
                x_min = dict['x']
                y_min = dict['y']

                x_max = x_min + width
                y_max = y_min + height
                temp["points"][0][0] = x_min
                temp["points"][0][1] = y_min
                temp["points"][1][0] = x_max
                temp["points"][1][1] = y_max
            dic['shapes'].append(temp)
                #print json.dumps(dic, indent=4, ensure_ascii=False, encoding='utf-8')
        with open(json_path,"a") as f:
            dic['shapes'].remove(dic['shapes'][0])
            json.dump(dic, f, indent=4)
