import cv2
import numpy as np
import os
import shutil

# 画像Aの読み込み
img_a = cv2.imread("ref_image.png")

# 画像Aの特徴量を検出
sift = cv2.xfeatures2d.SIFT_create()
kp_a, des_a = sift.detectAndCompute(img_a, None)

# 処理対象の画像フォルダ
folder_path = "target_images"

# 処理対象フォルダ内の画像ファイルのリストを取得
files = os.listdir(folder_path)

# 移動先のフォルダ
destination_folder = "similar_images"

# 処理対象フォルダ内の各画像との比較
for filename in files:
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 画像ファイルの読み込み
        img_b = cv2.imread(os.path.join(folder_path, filename))
        
        # 画像Bの右下部分の切り取り
        height, width, _ = img_b.shape
        roi_b = img_b[height - img_a.shape[0]: height, width - img_a.shape[1]: width]

        # x_start = width - 150
        # y_start = height - 150
        # roi_b = img_b[y_start:height, x_start:width]

        # 画像Bの特徴量を検出
        kp_b, des_b = sift.detectAndCompute(roi_b, None)
        
        # 画像Aと画像Bの特徴量をマッチング
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des_a, des_b, k=2)
        
        # マッチングされた特徴点のリストを取得
        good = []
        for m, n in matches:
            # 値を小さくすることで許容値を下げる
            if m.distance < 0.50 * n.distance:
                good.append([m])
        
        # マッチングされた特徴点の数が一定以上の場合には移動
        if len(good) > 10:
            shutil.move(os.path.join(folder_path, filename), destination_folder)
            print(f"Moved {filename} to {destination_folder}")
