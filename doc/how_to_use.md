## 如何使用



#### 新建：构建工作文件夹

```bash
Excel_JS_Runtime_CLI -create myfristproject
```

工作文件会包含以下文件：

1. myfristproject.xlsm
2. src 文件夹（其中包含所有的 javascript 文件）
3. Excel_JS_Runtime_CLI.ini



#### 展开：把 xlsm 文件展开到文件夹

```
Excel_JS_Runtime_CLI -spread here
```

当cd到工作文件夹中时，可以使用该命令 -spread here 把当前文件夹中的xlsm文件的 js 文件保存到 src文件夹中

```
Excel_JS_Runtime_CLI -spread myfirstproject.xlsm
```

把 xlsm 文件 变成 工作文件夹



#### 打包：把 javascript 打包到 xlsm 文件中

```
Excel_JS_Runtime_CLI -pack here
```

当cd到工作文件夹中时，可以使用该命令 -pack here 把当前文件夹中的 src 文件夹中的 js 文件保存到 xlsm 文件



#### 动态打包：每次 javascript 保存时，自动打包进 xlsm 文件中

```
Excel_JS_Runtime_CLI -watch_pack here
```

