# myapp/views.py
from django.shortcuts import render
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from polls.models import Todo
from django.urls import reverse
from polls.forms import TodoForm
from flask import json

def index(request):
    logged_in = False
    name = None

    if 'name' in request.POST and 'passwd' in request.POST:
        request.session['name'] = request.POST['name']
        request.session['passwd'] = request.POST['passwd']

    if 'logout' in request.POST:
        request.session.clear()

    if 'name' in request.session and 'passwd' in request.session:
        name = request.session['name']
        logged_in = True

    txt = 'ウィキ（ハワイ語: wiki）とは、不特定多数のユーザーが共同してウェブブラウザから直接コンテンツを編集するウェブサイトである。一般的なウィキにおいては、コンテンツはマークアップ言語によって記述されるか、リッチテキストエディタによって編集される[1]。ウィキはウィキソフトウェア（ウィキエンジンとも呼ばれる）上で動作する。ウィキソフトウェアはコンテンツ管理システムの一種であるが、サイト所有者や特定のユーザーによってコンテンツが作られるわけではないという点において、ブログソフトウェアなど他のコンテンツ管理システムとは異なる。またウィキには固まったサイト構造というものはなく、サイトユーザーのニーズに沿って様々にサイト構造を作り上げることことが可能であり、そうした点でも他のシステムとは異なっている[2]。 '
    txt2 = re.sub(r'(?<=。)', "\t", txt)
    sen = re.split(r'\t', txt2)

    names = ['太郎', '次郎', '三郎', '四郎']
    english_scores = [81, 72, 63, 94]
    math_scores = [61, 70, 85, 80]
    eng_key = '英語'
    math_key = '数学'

    d = {k : {eng_key : v1, math_key : v2} for k,v1,v2 in zip(names, english_scores, math_scores)}
    todo_list = Todo.objects.all()

    appt = [
    ["イルカを漢字で書くとどれ？","海豚","海牛","河豚",1],
    ["クラゲを漢字で書くとどれ？","水浮","水母","水星",2],
    ["カタツムリを漢字で書くとどれ？","禍牛","鍋牛","蝸牛",3],
    ["バッタを漢字で書くとどれ？","飛蝗","飛蟻","飛脚",1],
    ["タツノオトシゴを英語にするとどれ？","sea fish","sea horse","sea dragon",2],
    ["マグロを英語にするとどれ？","funa","suna","tuna",3],
    ["トンボを英語にするとどれ？","fly","dragonfly","butterfly",2],
    ["ヒトデを英語にするとどれ？","starfish","starshell","starmine",1],
    ["恒星の中で最も明るい星は？","デネブ","スピカ","シリウス",3],
    ["惑星の中で最も重たいのはどれ？","太陽","木星","天王星",2]
    ]
    appt = json.dumps(appt)
    params = {
        'todo_list':todo_list,
        'loggedIn':logged_in,
        'name':name,
        'sentence':sen,
        'origin_sentence':txt,
        'appt':appt,
    }
    return render(request, "polls/index.html", params)

def quest2(request):
    return render(request, 'polls/quest2.html')
def quest3(request):
    return render(request, 'polls/quest3.html')
def quest4(request):
    return render(request, 'polls/quest4.html')
def quest(request):
    return render(request, 'polls/quest.html')

def new(request):
    return render(request, 'polls/new.html')

def add(request):
    t1 = Todo()
    t1.todo_id = len(Todo.objects.order_by('-todo_id'))+1
    t1.update_date = timezone.now()
    t = TodoForm(request.POST, instance=t1)
    t.save()
    return HttpResponseRedirect(reverse('index'))

def detail(request, todo_id):
    todo = Todo.objects.get(todo_id=todo_id)
    context = {'todo': todo}
    return render(request, 'polls/new.html', context)

def update(request, todo_id):
    t1 = Todo.objects.get(todo_id=todo_id)
    t = TodoForm(request.POST, instance=t1)
    t.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, todo_id):
    t = Todo.objects.get(todo_id=todo_id)
    t.delete()
    return HttpResponseRedirect(reverse('index'))
