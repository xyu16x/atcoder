# atcoder
AtCoderのコードをアップロードする

## 環境構築にうったコマンド
 sudo apt install python3-pip
 sudo apt install python3.12-venv
 python3 -m venv .venv
 npm install -g --prefix ~/.local atcoder-cli
 vi ~/.bashrc
 # .bashrc に追加した行を再確認
 echo 'export PATH="$HOME/.local/bin:$PATH"'

## templateの設定
# acc の設定ディレクトリに移動
cd "$(acc config-dir)"
# Python用のテンプレートディレクトリを作成 (ディレクトリ名は任意だが、ここでは 'python'とする)
mkdir python
# accのデフォルトテンプレートの設定
acc config default-template python

## venvに入る
source .venv/bin/activate


## atcoder
### ログイン
oj login https://atcoder.jp/
### テストケースの取得
mkdir abc
cd ./abc
oj d https://atcoder.jp/contests/abc
cp ../../../library/template.py main.py
### ローカルテスト
oj t -c "python3 main.py"
### 提出
oj s https://atcoder.jp/contests/abcXXX/tasks/abcXXX_a A.py