load("@rules_foreign_cc//foreign_cc:defs.bzl", "cmake")

filegroup(
    name = "all_srcs",
    srcs = glob(["**"]),
)

cmake(
    name = "opencv",
    lib_source = ":all_srcs",
    generate_args = [
        "-GNinja",
        "-DBUILD_LIST=core,highgui,imgcodecs,imgproc,videoio,video,calib3d,dnn,features2d,flann,ml,objdetect,photo,stitching",
    ],
    out_shared_libs = select({
        "@platforms//os:macos": [
            "libopencv_core.dylib",
            "libopencv_core.4.9.0.dylib",
            "libopencv_core.409.dylib",

            "libopencv_highgui.dylib",
            "libopencv_highgui.4.9.0.dylib",
            "libopencv_highgui.409.dylib",

            "libopencv_imgcodecs.dylib",
            "libopencv_imgcodecs.4.9.0.dylib",
            "libopencv_imgcodecs.409.dylib",

            "libopencv_imgproc.dylib",
            "libopencv_imgproc.4.9.0.dylib",
            "libopencv_imgproc.409.dylib",

            "libopencv_videoio.dylib",
            "libopencv_videoio.4.9.0.dylib",
            "libopencv_videoio.409.dylib",

            "libopencv_video.dylib",
            "libopencv_video.4.9.0.dylib",
            "libopencv_video.409.dylib",

            "libopencv_calib3d.dylib",
            "libopencv_calib3d.4.9.0.dylib",
            "libopencv_calib3d.409.dylib",

            "libopencv_dnn.dylib",
            "libopencv_dnn.4.9.0.dylib",
            "libopencv_dnn.409.dylib",

            "libopencv_features2d.dylib",
            "libopencv_features2d.4.9.0.dylib",
            "libopencv_features2d.409.dylib",

            "libopencv_flann.dylib",
            "libopencv_flann.4.9.0.dylib",
            "libopencv_flann.409.dylib",

            "libopencv_ml.dylib",
            "libopencv_ml.4.9.0.dylib",
            "libopencv_ml.409.dylib",

            "libopencv_objdetect.dylib",
            "libopencv_objdetect.4.9.0.dylib",
            "libopencv_objdetect.409.dylib",

            "libopencv_photo.dylib",
            "libopencv_photo.4.9.0.dylib",
            "libopencv_photo.409.dylib",

            "libopencv_stitching.dylib",
            "libopencv_stitching.4.9.0.dylib",
            "libopencv_stitching.409.dylib",
        ],
        "@platforms//os:linux": [
            "libopencv_core.so",
            "libopencv_core.so.4.9.0",
            "libopencv_core.so.409",

            "libopencv_highgui.so",
            "libopencv_highgui.so.4.9.0",
            "libopencv_highgui.so.409",

            "libopencv_imgcodecs.so",
            "libopencv_imgcodecs.so.4.9.0",
            "libopencv_imgcodecs.so.409",

            "libopencv_imgproc.so",
            "libopencv_imgproc.so.4.9.0",
            "libopencv_imgproc.so.409",

            "libopencv_videoio.so",
            "libopencv_videoio.so.4.9.0",
            "libopencv_videoio.so.409",

            "libopencv_video.so",
            "libopencv_video.so.4.9.0",
            "libopencv_video.so.409",

            "libopencv_calib3d.so",
            "libopencv_calib3d.so.4.9.0",
            "libopencv_calib3d.so.409",

            "libopencv_dnn.so",
            "libopencv_dnn.so.4.9.0",
            "libopencv_dnn.so.409",

            "libopencv_features2d.so",
            "libopencv_features2d.so.4.9.0",
            "libopencv_features2d.so.409",

            "libopencv_flann.so",
            "libopencv_flann.so.4.9.0",
            "libopencv_flann.so.409",

            "libopencv_ml.so",
            "libopencv_ml.so.4.9.0",
            "libopencv_ml.so.409",

            "libopencv_objdetect.so",
            "libopencv_objdetect.so.4.9.0",
            "libopencv_objdetect.so.409",

            "libopencv_photo.so",
            "libopencv_photo.so.4.9.0",
            "libopencv_photo.so.409",

            "libopencv_stitching.so",
            "libopencv_stitching.so.4.9.0",
            "libopencv_stitching.so.409",
        ],
    }),
    out_include_dir = "include/opencv4",
    visibility = ["//visibility:public"],
)
