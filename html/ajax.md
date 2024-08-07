# Ajax

## 原生

```js
// 创建XMLHttpRequest对象
var xhr = new XMLHttpRequest();
// 编写回调函数
xhr.onreadystatechange = function() {
  // 判断请求状态和响应状态
  if (xhr.readyState == 4 && xhr.status == 200) {
    // 处理响应数据
    console.log(xhr.responseText);
  }
};
// 配置请求信息
xhr.open("GET", "https://example.com/api", true);
// 发送请求
xhr.send();
```

## jquery

如果 jquery 是最后一个引入的外部文件，可以直接使用 $ 对象, 否则使用 jQuery 对象

```js
let data = {
    username: "admin",
    password: "1234"
}

// 使用 get 请求
$.ajax({
    // 请求地址
    url: "https://example.com/api",
    // 请求方式
    type: "get",
    // 跟在url后的参数
    params: {},
    // 成功时触发
    success(response) {},
    // 失败时触发
    error(e) {}
})

// post 传输 json 数据
$.ajax({
    url: "https://example.com/api",
    type: "post",
    // 请求体
    data: JSON.stringify(data),
    // 设置内容类型
    contentType: "application/json;charset=UTF-8;",
    success(response) {
        // 解析 json
        console.log(response)
        console.log(response.data)
        // 如果没有自动解析成 json
        // console.log(JSON.parse(response.data))
    },
    error(e) {
        console.log(e)
    }
})
```

## axios

axios 为异步 Promise, 需要具备 js 异步基础

```js
// 发送 get 请求
axios.get('https://example.com/api', {
    // 跟在 url 后的参数,
    params: {}
}).then((response) => {
    // 成功
    console.log(response)
    console.log(response.data)
}).catch((e) => {
    // 失败
    console.log(e)
})

// post 发送 json 数据
axios.post('https://example.com/api', {
    // 请求体内容, 直接传入 object 会自动转成 json
    // 也可以放入 DataForm, 会处理成表单
    data: {}
}).then((response) => {
    console.log(response)
    console.log(response.data)
}).catch((e) => {
    console.log(e)
})

// 不通过方法指明请求方式
axios({
    method: 'post',
    data: {}
}).then((response) => {
    console.log(response)
    console.log(response.data)
}).catch((e) => {
    console.log(e)
})
```
