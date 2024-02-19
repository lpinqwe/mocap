cc_library(
    name = "opencv",
    srcs = select({
        "@platforms//os:macos": glob(["lib/libopencv_*.dylib"]),
        "@platforms//os:linux": glob(["lib/libopencv_*.so", "lib/libopencv_*.so.*"]),
        "@platforms//os:windows": glob(["lib/libopencv_*.dll"]),
    }),
    hdrs = glob(["include/opencv4/**/*.h", "include/opencv4/**/*.hpp"]),
    visibility = ["//visibility:public"],
    linkstatic = 1,
    includes = ["include/opencv4"],
)
