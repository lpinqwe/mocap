load("@rules_proto_grpc//cpp:defs.bzl", "cpp_proto_library")

proto_library(
  name = "hello_proto",
  srcs = ["hello.proto"],
)

cpp_proto_library(
    name = "cpp_hello_proto",
    protos = [":hello_proto"],
)

cc_binary(
    name = "main",
    srcs = ["main.cpp"],
    deps = [":cpp_hello_proto"],
)
