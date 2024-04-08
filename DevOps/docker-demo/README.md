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



# Redis

