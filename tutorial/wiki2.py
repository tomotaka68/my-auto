# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from BeautifulSoup import BeautifulSoup

file_path = '/tutorial/jawiki-latest-abstract.xml'
line_count = 17522478


def file_read_generator():
    """
    XMLをパースして<doc> 〜 </doc>を読み込み返却するgenerator
    :rtype: str
    """
    separate = '</doc>'
    f = open(file_path, 'r')
    count = 0
    txt = ''

    # Fileを1行ずつ読む
    for line in f:
        txt += line
        count += 1
        if separate in line:
            result = txt
            txt = ''
            yield result

        if count % 1000 == 0:
            print '{}/{}'.format(count, line_count)


for body in file_read_generator():
    # parseする
    soup = BeautifulSoup(body)
    print soup.title
    print soup.abstract
    # print soup.findAll('anchor')

print 'finish'
