# IDE

## VS Code

> based on Version 1.89.0

### Common Setting

点击左下角的设置齿轮选择`settings`, 或使用快捷键`ctrl + ,`进入`settings`界面

1. `Auto Save` 选择`afterDelay`

2. `settings.json`文件配置(可以跳过,只做了解)

   - Global file (以python项目为例)

     `Extensions`-> `Python`(前提是已安装此extentions), 选择任意一个带有`Edit in settings.json` 超链即可打开Global 的`settings.json`文件, 下文中我们配置插件的值也会生成此文件

   - project file

     快捷键`ctrl + shift + P` 键入`Preferences: Open Workspace Settings(JSON)`即可打开或创建当前项目的配置文件

3. `launch.json`文件配置(可以跳过,只做了解)

   点击左侧的`Run and Debug` 选择 `create a launch.json file`, 根据语言不同选择不同的选项.

   

### Keyboard-shortcuts

> [Reference](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference)

- `Alt+ ← / →` 光标切换

### Language

#### Python

##### Type Check

**语法检查**(Nice to have)

1. 点击左下角的设置齿轮选择`settings`, 或使用快捷键`ctrl + ,`

2. 搜索`@id:python.languageServer`, 并将`language server` 修改为`Pylance`

3. 搜索`@id:python.analysis.typeCheckingMode`, 并修改为`standard`

4. 搜索`@id:python.analysis.inlayHints.variableTypes` 勾选

5. 搜索`@id:python.analysis.inlayHints.functionReturnTypes` 勾选

6. 搜索`@id:python.analysis.autoImportCompletions`勾选

7. 搜索`@id:python.analysis.ignore`添加python虚拟环境所在的路径

   > 此操作是为了避免`typeCheckingMode=standard` 后, `Python`源码会被`Pylance`标为报错的问题,
   >
   > 此处我添加的虚拟环境为`/usr/lib/python3.10/**`, 如果不确定自己的位置, 可以点进去源码,看具体位置

**格式检查**

1. `Extensions`中搜索`python formatter`
2. 选择安装`Black Formatter` 

**拼写检查**

1. `Extentsion`中搜索`Code Spell Checker`
2. `ctrl + ,`搜索`@id:cSpell.spellCheckOnlyWorkspaceFiles`勾选
3. 搜索`cSpell.ignorePaths`添加python虚拟环境所在的路径(同上)

> `Extentsion`中安装的检验插件, 对`.gitignore`中的文件是默认不检查的
