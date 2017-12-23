# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:30:08 2017

@author: yuguang
"""
from PIL import Image
import numpy as np
#easy pic
#a = np.array(Image.open("/Users/yuguang/Desktop/python3/1.jpg"))
#print(a.shape, a.dtype)
#b = [255, 255, 255] - a
#im = Image.fromarray(b.astype('uint8'))#chong xin sheng cheng tu xiang
#im.save("/Users/yuguang/Desktop/python3/2.jpg")

a = np.array(Image.open("/Users/yuguang/Desktop/python3/pic/yexi.jpg").convert('L'))\
.astype('float')

depth = 10. #jing shen. jia dian shi wei le sheng ming shi fu dian shu
grad = np.gradient(a)# get pic's hui du zhi
grad_x, grad_y = grad
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 +1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2# fu shi jiao du
vec_az = np.pi/4.# fang wei jiao du
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.sin(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z) #gui yi hua
b = b.clip(0, 255)#delete error spots

im = Image.fromarray(b.astype('uint8'))
im.save("/Users/yuguang/Desktop/python3/pic/drawer1.jpg")
