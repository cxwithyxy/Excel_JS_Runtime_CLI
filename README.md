# Excel_JS_Runtime_CLI

这是一个命令行工具，便于基于 [Excel_JS_Runtime](https://github.com/cxwithyxy/Excel_JS_Runtime) 的 Excel 的 JavaScript 开发



## 如何安装

1. [下载已经被压缩成7z压缩包的 Excel_JS_Runtime_CLI](https://github.com/cxwithyxy/Excel_JS_Runtime_CLI/releases)
2. 用解压工具（winrar、7z、bandizip等）把这个 Excel_JS_Runtime_CLI.7z 解压到你想要放的地方
3. 然后 设置环境变量 PATH 到你解压出来的 Excel_JS_Runtime_CLI 根目录中



## 如何使用（工作流）

请先打开cmd

1. 构建工作文件夹（见命令说明）
2. cd 进工作文件夹
3. 激活动态打包（见命令说明）
4. 操作（修改、新增、删除）工作文件夹中js文件，Excel_JS_Runtime_CLI 会自动把 [js 文件](doc/how_to_write_js.md)写入 xlsm 中
5. 此时可以对xlsm增加数据，就是 excel 的正常操作，同时你也可以在 [xlsm 中调用](doc/how_to_call_js.md)你写的 js

继续循环第4、5步，直到你满意，就可以 ctrl+s 保存这个xlsm，然后把 xlsm 发给你同事朋友，就算他们没有安装Excel_JS_Runtime_CLI，打开xlsm之后，你编写的js代码也会一样在他们电脑上运行



## 命令

[命令说明](doc/how_to_use.md)



## 开发 Excel_JS_Runtime_CLI

#### 代码下载和开发依赖安装

1. 首先要有python 3.x 和 git
2. git clone 下来
3. cd 到 Excel_JS_Runtime_CLI 根目录
4. 通过 virtualenv 生成 python 环境
5. 切换到 python 环境中
6. 安装依赖 pip install -r requirements.txt -i https:*//mirrors.aliyun.com/pypi/simple/*

#### 运行

```bat
python Excel_JS_Runtime_CLI.py
```

#### 打包

```
pyinstaller Excel_JS_Runtime_CLI.spec
```



## 开发 Excel_JS_Runtime

请移步到 [Excel_JS_Runtime 仓库](https://github.com/cxwithyxy/Excel_JS_Runtime)