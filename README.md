## pyenvインストール
https://zenn.dev/unsoluble_sugar/articles/0f62cccae41ebffe4f2a

`$ brew install pyenv`

.zshrcに追記
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

インストール可能なバージョン一覧を確認、インストール
```
$ pyenv install --list
$ pyenv install 3.9.4
$ pyenv global 3.9.4
```

## poetryインストール
https://blog.mktia.com/pyenv-and-poetry-on-mac-m1/

`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

https://cocoatomo.github.io/poetry-ja/cli/#init

作成済みのリポジトリの場合
```
$ cd ${path} 
$ poetry init
```

新しくリポジトリを作る場合
```
$ poetry new ${path}
```

## responder導入
* responderを依存に追加
`$ poetry add responder`
* poetryの環境下でapp.pyを実行
`$ poetry run python app.py`
