微信机器人

itchat

- 模拟微信登陆

  - get请求获取uuidhttps://login.weixin.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_US&_={时间戳}，重定向到第三步url:状态轮询访问
  - 基于uuid请求二维码https://login.weixin.qq.com/qrcode/{uuid}
  - 轮询访问二维码状态https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={}==&tip=1&r=-2026440414&_={时间戳}

    - 200--成功，重定向
    - 201--被扫描，返回用户头像等信息
    - 408--失效
  
- 通过python decorator来对消息处理函数做注册
- 开启线程同步消息，对于新来的消息，基于friend/groupchat做出判断，调用不同的处理方法
  - 处理方法提取text问题，把问题通过request.post方法传递给后端模型
  - 提取模型返回结果，发送微信消息

