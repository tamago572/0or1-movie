import sys
import ffmpeg
import numpy as np
import os
import time

args = sys.argv

movie = args[1]
# 引数に渡された動画ファイルが存在するか確認
is_file = os.path.isfile(movie)
if is_file:
    print(f"{movie} が見つかりました")
else:
    print("存在する動画ファイルを入力してください")
    sys.exit()  # スクリプトを終了


frame_width = 48
frame_height = 36
color_depth = 1     # グレースケールは1、RGBは3


print("動画を変換します")
out, _ = (
    ffmpeg
    .input(movie)
    .output('pipe:', format='rawvideo', pix_fmt='gray', s='48x36', r=15)
    .run(capture_stdout=True)
)
print("動画を変換しました")
print("配列に格納しています")
frames = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1, frame_height, frame_width, color_depth])
)
print("配列に格納しました")

for frame in frames:
    # フレーム内の各ピクセルの明度を取得し、"0"という文字を黒色で表示します
    for y in range(frame_height):
        for x in range(frame_width):
            brightness = frame[y, x]
            # ANSIエスケープコードを使用して文字色を設定します
            # 38;2;R;G;Bmは前景色をRGB値で設定します
            print(f"\033[38;2;{brightness};{brightness};{brightness}m0", end="")
        print("\033[0m")  # 色設定をリセットして改行
