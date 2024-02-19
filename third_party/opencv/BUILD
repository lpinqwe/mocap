cc_library(
    name = "opencv",
    deps = select({
        "@platforms//os:linux": ["@opencv_src//:opencv"],
        "@platforms//os:macos": ["@opencv_src//:opencv"],
        "@platforms//os:windows": ["@opencv_local//:opencv"],
    }),
    visibility = ["//visibility:public"],
)
