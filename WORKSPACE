load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# gRPC

http_archive(
    name = "rules_proto_grpc",
    integrity = "sha256-Kghgozaug2tUZxy74HEO7BfGTvcMTFqIzP1H6m43Ob0=",
    strip_prefix = "rules_proto_grpc-4.6.0",
    urls = ["https://github.com/rules-proto-grpc/rules_proto_grpc/releases/download/4.6.0/rules_proto_grpc-4.6.0.tar.gz"],
)

load("@rules_proto_grpc//:repositories.bzl", "rules_proto_grpc_toolchains", "rules_proto_grpc_repos")
rules_proto_grpc_toolchains()
rules_proto_grpc_repos()

load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
rules_proto_dependencies()
rules_proto_toolchains()

load("@rules_proto_grpc//cpp:repositories.bzl", "cpp_repos")
cpp_repos()

# foreign_cc

http_archive(
    name = "rules_foreign_cc",
    sha256 = "476303bd0f1b04cc311fc258f1708a5f6ef82d3091e53fd1977fa20383425a6a",
    strip_prefix = "rules_foreign_cc-0.10.1",
    url = "https://github.com/bazelbuild/rules_foreign_cc/releases/download/0.10.1/rules_foreign_cc-0.10.1.tar.gz",
)
load("@rules_foreign_cc//foreign_cc:repositories.bzl", "rules_foreign_cc_dependencies")
rules_foreign_cc_dependencies()

# OpenCV

local_repository(
    name = "opencv",
    path = "third_party/opencv",
)

new_local_repository(
    name = "opencv_local",
    path = "third_party/opencv_local",
    build_file = "//third_party:opencv_local.BUILD",
)

http_archive(
    name = "opencv_src",
    build_file = "//third_party:opencv_src.BUILD",
    strip_prefix = "opencv-4.9.0",
    urls = ["https://github.com/opencv/opencv/archive/4.9.0.zip"],
    integrity = "sha256-m1tk1Qv0o93qtDCpsTxfngI8nmdjmrUKdNDCmLWmG3Q=",
)
