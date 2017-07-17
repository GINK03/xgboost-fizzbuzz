XGBoost fizzbuzz
=========

XGBoostのフィズバズです

# やろうと思った動機
DeepLearningならばFizzBuzzの３の倍数と５の倍数と１５の倍数の時に、特定の動作をするというルールを獲得することは容易なのですが、他の機械学習アルゴリズムはどうでしょうか  

XGBoostはその決定木の性質と、勾配ブースティングの学習アルゴリズムからルールを獲得することは難しくないんじゃないかと思いました  

ただ、数値として扱ってしまうと、かなり厄介で、連続する値が大きい小さいなどで内部的に判別するのは容易ではありません  

## 具体的な数値データの取り扱い

数字を文字表現として皆して、各桁の数字を一つの特徴量として扱います  

<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/4949982/28282120-47ffa97e-6b64-11e7-9028-383eb1df820d.png">
</p>
<div align="center"> 図1.　データの取り扱い </div>

## クラスの設定、目的関数の設定
クラスは3の倍数の時のFizz, ５の倍数の時のBuzz, １５の倍数の時のFizzBuzz、　その他の時　の4つのクラスの分類問題にしました  

softmaxではなくて、softprobを用いました  

[ドキュメント](https://github.com/dmlc/xgboost/blob/master/doc/parameter.md)を読むと、各クラスの所属する確率として表現されるようです（クラスの数ぶん、sigmoidが配置されていると、同じ？）  

## 学習データ
０〜９９９９９までの数字の各FizzBuzzを利用します　　

この時、　２割をランダムでテストデータに、８割を学習データに分割します　　

## 各種パラメータ
このようにしました、もっと最適な設定があるかもしれないので、教えていただけると幸いです  

etaが大きいのは、極めてroundが多いので、これ以上小さくするとまともな時間に学習が完了しません　　
```console
booster      = gbtree
objective    = multi:softprob
num_class    = 4
eta          = 1.0
gamma        = 1.0
min_child_weight = 1
max_depth   = 100
subsample   = 0.8
num_round   = 100000
save_period = 1000
colsample_bytree = 0.9
data        = "svm.fmt.train"
eval[test]  = "svm.fmt.test"
#eval_train = 1
test:data   = "svm.fmt.test"
```
