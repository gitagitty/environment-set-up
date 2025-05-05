# 1 安装TensorRT

官方文档：https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html

## 1

进入 https://developer.nvidia.com/tensorrt/download
选择你cuda和ubuntu版本对应的tensorRT  选择 tar package. 如果选择deb，需要cuda和cudnn都为deb安装方式
例：
我这边选择TensorRT 8.6 GA for Linux x86_64 and CUDA 11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7 and 11.8 TAR Package

## 2

下载并解压，终端进入对应文件夹

安装:

```
cd python
python3 -m pip install tensorrt-*-cp3x-none-linux_x86_64.whl
```

把想要装的python版本替换3x，一般为38
把 * 替换为具体版本号

如果是tensorrt8：

```
cd ../graphsurgeon
python3 -m pip install graphsurgeon-0.4.6-py2.py3-none-any.whl
```

```
cd ../onnx_graphsurgeon

python3 -m pip install onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl
```

如果是tensorrt10：

```
python3 -m pip install tensorrt_lean-*-cp3x-none-linux_x86_64.whl
python3 -m pip install tensorrt_dispatch-*-cp3x-none-linux_x86_64.whl

```

# 2 pytorch安装

https://pytorch.org/get-started/locally/

# 安装ubuntu

注意一个固态硬盘最多只能分4个区，在ubuntu分区时注意最大分区数量
