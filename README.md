# atcoder
AtCoderのコードをアップロードする

## Pythonインストール〜仮想環境作成
`sudo apt install python3-pip`  
`sudo apt install python3.12-venv`  
`python3 -m venv .venv`  
 
#### atcoder-cli インストール
`npm install -g --prefix ~/.local atcoder-cli`
`acc --version`
#### online-judge-toolsインストール
`pip3 install online-judge-tools`
`oj --version` 

## templateの設定
### acc の設定ディレクトリに移動
`cd "$(acc config-dir)"`  
### Python用のテンプレートディレクトリを作成 (ディレクトリ名は任意だが、ここでは 'python'とする)
`mkdir python`
### accのデフォルトテンプレートの設定
`acc config default-template python`  

## venvに入る
`source .venv/bin/activate`

## atcoder
### ログイン
`oj login https://atcoder.jp/`
### テストケースの取得
`acc new abcXXX`  
### ローカルテスト
`oj t -c "python3 main.py"`
### 提出
`acc submit -s -- -l 5009`

## 別バージョン
### テストケース取得
``