# Qiita記事墓

このリポジトリは [Qiita](https://qiita.com/) のスパム記事をアーカイブしています。

Qiita 記事のスパム検知のエンジン開発や機械学習用のコーパス作成などにご利用ください。

## フォーマット

### ファイル名

> `<Qiita の記事 ID>.enc`

### データ形式

> Markdown 形式のテキスト・ファイルを RSA 暗号化したバイナリ。

内容自体がスパムであるため Google 八分を受けないように、Markdown 形式のテキストを Qithub の RSA 秘密鍵で暗号化しています。

Qithub の公開鍵で複合してご利用ください。

### ディレクトリ構成

`YYYY` / `mm` / `dd` の日付を元にしたディレクトリに保存されています。

```
./
├── README.md
├── LICENSE.md
├── 2018
│   ├── 08
│   │   ├── 01
│   │   │   ├── xxxxxxxxxxxxxxxxxxxx.enc
│   │   │   ├── xxxxxxxxxxxxxxxxxxxx.enc
│   │   │   ├── xxxxxxxxxxxxxxxxxxxx.enc
│   │   │   ：
│   │   ├── 02
│   │   │   ├── xxxxxxxxxxxxxxxxxxxx.enc
│   │   │   ├── xxxxxxxxxxxxxxxxxxxx.enc
│   │   │   ├── xxxxxxxxxxxxxxxxxxxx.enc
：   ：   ：   ：
```

## スパムの判断について

新規投稿から**一定期間後にアクセスして投稿が削除されていた場合はスパム**と見なして自動的にアーカイブしています。

- 現在の確認スパン：投稿から１週間後

## 文責

このリポジトリは Qiita/Qiitadon の同人サークル「Qithub」によってメンテナンスされています。

## Opt-out

特定記事の削除など Opt-out を希望される場合は、以下を

- 記事 ID を添えて [Issue](https://github.com/Qithub-BOT/Qithub-ORG/issues) にあげる。
- 該当記事を削除したコミットを Pull Request であげる。
- [サークルメンバー](https://github.com/Qithub-BOT/Qithub-ORG/blob/master/MEMBERS.md)に Mastodon でダイレクトメッセージを送る。

## 免責事項/ライセンス

- このリポジトリのデータは自己責任でご利用ください。
- クリエイティブ・コモンズ 表示ー継承 4.0 国際ライセンス

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>

