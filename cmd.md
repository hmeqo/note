### 全局搜索替换

```bash
rg -l '<pattern>' </path/to> | sed 's/.*/"&"/' | xargs sed -i 's/<pattern>/<replacement>/g'
```

### mysql 迁移到 postgresql

```bash
docker run --rm --it --network host dimitri/pgloader \
  pgloader \
  "mysql://root:password@localhost:3306/db" \
  "postgresql://postgres:password@localhost:5432/db"
```
