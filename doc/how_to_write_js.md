# 如何编写js

Excel_JS_Runtime 中使用的 JSCRIPT 所以和 web 开发中的 JavaScript 有少许不同



## 基础例子

#### 返回值

```javascript
define([
], function() {
    ExcelResult = "I am bbbb";
});
```

这个代码就是让单元格显示 I am bbbb

#### 传入值

```javascript
define([

], function() {
    ExcelResult = Number(ExcelArgu[0]) + Number(ExcelArgu[1]);

});
```

传入值会被存在数组 **ExcelArgu** 中，第一个传入值就是 **ExcelArgu[0]** ，第二个就是 **ExcelArgu[1]**

