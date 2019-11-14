
import urllib.request as req

import sys
import io
import xml.etree.cElementTree as ET

import csv
import pprint
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="backslashreplace")

import MeCab
import sakujo
kaedetoneko=[]

with open('data1.csv',encoding='UTF-8') as f:
    reader = csv.reader(f)
    l = [row for row in reader]




    ln = len(l)
    print(l[1][1])
    print(ln)

    for a in range(ln-1):
        s=a+1
        l_y=l[s][0]

        #print(l_y)
        unko=l_y.replace('Wikipedia: ', '')
        print(unko)





        l_r=l[s][1]
        l_y=str(l[s][0])
        l_r=sakujo.delete_brackets(l_r)
        #print(l_y)
        tinko=l_r.replace(unko, '□')
        tinko=tinko.replace('□は、', '')
        tinko=tinko.replace('□とは、', '')
        tinko=tinko.replace('□とは', '')
        tinko=tinko.replace('とは', '')
        tinko=tinko.replace('□は', '')
        tinko=tinko.replace('□または', '')
        tinko=tinko.replace('『□』は、', '')
        tinko=tinko.replace('□,', '')
        tinko=tinko.replace('□　,', '')
        tinko=tinko.replace('□、', '')
        tinko=tinko.replace('□　、', '')
        tinko=tinko.replace('□。', '')
        tinko=tinko.replace('□  ', '')
        


        kaedetoneko.append([unko,tinko])
    #print(l)

    print(type('a'))
    print(kaedetoneko)


    with open('data2.csv',  'w', newline='',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerows(kaedetoneko)
