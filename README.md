# 和同開珎
和同開珎の名で知られる[漢字パズル](https://ja.wikipedia.org/wiki/%E5%92%8C%E5%90%8C%E9%96%8B%E7%8F%8E_(%E3%83%91%E3%82%BA%E3%83%AB))を自動的に生成するプログラムです. また, 問題を与えて解かせることも出来ます.

## 必要環境
Python3

## インストール
例えば以下のようにして, このリポジトリの内容をディレクトリに展開し, そのディレクトリに移動して下さい.
```
git clone https://github.com/knakan213/wado-puzzle.git
cd wado-puzzle
```

## 使い方
> Linux or Mac
```
python3 wado-puzzle.py
```
> Windows
```
python wado-puzzle.py
```
とすると, 和同開珎パズルがランダムに生成され出題されます.
問題だけ出力され入力待ちになるので, Enterキーを押して解答を表示します.
続いて次の問題が出題されます. 永遠に繰り返すので Ctrl-C で終了して下さい.

また, 問題を与えて解かせるには上左下右の漢字を引数として与えます. 例えば
```
   妥
割[  ]分
   方
```
という問題であれば
> Linux or Mac
```
python3 wado-puzzle.py 妥割方分
```
> Windows
```
python wado-puzzle.py 妥割方分
```
とします.

## ライセンス
- [armooo/graded-idioms-ja](https://github.com/marmooo/graded-idioms-ja)にて[Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)で公開されている二字熟語のリスト(all.cvs)を使用しています.
- このリポジトリのその他の内容はMITライセンスで公開されています.
