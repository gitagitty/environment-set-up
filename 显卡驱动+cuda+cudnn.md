需求：nvidia显卡  
# 1 安装显卡驱动
配置：nvidia显卡
## 方法1
点开软件和更新  
附加驱动  
选择 使用NVIDIA driver metapackage 来自 nvidia-driver-535
建议选择不带后缀的显卡驱动  
点击应用更改
## 方法2
1. 添加驱动源
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
```
2. 打开终端，输入
```
ubuntu-drivers devices
```
输出类似
```
driver   : nvidia-driver-535 - third-party non-free
driver   : nvidia-driver-570-server - distro non-free
driver   : nvidia-driver-535-server - distro non-free
driver   : nvidia-driver-570-server-open - distro non-free
driver   : nvidia-driver-560-open - third-party non-free
driver   : nvidia-driver-560 - third-party non-free
driver   : nvidia-driver-550 - third-party non-free
driver   : nvidia-driver-545-open - third-party non-free
driver   : nvidia-driver-570-open - third-party non-free
driver   : nvidia-driver-535-server-open - distro non-free
driver   : nvidia-driver-535-open - third-party non-free
driver   : nvidia-driver-550-open - third-party non-free
driver   : nvidia-driver-570 - third-party non-free recommended
driver   : nvidia-driver-545 - third-party non-free
driver   : xserver-xorg-video-nouveau - distro free builtin
```
3. 选择你想要的显卡驱动，建议选择数字后不带后缀的版本
4. 安装
```
sudo apt install nvidia-driver-5xx
```
将你选择的driver名称替换nvidia-driver-5xx

## 验证
### 1. 重启  
终端输入
```
nvidia-smi
```
如果跳出以下类似界面则安装成功
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.04             Driver Version: 570.124.04     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:01:00.0  On |                  N/A |
| N/A   52C    P8              4W /  115W |     366MiB /   8188MiB |      6%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1328      G   /usr/lib/xorg/Xorg                       59MiB |
|    0   N/A  N/A            1752      G   /usr/lib/xorg/Xorg                       99MiB |
|    0   N/A  N/A            1910      G   /usr/bin/gnome-shell                     97MiB |
|    0   N/A  N/A            3603      G   ...ess --variations-seed-version         45MiB |
+-----------------------------------------------------------------------------------------+

```
# 2 CUDA安装
官方文档：https://docs.nvidia.com/cuda/cuda-installation-guide-linux/contents.html
## 确认能够安装的cuda版本  
终端输入
```
nvidia-smi
```
输出
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.04             Driver Version: 570.124.04     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:01:00.0  On |                  N/A |
| N/A   52C    P8              4W /  115W |     366MiB /   8188MiB |      6%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1328      G   /usr/lib/xorg/Xorg                       59MiB |
|    0   N/A  N/A            1752      G   /usr/lib/xorg/Xorg                       99MiB |
|    0   N/A  N/A            1910      G   /usr/bin/gnome-shell                     97MiB |
|    0   N/A  N/A            3603      G   ...ess --variations-seed-version         45MiB |
+-----------------------------------------------------------------------------------------+

```
第一行显示 CUDA Version: 12.8  
这表明我电脑最高能装cuda 12.8版本
## 安装cuda
进入https://developer.nvidia.com/cuda-toolkit-archive  
选择你所需要的cuda版本  
选择linux-x86_64-ubuntu-20.04-runfile(local)
按照下面安装引导安装  
在运行安装程序后，将显卡驱动去掉，不安装驱动
```
│ - [ ] Driver                                                                 │
│      [ ] 570.86.10                                                           │
│ + [X] CUDA Toolkit 12.8                                                      │
│   [X] CUDA Demo Suite 12.8                                                   │
│   [X] CUDA Documentation 12.8                                                │
│ - [ ] Kernel Objects                                                         │
│      [ ] nvidia-fs                                                           │
│   Options                                                                    │
│   Install 
```
## 配置环境变量
通常cuda会被安装在/usr/local/cuda-X.X  
1. 打开终端输入
```
sudo gedit ~/.bashrc
```  
2. 在文件中添加下列内容
```
export CUDA_HOME=/usr/local/cuda-X.X
export PATH=/usr/local/cuda-X.X/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-X.X/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
将代码中cuda-X.X替换成你的cuda版本  
例： cuda-12.6  
保存并退出
3. 更新
```
source ~/.bashrc 
```
## 验证安装
终端输入
```
nvcc -V
```
输出类似信息则安装成功
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Wed_Aug_14_10:10:22_PDT_2024
Cuda compilation tools, release 12.6, V12.6.68
Build cuda_12.6.r12.6/compiler.34714021_0
```
（但是本人没有这个输出也能用）

## 关于切换不同cuda版本
按照以上过程安装不同版本的cuda  
cuda版本可通过设置环境变量来切换，在～/.bashrc 中调整想要的cuda版本的环境变量并刷新

# 3 安装cudnn
cudnn官方文档：https://docs.nvidia.com/deeplearning/cudnn/latest/
## 1
进入https://developer.nvidia.com/rdp/cudnn-archive  
选择你的cuda和ubuntu对应的cudnn版本  
选择 Local Installer for Linux x86_64 (Tar)并下载

## 2
1. 将压缩包解压
```
tar -xf cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz
```
2. 复制文件到指定地址
```
sudo cp cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/* /usr/local/cuda-11.8/include
sudo cp cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn* /usr/local/cuda-11.8/lib64
```
将自己的cudnn文件路径和cuda路径替代终端中的  
当选择对应cuda版本时，cudnn也会自动切换成对应cuda文件夹下的版本
