# Dockerfile

## 项目准备

1. 我们在`app`文件夹下实现了一个非常简单的`WebAPI Demo`

## Dockerfile实现
1. 在项目根目录下新建`devops`文件夹, 并新建`Dockerfile`文件(一般建议在根目录下直接建文件就好).
2. 在`Dockerfile`文件中, 编写要构建镜像的命令
3. 在项目根目录下运行: `docker build -t fastapi-hello-world -f devops/Dockerfile .`
   > 注意:
   >
   > 1. 此处`fastapi-hello-world` 即为你想构建的镜像的名字
   > 2. `-f` 指定了`Dockerfile`文件 所在的路径
   > 3. `.` 指定了Docker引擎用来查找和读取构建上下文中的文件的路径, 即此处为根目录
4.  运行`docker image ls` 即可看到自己刚构建成功的镜像


## 运行镜像

1. `docker run -p 8000:8000 fastapi-hello-world`

   > 此处踩了一个巨坑, 关于`WSL2`的, 解决方案:[参考链接](https://superuser.com/questions/1714002/wsl2-connect-to-host-without-disabling-the-windows-firewall)
2. 浏览器访问`http://localhost:8000/docs` 即可



## 性能测试

1. 安装`Apache HTTP` 性能测试工具:

   ```bash
   sudo apt-get update
   sudo apt-get install apache2-utils
   ```

2. 测试原生启动非docker环境下的`QPS`:

   ```bash
   # -n 1000 表示总共发送 1000 个请求
   # -c 100  表示并发 100 个请求
   ab -n 1000 -c 100 http://localhost:8000/
   ```

   输出数据如下:
   ```bash
   This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
   Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
   Licensed to The Apache Software Foundation, http://www.apache.org/
   
   Benchmarking localhost (be patient)
   Completed 100 requests
   Completed 200 requests
   Completed 300 requests
   Completed 400 requests
   Completed 500 requests
   Completed 600 requests
   Completed 700 requests
   Completed 800 requests
   Completed 900 requests
   Completed 1000 requests
   Finished 1000 requests
   
   
   Server Software:        uvicorn
   Server Hostname:        localhost
   Server Port:            8000
   
   Document Path:          /
   Document Length:        25 bytes
   
   Concurrency Level:      100
   Time taken for tests:   0.248 seconds
   Complete requests:      1000
   Failed requests:        0
   Total transferred:      150000 bytes
   HTML transferred:       25000 bytes
   Requests per second:    4040.09 [#/sec] (mean)
   Time per request:       24.752 [ms] (mean)
   Time per request:       0.248 [ms] (mean, across all concurrent requests)
   Transfer rate:          591.81 [Kbytes/sec] received
   
   Connection Times (ms)
                 min  mean[+/-sd] median   max
   Connect:        0    0   0.2      0       1
   Processing:     1   23   4.7     25      27
   Waiting:        1   23   4.8     25      27
   Total:          2   23   4.5     25      27
   
   Percentage of the requests served within a certain time (ms)
     50%     25
     66%     25
     75%     26
     80%     26
     90%     26
     95%     26
     98%     27
     99%     27
    100%     27 (longest request)
   ```

   可以得出主要的结论:

   - `P90`为 `26ms`, 即 90% 请求都可以在 26ms时完成
   - `QPS`为 4040.09, 即 一秒钟最大请求数为4040.09

3. 测试`docker`中的性能情况

   ```bash
   docker run -p 8000:8000 fastapi-hello-world
   ab -n 1000 -c 100 http://localhost:8000/  # 同样的情况
   ```

   输出数据如下:

   ```bash
   This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
   Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
   Licensed to The Apache Software Foundation, http://www.apache.org/
   
   Benchmarking localhost (be patient)
   Completed 100 requests
   Completed 200 requests
   Completed 300 requests
   Completed 400 requests
   Completed 500 requests
   Completed 600 requests
   Completed 700 requests
   Completed 800 requests
   Completed 900 requests
   Completed 1000 requests
   Finished 1000 requests
   
   
   Server Software:        uvicorn
   Server Hostname:        localhost
   Server Port:            8000
   
   Document Path:          /
   Document Length:        25 bytes
   
   Concurrency Level:      100
   Time taken for tests:   0.471 seconds
   Complete requests:      1000
   Failed requests:        0
   Total transferred:      150000 bytes
   HTML transferred:       25000 bytes
   Requests per second:    2122.58 [#/sec] (mean)
   Time per request:       47.113 [ms] (mean)
   Time per request:       0.471 [ms] (mean, across all concurrent requests)
   Transfer rate:          310.92 [Kbytes/sec] received
   
   Connection Times (ms)
                 min  mean[+/-sd] median   max
   Connect:        0    0   0.4      0       2
   Processing:     3   45  26.5     39     137
   Waiting:        1   45  26.5     39     137
   Total:          3   45  26.6     39     138
   
   Percentage of the requests served within a certain time (ms)
     50%     39
     66%     40
     75%     40
     80%     40
     90%     65
     95%    127
     98%    129
     99%    130
    100%    138 (longest request)
   ```

   可以得出主要的结论:

   - `P90`为 `65ms`, 即 90% 请求都可以在 65ms时完成
   - `QPS`为 2122, 即 一秒钟最大请求数为2122

   ---

   可见在`docker` 容器中运行性能损失蛮大的.



# Redis

拉取redis-docker镜像:

```bash
docker pull redis
```

安装Redis客户端工具

```bash
sudo apt-get install redis-tools
```

启动redis:

```bash
docker run --name redis-for-fastapi -p 6379:6379 redis
```

- `--name my-redis`：为容器指定一个名称，这里使用`my-redis`作为示例。
- `-p 6379:6379`：将主机的`6379`端口映射到容器的`6379`端口，这是Redis默认的端口。
- `-d`：在后台运行容器。
- `redis`：指定要使用的Redis镜像。

使用Redis客户端工具, 验证我们的服务已经正常启动:
```bash
redis-cli -h localhost -p 6379

SET mykey "Hello, Redis!"
GET mykey
# 会输出 "Hello, Redis!"
```



# 两个Docker互相访问

1. python安装第三方库`poetry add aioredis`

2. 在`fastapi`的`lifespan`中使用`aioredis`连接`redis`: 

   ```python
   aioredis.from_url(_url)
   ```

   

3. 因为`redis`的`image`和`fastapi`的`image`是各自独立的, 所以`fastapi`的`localhost:6379` 命令并不能访问到`docker`, 为了解决此问题我们需要使用`docker network`命令

   ```bash
   docker network create for-fastapi  # {for-fastapi} 为我们创建的虚拟网络名称
   
   # 启动镜像的时候都要加上 --network, (命令参数都不能放在{镜像名}后面)
   docker run --network for-fastapi --name my-redis -p 6379:6379 redis
   # {my-redis:6379} 就是上一条命令的 redis地址
   docker run -e REDIS_URL=redis://my-redis:6379 --network for-fastapi -p 8000:8000 fastapi-hello-world
   ```

   > - `-e` 参数会在启动时传入环境变量



# Docker命令

## 反射

- `docker inspect {image-name}` 反射镜像的信息
- `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' XXXXX` 获取容器的`IP`
- `docker inspect --format='{{range .Mounts}}{{.Destination}}{{"\n"}}{{end}}' xxxxxxx` 反射挂载路径



### VOLUME

Docker Volume 是 Docker 中用于持久化存储数据的一种机制。它允许容器在不受容器生命周期影响的情况下访问和共享数据。

所以我们做测试的时候写进redis的内容,其实都挂载进了我们的`WSL`中. 为此我们要删除它们

```bash
docker volume ls
```

> DRIVER    VOLUME NAME
> local     6c7c715835c2f6e0e5c91488cd514b1d2344c0aa82b1074866e8697c4613f5e9
> local     53a085553e581fad32bf54ddbd828d5efb9b94bb0b1054704015b472b5aceb64
>
> ---
>
> VOLUME NAME 与我们使用`docker inspect`反射`Mounts` 挂载的值一致

```bash
 # 请确保容器都安全退出, 且没有重要数据再删除
 # 本教程无产生隐私数据, 随便删
 docker volume rm XXXXXXX
```

