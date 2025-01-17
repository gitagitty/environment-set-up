# 1 安装ROS
终端输入
```
wget http://fishros.com/install -O fishros && . fishros
```
输入1
推荐更换系统源进行安装，更换系统源并清理第三方源  
然后根据你要安装的ros版本进行安装  
我这里选择foxy/noetic  
然后等待

# 2 
如果catkin编译时出现python依赖相关问题，可能是使用了其他环境的python，可以先在电脑上确认python安装
```
python --version
```
然后指定系统自带python进行编译，通常为
```
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```