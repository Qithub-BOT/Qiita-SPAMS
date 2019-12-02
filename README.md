# Qiita 墓地（Qiita 記事墓場）

このリポジトリは **[Qiita](https://qiita.com/) のスパム記事の情報を 10 万件以上アーカイブしています**。Qiita のスパム記事を検知するエンジン開発や機械学習用のコーパス作成などにご利用ください。

- おすすめの記事: [Qiitaのスパム狩りをしたらAutoMLに仕事を奪われた件](https://qiita.com/dcm_chida/items/0b687fe42b932e090a36) @ Qiita

## 注意（データはエイリアスです）

**このリポジトリ自体にはスパム記事の本文データは含まれていません**。スパム記事の本文を取得するのに必要な情報を JSON ファイルで提供しています。

各々の JSON ファイルに記載された API の URL（"`url_cache`" や "`url_raw`" キー）を通して取得ください。いずれの API も JSON 形式で取得できます。

- `url_cache` キー: Qiita 記事情報のキャッシュサーバーの URL です。本家 Qiita のサーバー負荷をあげないために設けた[キャッシュ・サーバー](https://github.com/Qithub-BOT/Qithub-ORG/tree/master/api/v1/qiita-cache)です。なるべくこちらをご利用ください。
- `url_raw` キー: 本家 Qiita の API の URL です。キャッシュサーバーが落ちている場合に利用ください。

## スパムの判断について

新規投稿から**一定期間後にアクセスして、投稿とユーザーが削除されていた場合をスパム記事と判断**しています。そのため、引越しをした場合もスパムとして判断される可能性があります。（Opt-Out はページ下部をご覧ください）

- リポジトリ更新頻度：現在、サーバー OS 入れ替えのため、不定期で更新しています。

## フォーマット

- Qiita 記事の記事 ID をファイル名とした JSON 配列のプレーン・テキスト。（UTF-8）
  - `spams` ディレクトリに設置されています。このとき記事 ID の最初の文字をディレクトリ名とした下に設置されています。

### データ形式

- ファイル名：
    `<Qiita記事ID>.json` （Qiita の記事 ID がファイル名）

- ファイルの内容（JSON配列）：
    １ファイル１記事
    ```json
    {
        "id_item": "<記事ID>",
        "id_user": "<ユーザID>",
        "url_cache": "<Qithub API のキャッシュ URL>",
        "url_raw": "<Qiita API のURL>",
        "date_post": "<投稿日>"
    }
    ```

### サンプル

Qiita 記事ID `affde3d2cca6ecec0c87` の場合、ファイル名は `affde3d2cca6ecec0c87.json` になり、設置先は `spams/a/affde3d2cca6ecec0c87.json` になります。


- ファイルの内容は以下の通り:

    ```json
    {
        "id_item": "affde3d2cca6ecec0c87",
        "id_user": "wedoseday",
        "url_cache": "https://qithub.gq/api/v1/qiita-cache/?id=affde3d2cca6ecec0c87",
        "url_raw": "https://qiita.com/api/v2/items/affde3d2cca6ecec0c87",
        "date_post": "2018-05-22T05:08:25+09:00"
    }
    ```

- キャッシュの URL 例: [https://qithub.gq/api/v1/qiita-cache/?id=affde3d2cca6ecec0c87](https://qithub.gq/api/v1/qiita-cache/?id=affde3d2cca6ecec0c87)
- キャッシュ（スパム記事の本文データ）の取得例：

    ```bash
    curl -o spam.json https://qithub.gq/api/v1/qiita-cache/?id=affde3d2cca6ecec0c87
    ```

### ディレクトリ構成

`/spams` ディレクトリ下に、Qiita 記事 ID の頭文字をディレクトリ名とした階層内に各々保存されています。

```text
./spams/
├── README.md
├── LICENSE.md
├── a/
│   ├── a00a765cb4fe79e16c35.json
│   ├── a01077d83a4c3bb5c7dd.json
│   ：
：
└── f/
    ├── f002a7ed1ce1aad5c474.json
：   ：   ：         ：
```

## Issue

本リポジトリに関する Issue は下記リポジトリで取りまとめています。

https://github.com/Qithub-BOT/Qithub-ORG/issues

## Opt-out

特定記事の削除など Opt-out を希望される場合は、以下のいずれかでご連絡ください。

- 該当記事の記事 ID を .gitignore に追記したコミットを Pull Request であげる。
- 記事 ID を添えて [Issue](https://github.com/Qithub-BOT/Qithub-ORG/issues) にあげる。
- [サークルメンバー](https://github.com/Qithub-BOT/Qithub-ORG/blob/master/MEMBERS.md)に Mastodon でダイレクトメッセージを送る。

## 文責

このリポジトリは Qiita/Qiitadon の同人サークル「[Qithub](https://github.com/Qithub-BOT/Qithub-ORG)」によってメンテナンスされています。

## 免責事項/ライセンス

- このリポジトリのデータは自己責任でご利用ください。
- クリエイティブ・コモンズ 表示ー継承 4.0 国際ライセンス

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
