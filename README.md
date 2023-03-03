# bash-warehouse
作成したbash置き場

## img_downloader.sh
指定したURLのリンク先にある画像を一括保存するbash
```
chmod 755 img_downloader.sh
./img_downloader.sh {取得URL}
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
