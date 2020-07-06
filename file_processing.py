import glob
import os
import os,shutil
import numpy as np
import pandas as pd

#保存list[list[]]的数据到txt文件
def write_data(filename, content_list,mode='w'):

    with open(filename, mode=mode, encoding='utf-8') as f:
        for line_list in content_list:
            # 将list转为string
            line=" ".join('%s' % id for id in line_list)
            f.write(line+"\n")

#保存list[]的数据到txt文件，每个元素分行
#list_data:需要保存的数据,type->list
def write_list_data(filename, list_data,mode='w'):

    with open(filename, mode=mode, encoding='utf-8') as f:
        for line in list_data:
            # 将list转为string
            f.write(str(line)+"\n")


#读取txt数据函数
def read_data(filename,split=" ",convertNum=True):

    with open(filename, mode="r",encoding='utf-8') as f:
        content_list = f.readlines()
        if split is None:
            content_list = [content.rstrip() for content in content_list]
            return content_list
        else:
            content_list = [content.rstrip().split(split) for content in content_list]
        if convertNum:
            for i,line in enumerate(content_list):
                line_data=[]
                for l in line:
                    if is_int(l):  # isdigit() 方法检测字符串是否只由数字组成,只能判断整数
                        line_data.append(int(l))
                    elif is_float(l):  # 判断是否为小数
                        line_data.append(float(l))
                    else:
                        line_data.append(l)
                content_list[i]=line_data
    return content_list


def is_int(str):
    # 判断是否为整数
    try:
        x = int(str)
        return isinstance(x, int)
    except ValueError:
        return False


def is_float(str):
    # 判断是否为整数和小数
    try:
        x = float(str)
        return isinstance(x, float)
    except ValueError:
        return False


def list2str(content_list):
    content_str_list=[]
    for line_list in content_list:
        line_str = " ".join('%s' % id for id in line_list)
        content_str_list.append(line_str)
    return content_str_list

#获取文件列表
#basename: 返回的列表是文件名（True），还是文件的完整路径(False)
def get_images_list(image_dir,postfix=['*.jpg'],basename=False):

    images_list=[]
    for format in postfix:
        image_format=os.path.join(image_dir,format)
        image_list=glob.glob(image_format)
        if not image_list==[]:
            images_list+=image_list
    images_list=sorted(images_list)
    if basename:
        images_list=get_basename(images_list)
    return images_list

def get_basename(file_list):
    dest_list=[]
    for file_path in file_list:
        basename=os.path.basename(file_path)
        dest_list.append(basename)
    return dest_list

def copyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        # print("copy %s -> %s"%( srcfile,dstfile))

#合并两个List
def merge_list(data1, data2):

    if not len(data1) == len(data2):
        return
    all_data = []
    for d1, d2 in zip(data1, data2):
        all_data.append(d1 + d2)
    return all_data


#切分数据
def split_list(data, split_index=1):

    data1 = []
    data2 = []
    for d in data:
        d1 = d[0:split_index]
        d2 = d[split_index:]
        data1.append(d1)
        data2.append(d2)
    return data1, data2


#获取file_dir目录下，所有文本路径，包括子目录文件
def getFilePathList(file_dir):

    filePath_list = []
    for walk in os.walk(file_dir):
        part_filePath_list = [os.path.join(walk[0], file) for file in walk[2]]
        filePath_list.extend(part_filePath_list)
    return filePath_list


#获得file_dir目录下，后缀名为postfix所有文件列表，包括子目录
def get_files_list(file_dir, postfix=None):

    file_list = []
    filePath_list = getFilePathList(file_dir)
    if postfix is None:
        file_list = filePath_list
    else:
        postfix = [p.split('.')[-1] for p in postfix]
        for file in filePath_list:
            basename = os.path.basename(file)  # 获得路径下的文件名
            postfix_name = basename.split('.')[-1]
            if postfix_name in postfix:
                file_list.append(file)
    file_list.sort()
    return file_list


#获取files_dir路径下所有文件路径，以及labels,其中labels用子级文件名表示
#files_dir目录下，同一类别的文件放一个文件夹，其labels即为文件的名
#postfix表示后缀名
def gen_files_labels(files_dir,postfix=None):

    # filePath_list = getFilePathList(files_dir)
    filePath_list=get_files_list(files_dir, postfix=postfix)
    print("files nums:{}".format(len(filePath_list)))
    # 获取所有样本标签
    label_list = []
    for filePath in filePath_list:
        label = filePath.split(os.sep)[-2]
        label_list.append(label)

    labels_set = list(set(label_list))
    print("labels:{}".format(labels_set))

    # 标签统计计数
    # print(pd.value_counts(label_list))
    return filePath_list, label_list

#根据name_table解码label
def decode_label(label_list,name_table):

    name_list=[]
    for label in label_list:
        name = name_table[label]
        name_list.append(name)
    return name_list

#根据name_table，编码label
def encode_label(name_list,name_table,unknow=0):

    label_list=[]
    for name in name_list:
        if name in name_table:
            index = name_table.index(name)
        else:
            index = unknow
        label_list.append(index)
    return label_list

if __name__=='__main__':
    filename = 'test.txt'
    w_data = [['1.jpg', 'dog', 200, 300, 1.0], ['2.jpg', 'dog', 20, 30, -2]]
    print("w_data=", w_data)
    write_data(filename,w_data, mode='w')
    r_data = read_data(filename)
    print('r_data=', r_data)