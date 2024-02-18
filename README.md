# Mocap System

## Requirements

1. [Bazel](https://bazel.build/)

2. [OpenCV](https://opencv.org/)

    1. Follow the [instructions](https://docs.opencv.org/4.9.0/d7/d9f/tutorial_linux_install.html) to compile OpenCV from source.

    2. Link the build directory to `third_party/opencv`:

        ```bash
        ln -s path/to/opencv third_party/opencv
        ```

## Demos

### `hello-cv-cpp`

```bash
bazel run //demos/hello-cv-cpp:main
```

### `hello-proto`

```bash
bazel run //demos/hello-proto:main
```
