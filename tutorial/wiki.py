
import urllib.request as req

import sys
import io
import xml.etree.cElementTree as ET

import csv
import pprint

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="backslashreplace")

import MeCab
#これ辞書↓
internet_set1 = set(['離散数学','応用数学','ケーブル','2次元配列','メモリ','オペレーティングシステム','ハードウェア','マルチメディア技術','フレーム','LAN','ゲートウェイ','アルゴリズム',
'プロトコル','TCP','IP','インターネット層','トランスポート層','DHCP','DNS','プロトコル','ルーター','イーサネット','イーサーネット','レイヤ2','スイッチング','レイヤ','トランザクション処理','セキュリティ','データベース','ネットワーク','ネットワーク','トポロジ','ケーブル','OSI参照モデル','2進数','16進数','ファイバ','0BASE','コリジョン','クロスサイトスクリプティング','Webサーバ','エンジニアリングシステム','クラスタ分析法',])

internet_set2 = set(['ネットワーク','トポロジ','ケーブル','OSI参照モデル','2進数','16進数','ファイバ','0BASE','コリジョン',])
internet_set3 = set(['イーサネット','イーサーネット','レイヤ2','スイッチング','レイヤ',])
internet_set4 = set(['TCP','IP','インターネット層','トランスポート層','DHCP','DNS','プロトコル','ルーター',])
internet_set = internet_set1
with open(r"C:\Users\hansa\Desktop\mysite\tutorial\jawiki-latest-abstract.xml",'r',encoding="utf-8_sig") as source:

    # get an iterable
    context_set = ET.iterparse(source, events=("start", "end"))
    list =[
        []
    ]

    #print(list)

    for event, root in context_set:
        # do something with elem
        #elem.get('Wikipedia')
        #child = root[0]

        #context_list = list(root)
        #child = context_list[2]
        #print(child.tag,child.text)

        #print(child.tag,child.text)
        #for value,title in root.iter('abstract'),root.iter('title'):
            #print(value.text,title.text)
        ##for result in root.findall('./doc/abstract'):
        #    print(result.text)

        for solt in root.findall('title'):

            #print(solt.text)
            for result in root.findall('abstract'):

                #list.append([solt.text,result.text])
                #print(result.text)

                text = result.text



                mecab = MeCab.Tagger("-Ochasen") #MeCabの取得
                tokens = mecab.parse(text) #分かち書きを行う

                if type(tokens) is str:
                    token = tokens.split("\n")




                    for ele in token:
                        element = ele.split("\t")
                        if element[0] == "EOS":
                            break

                        # 単語の表層を取得
                        surface = element[0]



                        if surface in internet_set:
                            list.append([solt.text,result.text])







                #print(list)

        #for child in root:
        #    print(child.tag,child.text)
        # get rid of the elements after processing
        root.clear()
    def get_unique_list(seq):
        seen = []
        return [x for x in seq if x not in seen and not seen.append(x)]

    list_copy=get_unique_list(list)
    print(list_copy,sep='\n')
    print(len(list))
    print(len(list_copy))

    with open('data1.csv',  'w', newline='',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerows(list_copy)
