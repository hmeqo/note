### 全局搜索替换

```bash
rg -l '<pattern>' </path/to> | sed 's/.*/"&"/' | xargs sed -i 's/<pattern>/<replacement>/g'
```

### mysql 迁移到 postgresql

```bash
docker run --rm dimitri/pgloader \
  pgloader \
  "mysql://root:password@host.docker.internal:3306/source_db" \
  "postgresql://postgres:password@host.docker.internal:5432/target_db"
```
