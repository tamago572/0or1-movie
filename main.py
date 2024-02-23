import sys
import ffmpeg
import numpy as np
import os

args = sys.argv

movie = args[1]
# 引数に渡された動画ファイルが存在するか確認
is_file = os.path.isfile(movie)
if is_file:
    print(f"{movie} が見つかりました")
else:
    print("存在する動画ファイルを入力してください")
    sys.exit()  # スクリプトを終了

out, _ = (
    ffmpeg
    .input(movie)
    .output('pipe:', format='rawvideo', pix_fmt='gray', s='48x36', r=30)
    .run(capture_stdout=True)
)

arr = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1, 36, 48])
)
