#!/bin/bash

# ダウンロード先のディレクトリを指定
DOWNLOAD_DIR="./images"

# 画像ファイルの拡張子を指定
IMAGE_EXT=("jpg" "jpeg" "png" "gif")

# ダウンロード先のディレクトリが存在しない場合は作成する
if [ ! -d "${DOWNLOAD_DIR}" ]; then
  mkdir -p "${DOWNLOAD_DIR}"
fi

# 指定したURLからHTMLを取得し、aタグのhref属性から画像URLを取得する
curl -s "$1" | grep -Eo 'href="[^\"]+"' | cut -d'"' -f2 | while read -r IMAGE_URL
do
  # 画像ファイルであるかを拡張子から判定する
  for EXT in "${IMAGE_EXT[@]}"
  do
    if [[ "${IMAGE_URL}" == *".${EXT}" ]]; then
      # 画像ファイルをダウンロードする
      curl -s -o "${DOWNLOAD_DIR}/$(basename ${IMAGE_URL})" "${IMAGE_URL}"
      break
    fi
  done
done

echo "Download completed!"
