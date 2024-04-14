# 物品交互

## 戴帽子

1. 在BP文件中新建一个类， 在组件中添加一个StaticMesh， 并绑定项目中的某个SM
2. 在StaticMesh中添加一个碰撞组件Sphere
3. 在碰撞组件中添加Event事件包括：
   - Begin Overlap：
     - Cast（强制类型转换）To 第三人称角色-> 使其可以监听Input
   - End Overlap：
     - Cast（强制类型转换）To 第三人称角色-> 停止监听Input
   - 键盘`E`：
     - Cast（强制类型转换）To 第三人称角色->Herself.`Equip Hat` （自定义事件）
4. 在BP_ThirdPersion中进行一系列操作：
   - 在视图中增加一个HatMesh
   - 在Event中Add Custom Event： `Equip Hat`
     1.  Set Static Mesh
     2. Attach Component To Component
        - Target ：HatMesh
        - Parent Socket： `HatSocket`
5. 在BP_ThirdPersion 中添加SM：
   1.  在BP_ThirdPersion绑定的Mesh属性中找到角色网格
   2.  在股价的head中增加一个Socket:  `HatSocket`



## 拾取到物品栏

1. 抽象类设计`ItemABC` 类, 其中有个属性`ItemInfo`

2. 继承于`ItemABC` 类,实现具体的物品类

3. 抽象类的`Sphere` 设定碰撞检测, 并在`Overlap`的时候使`Character` `Enable Input`, 并调用`Character`对应的`Event`

4. 在`BP_ThriedPersonCharacter` 中实现`步骤3`中的`Event`

   > 1. 在`BP_ThriedPersonCharacter`中新建一个`InventoryArrary`数组
   >
   > 2. 实现`E Key Event`:
   >
   >    > - Event接收一个参数,类型是`ItemInfo`
   >    > - 内部的逻辑是将接收的参数`append`到`InventoryArrary`数组中

5. 创建`UI Widget`展示`InventoryArrary`数组中的内容



## 抽象类设计

1. 用`Enum`类, 定义一些不同`Type`的类型

2. 用`Structure`(类似于数据类) 定义`Obj`的属性, 注意这个是可以嵌套定义的

3. 定义一个`BP ABC`类:

   1. 在里面添加上面步骤定义的变量

   2. 可选的设置变量的默认值

   3. 在视图视角中, 添加一个`Sphere Collision` 和`Static Mesh`

      > 可以在`Static Mesh`中设置一个`Static Mesh`作为预览占位符

4. 继承于`BP ABC`类, 创建新的子类. 并自定义属性默认值等







# UI

创建: 右键-> 用户界面-> 控件蓝图 -> 用户控件 -> `W_XXXWidget`

## 动态更新图标

`image`的工作舞台需要以下步骤:

1. Canvas Panel

   这是我们用户能看到的界面

2. Horizontal Box

   图标的最外层

3. Border

   可以用来添加选中高亮的效果

4. Image

   后面用来填充Icon的

`Graph`实现需要以下事件:

1. 自定义`UpdateImage` 事件
2. 输入添加:
   - ItemIndex: 第几个`Image` 被更新
   - ItemIcon: 要更新成的`Texture`
3. `ItemIndex` -> `Switch on Int` -> `Set Brush from Texture`

`ThirdPersonCharacter`在`PickUpItem`的时候, 依据`Widget Reference` call上面定义好的`UpdateImage` 事件