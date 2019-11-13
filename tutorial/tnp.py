        for result in root.findall('title'):
            if result.text == "Wikipedia: インターネット":
                print(result.text)

        for result in root.findall('title'):
            print(result.text)
            for result in root.findall('abstract'):
                print(result.text)
        if solt.text == "Wikipedia: 言語":
            print(list)
            break

import MeCab

text = '今日は晴れかな？'

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

    if surface in weather_set:
        print(surface)


['離散数学','応用数学','ケーブル','2次元配列','メモリ','オペレーティングシステム','ハードウェア','マルチメディア技術','フレーム','LAN','ゲートウェイ','アルゴリズム',
'プロトコル','トランザクション処理','セキュリティ','データベース','ネットワーク','クロスサイトスクリプティング','Webサーバ','エンジニアリングシステム','クラスタ分析法',]

list_a = []
list_b = []
kaede=np.array(list_a)
toneko=np.array(list_b)

c = np.concatenate((kaede.T,toneko), axis = 0)
print(c)



unko=l_y.replace('Wikipedia: ', '').replace(' ','')
