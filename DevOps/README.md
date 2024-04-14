# 环境安装

> 以下命令，需要科学上网

## 通用工具安装

1. 安装[Scoop](https://scoop.sh/).

2. 安装Git ：`scoop install git`.

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

   按照教程，在本地电脑上[配置SSH密钥](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)，并将[密钥添加到Github账户](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account).

   > 此处笔者踩了一个小坑，是代理22的问题， 解决方案如下：
   >
   > [ssh链接github端口22被拒绝](https://www.huatree.top/2024/02/05/20240205-ssh%E9%93%BE%E6%8E%A5github%E7%AB%AF%E5%8F%A322%E8%A2%AB%E6%8B%92%E7%BB%9D/)

3. 安装`WSL2`:

   > 需要win11，[参考链接](https://learn.microsoft.com/zh-cn/windows/python/web-frameworks#install-windows-subsystem-for-linux)

   ```bash
   wsl --install # 安装后需要重启系统
   sudo apt update && sudo apt upgrade
   ```

4. 安装python：

   > 注意此处安装的Python是win系统下

   ```bash
   scoop install python # 安装完成后可选运行注册表
   ```

   运行`python --version`可以看到已正确安装

### Python第三方工具安装

1. 安装[Poetry](https://python-poetry.org/docs/#installing-with-pipx)

   1. 安装[pipx](https://github.com/pypa/pipx): `scoop install pipx`; `pipx ensurepath`

   ```bash
   pipx install poetry
   pipx ensurepath  # 将poetry添加到环境变量中
   poetry completions bash >> ~/.bash_completion # 可选 代码补全
   ```

2. 安装[pre-commit](https://pre-commit.com/)

   ```bash
   pipx install pre-commit
   ```

   在项目中集成`pre-commit`:

   ```bash
   poetry add pre-commit --group dev
   ```

   右键新建文件`.pre-commit-config.yaml`, 运行`pre-commit sample-config` 并将内容复制到`.pre-commit-config.yaml`

   ```bash
   pre-commit install
   ```
