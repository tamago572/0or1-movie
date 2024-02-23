import sys
import ffmpeg
import numpy as np
import os
import time
import pygame

args = sys.argv

movie = args[1]
audio = args[2]
# 引数に渡された動画ファイルが存在するか確認
movie_Is_file = os.path.isfile(movie)
if movie_Is_file:
    print(f"{movie} が見つかりました")
else:
    print("存在する動画ファイルを入力してください")
    sys.exit()  # スクリプトを終了


# 引数に渡された音声ファイルが存在するか確認
audio_Is_file = os.path.isfile(audio)
if audio_Is_file:
    print(f"{movie} が見つかりました")
else:
    print("存在する音声ファイルを入力してください")
    sys.exit()  # スクリプトを終了


frame_width = 48
frame_height = 36
color_depth = 3     # グレースケールは1、RGBは3


print("動画を変換します")
out, _ = (
    ffmpeg
    .input(movie)
    .output('pipe:', format='rawvideo', pix_fmt='rgb24', s='48x36', r=15)
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
print("動画を再生します")


def playMovie():
    # subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", movie])
    for frame in frames:
        for row in frame:
            for pixel in row:
                r, g, b = pixel
                if r == 0 and g == 0 and b == 0:
                    print("\033[30m" + "a", end="")
                else:
                    print("\033[38;2;{};{};{}m".format(r, g, b) + "a", end="")
            print("\033[0m")  # Reset ANSI color
        time.sleep(1/15)  # フレームレートに合わせて待機
        print("\033c")


pygame.mixer.init()
pygame.mixer.music.load(audio)
pygame.mixer.music.play(1)

playMovie()
# pygame.mixer.music.stop()

print("動画の再生が完了しました")