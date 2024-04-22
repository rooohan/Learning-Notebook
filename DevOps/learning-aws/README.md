# OverView

本次教程我们使用[localstack](https://www.localstack.cloud/) 在本地模拟`aws`的一些常用API.



# 环境部署

按照官方文档, 选择最便捷的方式`localstack`部署[参考链接](https://docs.localstack.cloud/getting-started/installation/#docker-compose)(以官方最新的教程为主)

1. 在`devops`文件夹中创建`docker-compose.yaml` 文件

   ```yaml
   version: "3.8"
   
   services:
     localstack:
       container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
       image: localstack/localstack
       ports:
         - "127.0.0.1:4566:4566"            # LocalStack Gateway
         - "127.0.0.1:4510-4559:4510-4559"  # external services port range
       environment:
         # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
         - DEBUG=${DEBUG:-0}
       volumes:
         - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
         - "/var/run/docker.sock:/var/run/docker.sock"
   ```

2. 运行`docker compose `

   ```bash
   docker-compose -f ./devops/docker-compose.yml up
   ```

3. 停止服务

   ```bash
   docker-compose -f ./devops/docker-compose.yml down
   ```

4. 安装`LocalStack CLI`

   本项目用`Python`虚拟环境代替

   ```bash
   poetry install
   
   # 如果没有激活虚拟环境,那么运行下面命令
   poetry shell
   ```

   验证安装

   ```bash
   localstack config validate -f devops/docker-compose.yml
   ```

   

   
