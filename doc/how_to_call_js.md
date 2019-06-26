# 如何在 Excel 中调用写好的 js

Excel_JS_Runtime_CLI  能够把 js文件 导入 Excel 文件中， 但只有 xlsm 格式的 Excel文件才能运行 js 代码



## 基础调用

把你的js保存好，命名为 a.js

### 调用 js 文件

在 excel 的单元格中输入

```
=runJS("a.js")
```

然后单元格就会显示 a.js 运行后的结果，结果取决于返回值。

#### 传入一些值给 js 文件

在 excel 的单元格中输入

```
=runJS("a.js",3,2)
```

3 和 2 便是传入值了，在 a.js 中可以对着两个值进行处理，并返回处理后的结果。