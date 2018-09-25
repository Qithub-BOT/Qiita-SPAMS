# Qiita 墓地（Qiita 記事墓場）

このリポジトリは [Qiita](https://qiita.com/) でスパムと認定された記事の Qiita 記事 ID をアーカイブしています。

Qiita 記事のスパム検知のエンジン開発や機械学習用のコーパス作成などにご利用ください。

なお、本リポジトリにはスパム記事の本文データは含まれていません。別途 API を通して取得ください。

## フォーマット

Qiita 記事の投稿日をファイル名とした JSON 配列のプレーン・テキスト。（UTF-8）

### データ形式

- ファイル名：
    `<YYYY_mm_dd>.json` （投稿された日）

- ファイルの内容（JSON配列）：
    １要素１記事
    ```json
    [
        {
            "id_item": "<記事ID>",
            "id_user": "<ユーザID>",
            "url_cache": "<Qithub API のキャッシュURL>",
            "url_raw": "<Qiita API のURL>",
            "date_post": "<投稿日>"
        },
        {
            "id_item": "<記事ID>",
            "id_user": "<ユーザID>",
            "url_cache": "<Qithub API のキャッシュURL>",
            "url_raw": "<Qiita API のURL>",
            "date_post": "<投稿日>"
        },
        {
            //以下同文
        }
    ]
    ```


### ディレクトリ構成

`YYYY` / `mm` の日付を元にしたディレクトリに保存されています。

```
./
├── README.md
├── LICENSE.md
├── 2018
│   ├── 08
│   │   ├── 2018_08_01.json
│   │   ├── 2018_08_02.json
│   │   ├── 2018_08_03.json
│   │   │         ：
│   ├── 09
│   │   ├── 2018_09_01.json
│   │   ├── 2018_09_02.json
│   │   ├── 2018_09_03.json
│   │   │         ：
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

