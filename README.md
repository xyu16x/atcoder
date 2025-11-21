# atcoder
AtCoderのコードをアップロードする

## Pythonインストール〜仮想環境作成〜ライブラリ
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
`acc login`
### テストケースの取得
`acc new abcXXX`  
### vi ~/.bashrc ※>> ~/.bashrcはしない
`alias submit='acc submit -- main.py --language 5055'`  
`alias test='oj t -c "python3 main.py"'`  