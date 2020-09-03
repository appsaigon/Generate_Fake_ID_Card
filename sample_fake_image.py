import os
import random

import cv2
import numpy as np
from sklearn.model_selection import train_test_split

fake_path = '/home/list_99/Python/Generate_Fake_ID_Card/fake'


def get_image(path):
    '''
    Get all filename in a direction
    Parameter
    ---------
    path:str, path to direction

    Return
    ------
    Return a list contains all filename no duplicate without extention in direction
    
    Example
    -------
    >>> cd image
    >>> tree
    .
    ├── a.png
    ├── b.png
    └── a.mask.png
    >>> get_image('./image')
    ['./image/a', './image/b']
    '''
    file = os.listdir(path)
    fn = set()
    for i in file:
        if i.split('.')[0] == '':
            continue
        fn.add(path + '/' + i.split('.')[0])
    return list(fn)


def count_fake_point(mask):
    '''
    return number of point with values equal to 255 (white point) in mask
    '''
    return mask[mask == 255].shape[0]


def sample_fake(img, mask):
    kernel_size = 64
    stride = 8
    threshold = 2000
    samples = []
    coordinates = []
    if len(mask.shape) > 2:
        mask = mask[:, :, 0]
    for y_start in range(0, img.shape[0] - kernel_size + 1, stride):
        for x_start in range(0, img.shape[1] - kernel_size + 1, stride):
            rand_x = random.randint(-7,7)
            rand_y = random.randint(-7,7)
            
            fake_point = count_fake_point(mask[y_start:y_start + kernel_size + rand_y, x_start:x_start + kernel_size + rand_x])
            
            if (fake_point > 100) and (kernel_size * kernel_size - fake_point > threshold):
                samples.append(img[y_start:y_start + kernel_size + rand_y, x_start:x_start + kernel_size + rand_x, :3])
                coordinates.append((x_start,y_start))
    return samples,coordinates


def main():
    fns = get_image(fake_path)

    y = np.array([0]*len(fns))
    fns_train ,fns_valid,_,_=train_test_split(fns,y,test_size=0.2,stratify=y)
    f = open('./patch_coord_neg.txt','w')

    for idx,fn in enumerate(fns_train):
        print(fn+'.jpg')
        img = cv2.imread(fn + '.jpg')
        mask = cv2.imread(fn + '.mask.png',0)
        #for s in sample_fake(img, mask)[1]:
            #f.write(fn.split('/')[-1]+'.png'+', {}, {}\n'.format(s[0],s[1]))
        for s in sample_fake(img,mask)[0]:
            cv2.imwrite('./train/tp/train_tp_{}.png'.format(idx),s)
        
    for idx,fn in enumerate(fns_valid):
        print(fn+'.jpg')
        img = cv2.imread(fn + '.jpg')
        mask = cv2.imread(fn + '.mask.png',0)
        #for s in sample_fake(img, mask)[1]:
            #f.write(fn.split('/')[-1]+'.png'+', {}, {}\n'.format(s[0],s[1]))
        for s in sample_fake(img,mask)[0]:
            cv2.imwrite('./valid/tp/valid_tp_{}.png'.format(idx),s)

    print('done')

if __name__ == '__main__':
    main()