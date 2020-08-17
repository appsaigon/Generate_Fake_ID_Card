#%%
import random
import cv2
import numpy as np
from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageEnhance,ImageOps
#%%
font1 = ImageFont.truetype('/home/list_99/Python/Generate_Fake_ID_card/font/Roboto-Bold.ttf',size=18)
font2 = ImageFont.truetype('/home/list_99/Python/Generate_Fake_ID_card/font/Inter-Medium-slnt=0.ttf',size=19)
font3 = ImageFont.truetype('/home/list_99/Python/Generate_Fake_ID_card/font/Roboto-Medium.ttf',size=25)
font4 = ImageFont.truetype('/home/list_99/Python/Generate_Fake_ID_card/font/Roboto-Medium.ttf',size=19)
font5 = ImageFont.truetype('/home/list_99/Python/Generate_Fake_ID_card/font/Inter-Medium-slnt=0.ttf',size=14)


pattern_file_path = '/home/list_99/Python/Generate_Fake_ID_card/front.jpg'
avatar_file_path = '/home/list_99/Python/Generate_Fake_ID_card/avatar'
firstname_file_path = '/home/list_99/Python/Generate_Fake_ID_card/name/firstname.txt'
middlename_file_path = '/home/list_99/Python/Generate_Fake_ID_card/name/middlename.txt'
lastname_file_path = '/home/list_99/Python/Generate_Fake_ID_card/name/lastname.txt'
commune_file_path = '/home/list_99/Python/Generate_Fake_ID_card/address/commune.txt'
district_file_path = '/home/list_99/Python/Generate_Fake_ID_card/address/district.txt'
province_file_path = '/home/list_99/Python/Generate_Fake_ID_card/address/province.txt'

n=53

first = open(firstname_file_path,'r').read().split('\n')
middle = open(middlename_file_path,'r').read().split('\n')
last = open(lastname_file_path,'r').read().split('\n')
commune = open(commune_file_path,'r').read().split('\n')
district = open(district_file_path,'r').read().split('\n')
province = open(province_file_path,'r').read().split('\n')
gender_types = ['Nam','Nữ']
brightness = [0.95,0.9,0.85,0.8]
origin = Image.open(pattern_file_path)

for x in range(200):
    img = origin.copy()
    rand = random.randint(0,32)
    ava = Image.open(avatar_file_path+'/avatar'+str(rand)+'.jpg')

    draw = ImageDraw.Draw(img)
    name = random.choice(first) + ' ' + random.choice(middle) + ' ' +random.choice(last)
    
    bird = str(random.randint(1,31)) + '/' + str(random.randint(1,12)) + '/' + str(random.randint(1960,2004))

    IDnumber = [random.randint(0,9) for i in range(12)]
    IDnumber = ' '.join(str(i) for i in IDnumber)
    sex = random.choice(gender_types)
    address = random.choice(commune)+', '+random.choice(district)+', '+random.choice(province)
    size = (3*n+random.randint(-5,5) , 4*n+random.randint(-5,5))
    r1 = random.randint(0,50)
    r2 = random.randint(0,50)
    r3 = random.randint(0,50)
    r4 = random.randint(0,50)
    r5 = random.randint(0,50)
    r6 = random.randint(0,50)
    draw.text((323,170+random.randint(-3,3)), name,(r1,r1,r1), font=font1)
    draw.text((368,209+random.randint(-3,3)),bird,(r2,r2,r2),font=font2)
    draw.text((280,109+random.randint(-3,3)),IDnumber,(204,102,0),font=font3)
    draw.text((278,242+random.randint(-3,3)),sex,(r3,r3,r3),font=font4)
    draw.text((444,240+random.randint(-3,3)),'Việt Nam',(r4,r4,r4),font=font4)
    draw.text((290,274+random.randint(-3,3)),address,(r5,r5,r5),font=font4)
    draw.text((316,306+random.randint(-3,3)),address,(r6,r6,r6),font=font4)
    draw.text((145+random.randint(-3,3), 363 + random.randint(-3,3)),'29/1/2024',(0,0,0),font=font5)

    enhancer = ImageEnhance.Brightness(ava)
    ava = enhancer.enhance(random.choice(brightness))
    ava=ava.resize(size)
    if random.randint(0,1) == 0:
        ava = ava.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(ava,(28,143+random.randint(-3,3)))
    #img.save('/home/list_99/Python/Generate_Fake_ID_card/fake/fake{}.jpg'.format(x))
    img.show()