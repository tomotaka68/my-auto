
import urllib.request as req

import sys
import io
import xml.etree.cElementTree as ET

import csv
import pprint

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="backslashreplace")
import MeCab

text =''

#天気の関連語をまとめたgazetteer
weather_set = set(['晴れ','天気','雨'])

mecab = MeCab.Tagger("-Ochasen") #MeCabの取得
tokens = mecab.parse(text) #分かち書きを行う
token = tokens.split("\n")

#以下、分かち書き後の単語を抽出
for ele in token:
    element = ele.split("\t")
    if element[0] == "EOS":
        break

    # 単語の表層を取得
    surface = element[0]
