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
   2.  在骨架的head中增加一个Socket:  `HatSocket`

## 门

1. 继承于`StaticMeshAction`类创建`BP`, 并`Attach`上门的`SM`和门框的`SM`
2. 设置一个变量`InitialDoorRotation`, 并在`Event BeginPlay`的时候,通过`Get Actor Rotation`获取`SM`的位置并赋值给`InitialDoorRotation`
3. `Add Custom Event`创建开门事件: 
   1. 创建一个开始关键帧是(0,1), 结束关键帧是`(1,90)`的`TimeLine`
   2. 将`InitialDoorRotation`通过`Break Rotation`打散成`X, Y, Z`:
      - X 保持不变
      - Y 保持不变
      - Z 通过`substract` 函数减去`TimeLine`的输出值, 并输出新的 Z
   3. `Set Action Rotation`  的`New Rotation`引脚, 通过`Make Rotation` 接收上一步骤的`X, Y, Z`
4. 设定触发逻辑, 比如检测到重叠事件的时候, 使角色的输入可用, 并在按对应的键以后 call  步骤3中的开门事件



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



# 抽象类设计

1. 用`Enum`类, 定义一些不同`Type`的类型

2. 用`Structure`(类似于数据类) 定义`Obj`的属性, 注意这个是可以嵌套定义的

3. 定义一个`BP ABC`类:

   1. 在里面添加上面步骤定义的变量

   2. 可选的设置变量的默认值

   3. 在视图视角中, 添加一个`Sphere Collision` 和`Static Mesh`

      > 可以在`Static Mesh`中设置一个`Static Mesh`作为预览占位符

4. 继承于`BP ABC`类, 创建新的子类. 并自定义属性默认值等





# 玩家

> - **使用Pawn**：
>   - 当你需要一个非常简单的游戏对象，不需要角色模型或动画时，可以使用Pawn。
>   - 当你需要自定义控制逻辑，比如飞行器、无人机、地面车辆等。
>   - 当你需要与玩家角色具有相同的控制能力，但没有生命值或动画时。
> - **使用Character**：
>   - 当你需要一个具有动画和模型的角色时，使用Character更为合适。
>   - 当你需要一个具有基本生命系统、碰撞体积以及默认的输入和移动逻辑的角色时。
>   - 当你需要一个玩家角色或有生命体现的游戏对象时，使用Character更为合适。

## Pawn

1. 创建一个继承自`Pawn`的蓝图
2. 在`DefaultSceneRoot`上`attach`一个`StaticMesh`, 作为第三人称时看到的模型
3. 在`DefaultSceneRoot`上`attach`一个`SpringArm`
   - `SpringArm`: 弹簧臂, 可以在第三人称视角下,当镜头与`DefaultSceneRoot`之间有障碍物的时候, 可以拉近镜头.
   - `Target Arm Length`: 设置`Camera`的距离
4. 在`SpringArm`上`attach`一个`Camera`
5. 将`GameModel`蓝图类的`Default Pawn Class` 设置为我们上面创建的蓝图类.

## Character

> `Capsule`检测碰撞
>
> `Arrow`前进方向
>
> `Mesh` 装载骨骼网络

1. 创建一个继承自`Character`的蓝图
2. 其他操作类似于`Pawn`

## Controller

### Speech Mappings

> Edid -> Project Settings -> Engine -> Input

要设定这个原因是因为, 如果我们直接在`PlayController`的蓝图 添加某些按键的事件的话, 角色的功能就会跟输入键绑死, 玩家就不能自定义按键了, 所以我们要先创建一个指令map

### 步骤

1. 创建一个继承自`PlayController`的蓝图
2. 实现具体的功能, 并关联对应的指令map集中的具体指令
3. 在`GameModel`蓝图类中将`Play Controller Class`改成自定义的`Controller`类

- `get player character`: `Controller`不能直接访问一些来自角色类才能访问的函数,比如`jump`, 此时要先获取角色

  > 我们还经常会用到一个方法叫`Cast to BP ThiredPerson Character`方法, 这两个的区别是:
  >
  > - `get player character` 获取的是`character`类(父类)
  > - `Cast to BP ThiredPerson Character` 获取的是我们自定义的`Character`类(具体的子类)
  >
  > 所以要访问common的函数时`get player character`就够了, 而`Cast to BP ThiredPerson Character`  是在获取一些我们自定义类属性的时候会用到的.



# 敌人

要创建一个在一个起始点A, 和终止点B之间游荡的敌人可以这样设计:

1. 基于`Pawn`蓝图类创建一个类, 并`attach`上`SM`

2. 创建一个`Vector`变量`EndPoint`(用作B点), 并在属性中设置`可编辑实例`和`可显示控件`

3. 创建一个时间轴:

   - 选中`使用最后一个关键帧`, `自动播放` 和`循环`
   - 创建三个关键帧,并将头尾关键帧的值设为`0`, 第二个设为`1`. (时间轴的总长度/2 代表敌人从A到B共计要花费的时间)

4. 将时间轴的输出值连接到`Lerp(Vector)`的`Alpha`端点

   > 在此处的用处为:生成一系列连续的向量,其开始值为相对于`self`的`[0,0,0]`(即`lerp`函数的`A`端点值), 在经过一秒后插值生成至相对于`self`的B点的位置向量, 再经过一秒后插值生成至`self`的`[0,0,0]`

5. 将`EndPoint`的值链接到`Lerp(Vector)`的`B`端点上

6. 将`Lerp(Vector)`的`Return Value` 的值连接至`Set Relative Location`的`New Location`上

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
