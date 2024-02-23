#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    cv::VideoCapture cap("input.mp4");  // 動画を開く

    if (!cap.isOpened()) {
        std::cerr << "Error opening video" << std::endl;
        return -1;
    }

    cv::Mat frame;
    while (true) {
        cap >> frame;  // フレームを取得

        if (frame.empty()) {
            break;  // フレームがなければループを抜ける
        }

        cv::cvtColor(frame, frame, cv::COLOR_BGR2GRAY);  // グレースケールに変換
        cv::resize(frame, frame, cv::Size(48, 36));  // サイズを変更

        // 各ピクセルの明度を取得し、"0"という文字をその明度で表示
        for (int y = 0; y < frame.rows; ++y) {
            for (int x = 0; x < frame.cols; ++x) {
                int brightness = frame.at<uchar>(y, x);
                // ここでは明度に応じて"0"を表示する代わりに、明度をそのまま出力します
                std::cout << brightness << " ";
            }
            std::cout << std::endl;
        }
    }

    return 0;
}