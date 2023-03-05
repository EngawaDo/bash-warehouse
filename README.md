# bash-warehouse
作成したbash諸々置き場

## img_downloader.sh
指定したURLのリンク先にある画像を一括保存するbash
```
chmod +x img_downloader.sh
./img_downloader.sh [取得URL]
```

## find_similar_images.py
指定した画像と同じイラストを含む画像をフォルダ仕分けする

実行するには以下のライブラリが必要
```
# ライブラリのインストール
pip install opencv-python
pip install numpy
pip install opencv-contrib-python
# スクリプト実行
python find_similar_images.py
```

## img_downloader.py
指定したURLのリンク先にある画像を一括保存するスクリプト
　第１引数：取得URL（指定しない場合は、実行時に入力を求められる）
　第２引数：格納先のサブフォルダ

```
# スクリプト実行
python img_downloader.py
```

## img_downloader_with_file_read.sh

`img_downloader.py`を外部ファイルに定義したURLを読み込んで連続実行するbash
URLの直前にコメントで記述した内容をサブフォルダにする

```
chmod +x img_downloader_with_file_read.sh
./img_downloader_with_file_read.sh [URLを定義したファイル]
```
