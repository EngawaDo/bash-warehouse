#!/bin/bash

filename="$1"
echo "filename: $filename"

sub_dir=""
while read line; do
  # コメント行を保存先のサブディレクトリにする
  if [[ $line == \#* ]]; then
    sub_dir=$(echo "$line" | tr -d ' ' | tr -d '#')
    continue
  fi

  # 空行の場合はスキップ
  if [[ -z "$line" ]]; then
    continue
  fi
  echo "--------------------------------"
  echo "$line"
  echo "--------------------------------"
  python img_downloader.py $line $sub_dir
done < "$filename"