# django

## 安装

```bash
pip install django
```

## 创建项目

```bash
django-admin startproject mysite
```

## 项目结构

```txt
mysite
|---- manage.py         # 项目管理
|---- mysite            # 主文件夹
|    |---- __init__.py
|    |---- asgi.py      # 异步wsgi
|    |---- settings.py  # 设置
|    |---- urls.py      # 路由
|    |---- wsgi.py      # wsgi
|---- myapp
|    |---- migrations        # 迁移数据库所需文件
|    |    |---- __init__.py
|    |---- __init__.py
|    |---- admin.py          # 数据库管理模型
|    |---- apps.py           # app
|    |---- forms.py          # 表单, 非必要
|    |---- models.py         # 数据模型
|    |---- tests.py          # 单元测试
|    |---- views.py          # 视图
|    |---- urls.py           # 路由, 非必要
```

## 管理项目

### 创建app

```bash
python manage.py startapp myapp
```

### 迁移数据库

#### 创建迁移文件至

```bash
python manage.py makemigrations
```

#### 迁移至数据库

```bash
python manage.py migrate
```

#### 从数据库迁移至python模型

```bash
python manage.py inspectdb>myapp/models.py
```

### 运行和构建

#### 运行

性能较差, 仅用于开发环境, 生产环境使用 uwsgi / nginx

```bash
python manage.py runserver
```

#### 收集静态文件

```bash
python manage.py collectstatic
```

## 视图

`django.views.generic`

| 视图类         | 描述     |
| -------------- | -------- |
| `View`         | 普通视图 |
| `TemplateView` | 模板视图 |

五大视图

| 动作 | 视图名                   |
| ---- | ------------------------ |
| 增   | `CreateView`             |
| 删   | `DeleteView`             |
| 改   | `UpdateView`             |
| 查   | `ListView`, `DetailView` |

## 数据模型

`django.db.models`

### Instance

| 方法     | 描述           |
| -------- | -------------- |
| `save`   | 保存           |
| `get`    | 获取某一列的值 |
| `delete` | 删除           |

### QuerySet | objects

| 方法          | 描述                     |
| ------------- | ------------------------ |
| `all`         | 全部                     |
| `filter`      | 筛选                     |
| `get`         | 获取实例, 如没有则抛异常 |
| `delete`      | 删除                     |
| `update`      | 更新                     |
| `create`      | 创建                     |
| `bulk_create` | 创建多个                 |
| `order_by`    | 排序                     |

## 表单

`django.forms`

| 方法           | 描述               |
| -------------- | ------------------ |
| `is_valid`     | 验证是否成功       |
| `is_bound`     | 是否绑定了表单数据 |
| `errors`       | 验证失败的错误信息 |
| `cleaned_data` | 验证后的数据       |
