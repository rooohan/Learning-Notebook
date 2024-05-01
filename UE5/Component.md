# API

## Light

- `Toggle Visibility` : 开启关闭光源



## Time

### TimeLine

按设定的函数图像输出`float`

- 很多时候是要选择`play from start`



### Delay

一个延时组件(只能在Event 中应用)



### Set Global Time Dilation

设定全局的时间流速



## Process control

### Sequence

接上`Sequence` , 后面可以接自定义函数或者`Event`

### Branch

根据`condition`, 执行True 或者False后面的逻辑











## Spawn

### Spawn Action from class

指定`cls`后,生成指定的cls

### Spawn Emitter from Location

在指定位置生成一个特效



## Vector

### Break Vector

将一个返回值是向量的`Vector`打散

### Make Vector

将几个数字合并成一个Vector



### IsValid

判断一个类是否有效



### Get Forward Vector

获取`Target`的方向向量坐标



## Math

### Get Random Integer



## Physics

### Set Simulate Physics

对`Target` 启用 `物理`

> 开始`simulate`后, 如果`Target`依赖或依附其他组件, 那么会自动分离, 所以一般此时后面会跟`Attach Component To Component` 让其复原

### Add Impulse

对`Target`添加冲量

### Movement

#### Disable Movement

角色移动组件不可用

#### Set Movement Mode

角色的移动组件可用





# BP

## 添加`BP_Reference`

你可以在一个BP_A中添加另一个`BP_Reference`引用:

1. 在`component` 中添加一个变量`BP_XXX`,并将其类型设定为`XXX`;
2. 并将新建变量`BP_XXX`的`Detail`的`可编辑实例`和`生成时公开`设置为`True`;
3. 编译
4. 在`BP_A`中的`默认`中将看到`component` 中新建的变量`BP_XXX`, 选择右边的吸附工具,吸附.



## 数据结构

### Int

- switch on int



### Enum

1. 在`Context`文件夹中右键,选择`创建高级资产`下的`蓝图`下的`Enum`
2. 添加对应的值

常用API:

- `switch on XXX-YOUR-ENUM-TYPE`

  会获取一个分支, 然后可以后面继续执行

### Structure

1. 在`Context`文件夹中右键,选择`创建高级资产`下的`蓝图`下的`Structure`
2. 添加对应的值

修改其对应的值有两种方式:

- 全量更新:

  1. 拖拽至工作台选择`set {structure} `
  2. 左边拖拽出`make XXXStructure`

- 部分更新:

  1. 拖拽至工作台选择`get {structure} `
  2. 右边拽出`set member in {structure}`, 并修改要修改的值
  3. `set member`的`Struct Out`输出链接到`set {structure}`上


### Array

- For each loop
- Get (a copy)
- Get (a reference)





# Utils

## comment

1. 选中所有框后,按`C`
2. `缩放时显示气泡`设置为`True`



## Why Function or Evenr

这是我本身一个比较大的疑惑, 因为我发现我不能在`function` 中拉出一个`delay`节点,但是在`Event`中就可以. 对此有一些解释:

> https://forums.unrealengine.com/t/why-cant-i-add-a-delay-node-to-a-function/284366/9

这也验证了一些区别:

- `Event`没有返回值，并允许延迟和其他潜在功能。
- `function` 不行

## Debug

1. 在蓝图的图表界面, 在可拖拽界面右键一个`变量`, 选中`查看此数值`
2. 在当前页面,选择`运行`按钮
3. 选择`未选中调试对象` 下拉菜单, 将其替换成我们刚选中的`数值`
4. 玩游戏触发 我们要查看的逻辑
5. 鼠标移上去可以看到变量值





# Component

## RoatingMovement

可以让其旋转

- Rotation Rate 旋转的速率



## Arrow

目前还不太清楚是做什么的



## StaticMesh

### Collision

> 对于武器或者拾取的什么东西, 设置为没有碰撞会更好些

#### Present

- camera ignore 不会撞到相机





# UE5

## Varible

### Detail

- 可编辑实例 选中按钮后,会让此变量变成`obj`的一个实例属性, 我们可以在关卡中自定义不同的值
