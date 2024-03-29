# 环境安装

> 以下命令，需要科学上网

## 通用工具安装

1. 安装[Scoop](https://scoop.sh/).

2. 安装Git ：`scoop install git`.

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

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

2. 



