# Update Index.json

このパッケージは、このリポジトリにある `spams/` ディレクトリ内の JSON ファイル一覧をリポジトリ・ルートディレクトリに作成します。

## 実行例

```shellsession
$ cd path/to/Qiita-SPAMS/tools/update-index/
$ python3 Main.py
13239 indexes written in "/index.json".
```

## その他

### コーディング・スタイル（Linter）

- PEP-8 ベース
    - "setup.cfg" の "[pycodestyle]" 設定にある "ignore" を除く制限以外は、基本的に PEP-8 のコーディング・スタイルに準拠しています。
    - "pycodestyle" + "autopep8" でスタイルを整えています。
        - `$ autopep8 --in-place --aggressive --aggressive Main.py`

### 検証環境

- Python v3.6.0 @ macOS v10.13.6
    - pip v18.1
    - pycodestyle v2.4.0
    - autopep8 v1.4.3
