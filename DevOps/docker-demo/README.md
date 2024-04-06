# 项目准备
1. 我们在`app`文件夹下实现了一个非常简单的`WebAPI Demo`

# Dockerfile实现
1. 在项目根目录下新建`devops`文件夹, 并新建`Dockerfile`文件(一般建议在根目录下直接建文件就好).
2. 在`Dockerfile`文件中, 编写要构建镜像的命令
3. 在项目根目录下运行: `docker build -t fastapi-hello-world -f devops/Dockerfile .`
   > 注意:
   1. 此处`fastapi-hello-world` 即为你想构建的镜像的名字
   2.  `-f` 指定了`Dockerfile`文件 所在的路径
   3.  `.` 指定了Docker引擎用来查找和读取构建上下文中的文件的路径, 即此处为根目录
4.  运行`docker image ls` 即可看到自己刚构建成功的镜像
   

# 运行镜像

1. `docker run -p 8000:8000 fastapi-hello-world`
   > 此处踩了一个巨坑, 关于`WSL2`的, 解决方案:[参考链接](https://superuser.com/questions/1714002/wsl2-connect-to-host-without-disabling-the-windows-firewall)
2. 浏览器访问`http://localhost:8000/docs` 即可

