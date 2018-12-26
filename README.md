# Qiita 墓地（Qiita 記事墓場）

このリポジトリは [Qiita](https://qiita.com/) でスパムと認定された記事の Qiita 記事 ID をアーカイブしています。

Qiita 記事のスパム検知のエンジン開発や機械学習用のコーパス作成などにご利用ください。

なお、**本リポジトリにはスパム記事の本文データは含まれていません**。`/spams` ディレクトリにある各JSON ファイルの "`url_cache`" や "`url_raw`" キーに記載された URL 先の API を通して別途取得ください。いずれの API も JSON 形式で取得できます。

また、`url_cache` キーの URL は、本家 Qiita のサーバー負荷をあげないために[設けたキャッシュ・サーバー](https://github.com/Qithub-BOT/Qithub-ORG/tree/master/api/v1/qiita-cache)ですので、なるべくそちらをご利用ください。（キャッシュ・サーバーが落ちてたら本家をご利用ください）

## フォーマット

Qiita 記事の投稿日をファイル名とした JSON 配列のプレーン・テキスト。（UTF-8）

### データ形式

- ファイル名：
    `<Qiita記事ID>.json` （投稿された日）

- ファイルの内容（JSON配列）：
    １要素１記事
    ```json
    {
        "id_item": "<記事ID>",
        "id_user": "<ユーザID>",
        "url_cache": "<Qithub API のキャッシュURL>",
        "url_raw": "<Qiita API のURL>",
        "date_post": "<投稿日>"
    }
    ```
### サンプル

Qiita 記事ID `affde3d2cca6ecec0c87` の場合は、`a/affde3d2cca6ecec0c87.json` ファイルになり内容は以下の通りになります。

```json
{
    "id_item": "affde3d2cca6ecec0c87",
    "id_user": "wedoseday",
    "url_cache": "https://qithub.gq/api/v1/qiita-cache/?id=affde3d2cca6ecec0c87",
    "url_raw": "https://qiita.com/api/v2/items/affde3d2cca6ecec0c87",
    "date_post": "2018-05-22T05:08:25+09:00"
}
```

### ディレクトリ構成

`/spams` ディレクトリ下に、Qiita 記事 ID の頭文字をディレクトリ名とした階層内に各々保存されています。

```
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

## スパムの判断について

新規投稿から**一定期間後にアクセスして投稿とユーザーが削除されていた場合はスパム記事**と見なして自動的にアーカイブしています。

- 現在の確認間隔：投稿から１週間後

## Issue

本リポジトリに関する Issue は下記リポジトリで取りまとめています。

https://github.com/Qithub-BOT/Qithub-ORG/issues

## Opt-out

特定記事の削除など Opt-out を希望される場合は、以下のいずれかでご連絡ください。

- 記事 ID を添えて [Issue](https://github.com/Qithub-BOT/Qithub-ORG/issues) にあげる。
- 該当記事を削除したコミットを Pull Request であげる。
- [サークルメンバー](https://github.com/Qithub-BOT/Qithub-ORG/blob/master/MEMBERS.md)に Mastodon でダイレクトメッセージを送る。

## 文責

このリポジトリは Qiita/Qiitadon の同人サークル「Qithub」によってメンテナンスされています。

## 免責事項/ライセンス

- このリポジトリのデータは自己責任でご利用ください。
- クリエイティブ・コモンズ 表示ー継承 4.0 国際ライセンス

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>

