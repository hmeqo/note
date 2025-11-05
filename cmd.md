### 查看本目录下非当前用户和组的文件

```bash
fd -u --owner "!$USER" --owner ":!$USER"
```

### 全局搜索替换

```bash
rg -l '<pattern>' </path/to> | sed 's/.*/"&"/' | xargs sed -i 's/<pattern>/<replacement>/g'
```

### 生成自签名证书

```bash
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 \
  -nodes -keyout key.pem -out cert.pem \
  -addext "subjectAltName=IP:127.0.0.1,DNS:localhost"
```
