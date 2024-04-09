# 使用 Python 3.10 镜像作为基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /docker-demo

# 安装 poetry
RUN pip install poetry

# 将 pyproject.toml 和 poetry.lock 文件复制到工作目录
COPY pyproject.toml poetry.lock /docker-demo/

# 安装项目依赖
RUN poetry install --no-interaction --no-ansi

# 将项目文件复制到工作目录
COPY . /docker-demo

RUN ls -la /docker-demo

# 暴露端口 8000
EXPOSE 8000

# 使用 uvicorn 运行你的 FastAPI 应用
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]