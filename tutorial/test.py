import MeCab

text = '今日は晴れかな？'

#天気の関連語をまとめたgazetteer
weather_set = set(['晴れ','天気','雨'])
weather_set2 = ['ラジオ','ゲーム','アニメ']

mecab = MeCab.Tagger("-Ochasen") #MeCabの取得
tokens = mecab.parse(text) #分かち書きを行う
token = tokens.split("\n")

list = list(weather_set2)
#以下、分かち書き後の単語を抽出

for ele in token:
    element = ele.split("\t")
    if element[0] == "EOS":
        break

    # 単語の表層を取得
    surface = element[0]


    if text.find(weather_set2[0])>=0 or text.find(weather_set2[1])>=0 or text.find(weather_set2[2])>=0:
        break
    else:
        if surface in weather_set:
            print(text)
