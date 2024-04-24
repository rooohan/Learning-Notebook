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

# QuickStart

```bash
docker-compose -f ./devops/docker-compose.yml up
poetry shell
```

1. 创建[buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)

   创建一个名为 `localstack-thumbnails-app-images`的存储桶，

   ```bash
   awslocal s3 mb s3://localstack-thumbnails-app-images
   ```

   - `awslocal` 是一个命令行工具，它是 `aws` 命令的一个包装器，用于与 LocalStack 交互。
   - `s3` 是指定的AWS 服务，用于存储和检索数据。
   - `mb` 是 `make bucket` 的缩写，用于创建一个新的存储桶。
   - `s3://localstack-thumbnails-app-images` 是新存储桶的名称。

2. 存储桶地址写入AWS Systems Manager

   ```bash
   awslocal ssm put-parameter \
       --name /localstack-thumbnail-app/buckets/images \
       --type "String" \
       --value "localstack-thumbnails-app-images"
   ```

   - `ssm`  AWS Systems Manager 的缩写，用于管理 AWS 资源的服务。
   - `put-parameter` 是一个命令，用于在 Parameter Store 中创建一个新的参数。
   - `--name /localstack-thumbnail-app/buckets/images` 指定了新参数的名称。
   - `--type "String"` 指定了参数的类型为字符串。
   - `--value "localstack-thumbnails-app-images"` 指定了参数的值。

3. 创建SNS

   AWS Simple Notification Service（SNS）是一种高可扩展、高可靠性的消息发布和订阅服务。它能够在应用程序、服务和设备之间以可靠的方式传递消息，并支持广泛的消息传输协议，包括 HTTP、HTTPS、Email、SMS、SQS（Simple Queue Service）、Lambda、Mobile Push 和自定义协议等。

   但是不能保证消息的有序性, 如果有序请使用SQS(Amazon Simple Queue Service)

   ```bash
   awslocal sns create-topic --name failed-resize-topic
   ```

4. 订阅SNS

   ```bash
   awslocal sns subscribe \
       --topic-arn arn:aws:sns:us-east-1:000000000000:failed-resize-topic \
       --protocol email \
       --notification-endpoint my-email@example.com
   ```

   - `sns` 是 AWS Simple Notification Service 的缩写，这是一个用于发布-订阅（pub-sub）消息传递的服务。
   - `subscribe` 是一个命令，用于为一个特定的主题创建一个新的订阅。
   - `--topic-arn arn:aws:sns:us-east-1:000000000000:failed-resize-topic` 
     - `arn` Amazon Resource Name, 指定了你想要订阅的主题.
     - `us-east-1` 是 AWS 区域的标识符，表示这个资源位于 AWS 的美国东部（弗吉尼亚北部）区域。
     - `000000000000` 是 AWS 账户的 ID，表示这个资源属于哪个 AWS 账户
   - `--protocol email` 指定了通知的协议为电子邮件。
   - `--notification-endpoint my-email@example.com` 指定了接收通知的电子邮件地址。

5. 存储桶事件触发Lambda

   设置 S3 存储桶 `localstack-thumbnails-app-images` 的通知配置，当有对象被创建时，触发 Lambda 函数 `resize`

   ```bash
   awslocal s3api put-bucket-notification-configuration \
       --bucket localstack-thumbnails-app-images \
       --notification-configuration "{\"LambdaFunctionConfigurations\": [{\"LambdaFunctionArn\": \"$(awslocal lambda get-function --function-name resize | jq -r .Configuration.FunctionArn)\", \"Events\": [\"s3:ObjectCreated:*\"]}]}"
   ```

   - `awslocal s3api put-bucket-notification-configuration`：这是用于设置 S3 存储桶通知配置的 AWS CLI 命令。
   - `--bucket localstack-thumbnails-app-images`：指定了要设置通知配置的 S3 存储桶，即 `localstack-thumbnails-app-images`。
   - `--notification-configuration`：指定了通知配置的内容。这里使用了 JSON 格式的字符串来定义通知配置。
   - `{"LambdaFunctionConfigurations": [...]}`：这部分定义了 Lambda 函数的配置。在这个例子中，只有一个 LambdaFunctionConfigurations。
   - `\"LambdaFunctionArn\": \"$(awslocal lambda get-function --function-name resize | jq -r .Configuration.FunctionArn)\"`：这部分是 Lambda 函数配置的详细信息，其中包括 Lambda 函数的 ARN（Amazon 资源名称）。通过 `$(...)` 这种语法，调用了另一个命令 `awslocal lambda get-function` 来获取 Lambda 函数 `resize` 的详细信息，然后通过 `jq` 工具提取出其中的 `FunctionArn` 属性。`jq -r .Configuration.FunctionArn` 的作用是从 Lambda 函数的详细信息中提取出 FunctionArn，并以纯文本形式输出。
   - `\"Events\": [\"s3:ObjectCreated:*\"]`：这部分指定了触发 Lambda 函数的事件类型，即在 S3 存储桶中有对象被创建时触发 Lambda 函数。这里使用的事件类型是 `s3:ObjectCreated:*`，表示任何对象被创建时都会触发。

6. 创建Lambda函数

   在 LocalStack 的 Lambda 服务中创建一个新的函数，名为 `resize`，运行时环境为 Python 3.9，超时时间为 10 秒，函数代码在 `lambdas/resize/lambda.zip` 文件中，处理程序为 `handler.handler`，死信队列为 `arn:aws:sns:us-east-1:000000000000:failed-resize-topic`，执行函数的 IAM 角色为 `arn:aws:iam::000000000000:role/lambda-role`，并设置了环境变量 `STAGE` 的值为 `local`。

   ```bash
   awslocal lambda create-function \
       --function-name resize \
       --runtime python3.9 \
       --timeout 10 \
       --zip-file fileb://lambdas/resize/lambda.zip \
       --handler handler.handler \
       --dead-letter-config TargetArn=arn:aws:sns:us-east-1:000000000000:failed-resize-topic \
       --role arn:aws:iam::000000000000:role/lambda-role \
       --environment Variables="{STAGE=local}"
   ```

   - `create-function` 是一个命令，用于创建一个新的 Lambda 函数。
   - `--function-name resize` 指定了新函数的名称为 `resize`。
   - `--runtime python3.9` 指定了函数的运行时环境为 Python 3.9。
   - `--timeout 10` 指定了函数的超时时间为 10 秒。
   - `--zip-file fileb://lambdas/resize/lambda.zip` 指定了包含函数代码的 ZIP 文件的路径。
   - `--handler handler.handler` 指定了函数的处理程序，这是在你的代码中调用的函数。
   - `--dead-letter-config TargetArn=arn:aws:sns:us-east-1:000000000000:failed-resize-topic` 指定了死信队列的 ARN，如果 Lambda 函数处理失败，未处理的事件将发送到这个 SNS 主题。
   - `--role arn:aws:iam::000000000000:role/lambda-role` 指定了执行函数的 IAM 角色的 ARN。
   - `--environment Variables="{STAGE=local}"` 指定了函数的环境变量。

# 基础概念

1. [S3 (Simple Storage Service) ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

   一种对象存储服务, 提供了可扩展性、数据可用性、安全性和性能. 常见的应用场景有:

   - **静态网站托管**
   - **内容分发**
   - **备份和存档**: 定期将数据库备份存储
   - **大数据分析**: 
   - **文件上传**







   

   
