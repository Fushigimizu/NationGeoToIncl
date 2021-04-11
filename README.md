# WebMultiPages
複数ページに分割されているウェブサイトの記事を1つのテキストにして保存します。現在は ナショナルジオグラフィック日本版にのみ対応しています。

[Anki で Incrimental Reading をする](https://ankiweb.net/shared/info/935264945)ために作りましたが、Incrimental Reading 自体を全然していないので更新できていません。

# 用意するもの(Windows の場合)
- chromedriver.exe(スクリプトと同じディレクトリに置く)
- 日経BP のアカウント

# 使い方
- url.txt に保存したい記事の1ページ目の URL を、1行につき1つずつ書いておく
- natiogeo.py 内にある<メールアドレス><パスワード>を、日経BP に登録したものに置き換える
- main.py を実行する
- 終了すると import.txt に各記事が1行に1つずつ出力されているので、Anki で読み込む
- インポート時は「タブで区切ったフィールド」を選択し、「フィールドに HTML を使う」にチェックを入れること
