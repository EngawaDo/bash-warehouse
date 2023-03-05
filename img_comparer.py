import os
import cv2
import shutil
import sys

if len(sys.argv) < 2:
    print("引数が足りません。")
    print("使用方法: python img_comparer.py [検索対象] [比較画像]")
    sys.exit(1)

target_folder = sys.argv[1]
compare_image = sys.argv[2]
moved_images = "moved_images"

# 特徴量の計算に使用するSIFTを初期化
sift = cv2.xfeatures2d.SIFT_create()

# 比較対象の画像を読み込む
img1 = cv2.imread(compare_image)
# 特徴量を計算する
kp1, des1 = sift.detectAndCompute(img1, None)

# 移動先のフォルダを作成
if not os.path.exists(moved_images):
    os.mkdir(moved_images)

# 指定したフォルダを再帰的に探索し、画像を移動
for root, dirs, files in os.walk(target_folder):
    for file in files:
        # ファイルが画像ファイルでない場合はスキップ
        if not file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            continue
        # 画像ファイルのパスを取得
        img_path = os.path.join(root, file)
        # 画像を読み込む
        print(img_path)
        img2 = cv2.imread(img_path)
        # 特徴量を計算する
        kp2, des2 = sift.detectAndCompute(img2, None)
        # 画像間のマッチングを行う
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        # マッチング結果をフィルタリングする
        good_matches = []
        for m, n in matches:
            if m.distance < 0.25 * n.distance:
                good_matches.append(m)
        # マッチング数が一定以上の場合は画像を移動する
        if len(good_matches) >= 10:
            moved_path = os.path.join(moved_images, file)
            shutil.move(img_path, moved_path)
