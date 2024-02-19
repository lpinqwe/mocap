#include <iostream>
#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
    cout << "OpenCV version: " << CV_VERSION << endl;

    Mat mat = imread("demos/hello-cv-cpp/lena.jpg");
    imshow("Image", mat);
    waitKey();
    destroyAllWindows();

    return 0;
}
