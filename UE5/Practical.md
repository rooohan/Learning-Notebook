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