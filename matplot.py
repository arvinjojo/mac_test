# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:32:59 2017

@author: yuguang
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  
import numpy as np



##plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
#plt.subplot(3, 2, 4)
#plt.ylabel("grade")
#plt.axis([-1, 10, 0, 6]) #asix range
#plt.savefig('test', dpi=600) #png
#plt.show()

##energy curves
#def f(t):
#    return np.exp(-t)*np.cos(2*np.pi*t)
#    
#a = np.arange(0.0, 5.0, 0.02)
#
#plt.subplot(211)
#plt.plot(a, f(a))
#
#plt.subplot(2, 1, 2)
#plt.plot(a, np.cos(2*np.pi*a), 'r--')
#plt.show()

##show different line shapes
#a = np.arange(10)
#plt.plot(a, a*1.5, 'go-', a, a*2.5, ':', a, a*3.5, 'rx')
#plt.show()

#plt.plot([3, 1, 4, 5, 2])
#plt.ylabel("纵轴（值）")
#plt.savefig('test1', dpi=600)
#plt.show



# #xian shi zhong wen 1
#def getChineseFont():  
#    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')  
#plt.plot([3, 1, 4, 5, 2])
#plt.ylabel("纵轴（值）", fontproperties=getChineseFont())
#plt.show()  

##xian shi zhong wen 2 shrink biao shi jian tou jv li wen ben jv li
#def getChineseFont():  
#    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')  
#a = np.arange(0.0, 5.0, 0.02)
#plt.plot(a, np.cos(2*np.pi*a), 'r--')
#
#plt.xlabel('横轴', fontproperties=getChineseFont(), fontsize=15, color='green')
#plt.ylabel('纵轴', fontproperties=getChineseFont(), fontsize=15)
#plt.title('正弦波 $y=cos(2\pi x$)', fontproperties=getChineseFont(), fontsize=25)
#plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5),\
#arrowprops=dict(facecolor='black', shrink=0.1, width=2))
#
#plt.axis([-1, 6, -2, 2])
#plt.grid(True)
#plt.show()

##bing tu
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
#sizes = [15, 30, 45, 10]
#explode = (0, 0.1, 0, 0)
#
#plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',\
#shadow=False, startangle=90)
#plt.axis('equal')
#plt.show()

##zhi fang tu
#np.random.seed(0)# mei ci sheng cheng de sui ji shu xiang tong
#mu, sigma = 100, 20
#a = np.random.normal(mu, sigma, size=100)
#
#plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='b', alpha=0.75)
#plt.title('Histogram')
#plt.show()

##ji zuo biao
#N = 10
#theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
#radii =10*np.random.rand(N)
#width = np.pi / 4*np.random.rand(N)
#
#ax = plt.subplot(111, projection='polar')
#bars = ax.bar(theta, radii, width=width, bottom=0.0)
#
#for r, bar in zip(radii, bars):
#    bar.set_facecolor(plt.cm.viridis(r/10.))
#    bar.set_alpha = (0.5)
#
#plt.show()