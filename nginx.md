## 配置

### 手机端 pc 端自动判断

```nginx
map $http_user_agent $backend_port {
    default                         "3000";  # 默认PC端
    ~*(android|iphone|ipad|mobile)  "3001";  # 移动设备
}
```

并设置转发

```nginx
server {
    location / {
        # 根据设备类型转发到不同端口
        proxy_pass http://127.0.0.1:$backend_port;

        # 必要的代理头设置
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # WebSocket支持
        # proxy_http_version 1.1;
        # proxy_set_header Upgrade $http_upgrade;
        # proxy_set_header Connection "upgrade";
    }
}
```

### 反向代理

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
