## pyenvインストール
https://zenn.dev/unsoluble_sugar/articles/0f62cccae41ebffe4f2a

```shell
$ brew install pyenv
```

.zshrcに追記
```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

インストール可能なバージョン一覧を確認、インストール
```shell
$ pyenv install --list
$ pyenv install 3.9.4
$ pyenv global 3.9.4
```

## poetryインストール
https://blog.mktia.com/pyenv-and-poetry-on-mac-m1/

```shell
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

https://cocoatomo.github.io/poetry-ja/cli/#init

作成済みのリポジトリの場合
```shell
$ cd ${path} 
$ poetry init
```

新しくリポジトリを作る場合
```
$ poetry new ${path}
```

## IntelliJでpoetryを使う
1. [Poetryのプラグイン](https://plugins.jetbrains.com/plugin/14307-poetry) をインストールする
1. File > Project Structureを開く
   1. Project Settings -> Project を開く
   1. Project SDK -> Add SDK -> Python SDKを開く
   1. Poetry Environment -> Existing Environment Interpreterから利用したいvenvを指定
1. Run > Edit Configrations > +(Add New Configrations)
   1. Pythonを選択
   1. Configration > Script Pathでアプリケーションのエントリポイントを指定

## responder導入
* responderを依存に追加
```shell
$ poetry add responder
```
* poetryの環境下でapp.pyを実行
```shell
$ poetry run python app.py
```
