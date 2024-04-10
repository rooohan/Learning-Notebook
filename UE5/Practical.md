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





## 抽象类设计

1. 用`Enum`类, 定义一些不同`Type`的类型

2. 用`Structure`(类似于数据类) 定义`Obj`的属性, 注意这个是可以嵌套定义的

3. 定义一个`BP ABC`类:

   1. 在里面添加上面步骤定义的变量

   2. 可选的设置变量的默认值

   3. 在视图视角中, 添加一个`Sphere Collision` 和`Static Mesh`

      > 可以在`Static Mesh`中设置一个`Static Mesh`作为预览占位符

4. 继承于`BP ABC`类, 创建新的子类. 并自定义属性默认值等