## 如何使用



#### 新建：构建工作文件夹

```bash
python Excel_JS_Runtime_CLI init myfristproject
```

工作文件会包含以下文件：

1. anynameifyoulike.xlsm
2. src 文件夹（其中包含所有的 javascript 文件）
3. Excel_JS_Runtime_CLI.setting.json



#### 展开：把 xlsm 文件展开到文件夹

```
python Excel_JS_Runtime_CLI spread myfristproject.xlsm myfristproject
```



#### 打包：把 javascript 打包到 xlsm 文件中

```
python Excel_JS_Runtime_CLI pack myfristproject myfristproject.xlsm
```



#### 动态打包：每次 javascript 保存时，自动打包进 xlsm 文件中

```
python Excel_JS_Runtime_CLI watch-pack myfristproject myfristproject.xlsm
```

