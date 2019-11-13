var data4;
getCSVFile('../static/data2.csv');

function getCSVFile(url) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
    createArray(xhr.responseText);
    };

    xhr.open("get", url, true);
    xhr.send(null);

}

function createXMLHttpRequest() {
    var XMLhttpObject = null;
    XMLhttpObject = new XMLHttpRequest();
    return XMLhttpObject;
}

function createArray(csvData) {
    var tempArray = csvData.split("\r\n");
    var csvArray = new Array();
    for(var i = 0; i<tempArray.length;i++){
    csvArray[i] = tempArray[i].split(",");
    }
    data4=csvArray;
}

var n = 2000//問題数

ar = new Array(n);
for (y2=0; y2<ar.length; y2++){
    ar[y2] = new Array(n);
}



function shuffle(array) {
  var n = array.length, t, i;

  while (n) {
    i = Math.floor(Math.random() * n--);
    t = array[n];
    array[n] = array[i];
    array[i] = t;
  }

  return array;
}



function randomSelect(array, num){
    let newArray = [];
    while(newArray.length < num && array.length > 0){
        // 配列からランダムな要素を選ぶ
        const rand = Math.floor(Math.random() * array.length);
        // 選んだ要素を別の配列に登録する
        newArray.push(array[rand]);
        // もとの配列からは削除する
        array.splice(rand, 2);
    }
    return newArray;
}


var ary = new Array();

for (y3=0; y3<ary.length; y3++){
    ary[y3] = new Array();
}

var test_array = [ 1, 2, 3];


for(var st = 0; st <ar.length ; st++){


    ary = data4;
    rand=Math.floor(Math.random() * ary.length);
    var random = ary[rand];
    // もとの配列からは削除する
    ary.splice(rand, 1);
    //random2 =  new Array(ary.length);
    random2 = ary;

    const selected = randomSelect(random2.slice(), 2);

    var randomNumber = Math.floor( Math.random() * (4 - 1) + 1 );



    //ary = ary_origin;
    // 配列arrayからランダムにnum個の要素を取り出す
    //ary.push(ary[rand]);

    t = shuffle(test_array);

    ar[st][0] = random[0];
    ar[st][t[0]] = random[1];
    ar[st][t[1]] = selected[0][1];
    ar[st][t[2]] = selected[1][1];
    ar[st][4] = t[0];
}

function getCol(matrix, col){
   var column = [];
   for(var i=0; i<matrix.length; i++){
      column.push(matrix[i][col]);
   }
   return column;
}

var array = [
    ['光ファイバー','光ファイバの説明'],
    ['OSI参照モデル','OSI参照モデルの説明'],
    ['インターネット層','インターネット層の説明'],
    ['アプリケーション層','アプリケーション層の説明'],
    ['ルーター','ルーターの説明']
]; //..your 3x20 array
var a1 = getCol(array, 0); //Get first column

var qa = ar;

//count = 0; //問題番号
q_sel = 3; //選択肢の数

setReady();

//最初の問題
//quiz();

//初期設定
function setReady() {
	count = 0; //問題番号
	ansers = new Array(); //解答記録

	//最初の問題
	quiz();
}

//問題表示
function quiz() {
	var s, n;
	//問題
	document.getElementById("text_q").innerHTML = (count + 1) + "問目：" + qa[count][0]+"の説明で正しいのを選べ";
	//選択肢
	s = "";
	for (n=1;n<=q_sel;n++) {
		s += "【<a href='javascript:anser(" + n + ")'>" + n + "：" + qa[count][n] + "</a>】"+"<br>"+"<br>";
	}
	document.getElementById("text_s").innerHTML = s;
}

//解答表示
function anser(num) {
	var s;
	s = (count + 1) + "問目：";
	//答え合わせ
	if (num == qa[count][q_sel + 1]) {
		//正解
		s += "○" + qa[count][num];
	} else {
		s += "×" + qa[count][num];
	}
	document.getElementById("text_a").innerHTML = s;
    //次の問題を表示
    count++;
    if (count < qa.length) {
        quiz();
    }
    else {
    //終了
        document.getElementById("text_q").innerHTML = "";
        document.getElementById("text_s").innerHTML = "";
    }
}

//解答表示
function anser(num) {
	var s;
	s = (count + 1) + "問目：";
	//答え合わせ
	if (num == qa[count][q_sel + 1]) {
		//正解
		s += "○" + qa[count][num];
		ansers[count] = "○";
	} else {
		s += "×" + qa[count][num];
		ansers[count] = "×";
	}
	document.getElementById("text_a").innerHTML = s;

	//次の問題を表示
	count++;
	if (count < qa.length) {
		quiz();
	} else {
        //終了
		s = "<table border='2'><caption>成績発表</caption>";
		//1行目
		s += "<tr><th>問題</th>";
		for (n=0;n<qa.length;n++) {
			s += "<th>" + (n+1) + "</th>";
		}
		s += "</tr>";
		//2行目
		s += "<tr><th>成績</th>";
		for (n=0;n<qa.length;n++) {
			s += "<td>" + ansers[n] + "</td>";
		}
		s += "</tr>";
		s += "</table>";
		document.getElementById("text_q").innerHTML = "";
        //次の選択肢
		s = "【<a href='javascript:history.back()'>前のページに戻る</a>】";
		s += "【<a href='javascript:setReady()'>同じ問題を最初から</a>】";
		s += "【<a href=''>次の問題に進む</a>】";
		document.getElementById("text_s").innerHTML = s;
	}
}


var qaa= data4;



var length = 20;
var ar_ox = new Array(1);
for(let y = 0; y < qaa.length; y++) {
  ar_ox[y] = new Array(1).fill(0);
}
var ans_ox = new Array(1);
for(let y = 0; y < qaa.length; y++) {
  ans_ox[y] = new Array(1).fill(0);
}


for(var z = 0; z<ar_ox.length-1 ; z++){

    var aryq = qaa;
    randq=Math.floor(Math.random() * aryq.length);
    var randomq = aryq[randq];

    aryq.splice(randq, 1);

    randomq2 = aryq;

    var a_ox= randomq[0]

    const selectedq = randomSelect(randomq2.slice(), 1);

    rand2_1 =  Math.floor(Math.random()*2 + 1) ;
    if(rand2_1==2){
        var b_ox = selectedq[0][1];
        ans_ox[z][0] = selectedq[0][0];
        ans_ox[z][1] = selectedq[0][1]
        var c_ox = a_ox + 'とは' + b_ox;
        ar_ox[z][0] = c_ox;
        ar_ox[z][1] = 2 ;
    }
    else if(rand2_1==1){
        var d_ox =  selectedq[0][0] + 'とは' +selectedq[0][1];
        ar_ox[z][0] = d_ox;
        ar_ox[z][1] = 1;
    }

}


var qa_ox = [
  ['「テトリス（ゲーム）」を開発したのは、日本人だ。', 2],
  ['生きている間は、有名な人であっても広辞苑に載ることはない。 ', 1],
  ['現在、2000円札は製造を停止している。', 1],
  ['パトカーは、取り締まっている最中であれば、どこでも駐車違反になることはない。', 2],
  ['昆虫の中には、口で呼吸する昆虫もいる。 ', 2],
  ['一般的に体の水分は、男性より女性のほうが多く含まれている。', 2],
  ['たとえ１ｃｍの高さであっても、地震によって起こるのは全て「津波」である。', 1],
  ['1円玉の直径は、ちょうど１ｃｍになっている。', 2],
  ['塩はカロリー０である。 ', 1],
  ['「小中学校は、PTAを作らなければならない」と法律で定められている。', 2]
];

var count_ox = 0;
var correctNum_ox = 0;

window.onload = function() {
  // 最初の問題を表示
  var question_ox = document.getElementById('question_ox');
  question_ox.innerHTML = (count_ox + 1) + '問目：' + ar_ox[count_ox][0]+ '〇か×か？';
};

// クリック時の答え判定
function hantei(btnNo) {
      if (ar_ox[count_ox][1] == btnNo) {
        correctNum_ox++;
      }

      if (count_ox == ar_ox.length-1) {
        alert('あなたの正解数は' + correctNum_ox + '問です！');
      }

      // 次の問題表示
      count_ox++;
      var question_ox = document.getElementById('question_ox');
      question_ox.innerHTML = (count_ox + 1) + '問目：' + ar_ox[count_ox][0]+ '〇か×か？';
      if(btnNo==1){
          if(ar_ox[count_ox-1][1]==2){
              s = '2不正解2!' + ar_ox[count_ox-1][0] + 'は不正解.' +'<br><br>'+ '正解は'+ans_ox[count_ox-1][0]+'とは'+ ans_ox[count_ox-1][1];
          }
          else if(ar_ox[count_ox-1][1]==1){
              s ='1正解1!' + ar_ox[count_ox-1][0] + 'は正解';
          }
      }
      if(btnNo==2){
        if(ar_ox[count_ox-1][1]==2){
            s = '4正解4!' + ar_ox[count_ox-1][0] + 'は不正解.' +'<br><br>'+ '正解は'+ans_ox[count_ox-1][0]+'とは'+ ans_ox[count_ox-1][1];
        }
        else if(ar_ox[count_ox-1][1]==1){
            s ='3不正解3!' + ar_ox[count_ox-1][0] + 'は正解';
        }
        }
      document.getElementById("text_ans").innerHTML = s;
}


var quizzes = data4;
var quiz2;

init();
function init(){
    var ra = Math.floor(Math.random() * quizzes.length);
    quiz2 = quizzes[ra];

    //問題用のフォームに表示する

    document.getElementById("questionana").innerHTML = quiz2[1];

}

function doAnswer(){
    //回答用のフォームに入力した値を取得
    var answerForm = document.querySelector("#answerana");
    var answer = answerForm.value;

    //回答用フォームで入力した内容を削除する
    answerForm.value = "";

    //入力した内容が正しいか調べる
    if (answer == quiz2[0]) {
        //入力した内容が正解の時
        right();
    } else {
        //入力した内容が不正解の時
        wrong();
    }
}

//正解の時に実行する関数
function right(){
    alert("正解です");

    init();
}

//不正解の時に実行する関数
function wrong(){
    alert("不正解です");

}
