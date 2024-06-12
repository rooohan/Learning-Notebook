# 环境



```bash
docker pull solr
```

## 运行

```bash
mkdir solrdata
sudo chown -R 8983:8983 $PWD/solrdata  # 设置权限
docker run -d -v "$PWD/solrdata:/var/solr" -p 8983:8983 --name my_solr solr solr-precreate gettingstarted
```

或者

```bash
docker compose up -d
```

## 访问

`http://localhost:8983/solr/#/`
