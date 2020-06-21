1. http 与 https 理解：
    http：请求协议， 超文本传输协议 默认端口是80
    https: 提供了安全通道的请求协议， 添加了ssl层 对数据加密， 默认端口是443

2. 状态码：
    20X：处理成功相应类
        200：请求被接受，获得相应内容
        201: xx提示知道新文件的URL
        202：请求被接受，未处理完
        203: 返回的信息不确定或不完整
        204: 请求被接受，但没有返回信息
    30X：重定向相应类
        300: xx请求的资源可以在多处获得
        301: 永久重定向
        302: 临时重定向
        303: 建议用户访问其他URL
        304: 请求的资源未更新 ？？客户端已经执行了Get，但文件未变化
    40X：客户端错误
        400: 非法请求，语法错误
        401: 未授权
        402: 保留有效ChargeTo头响应？
        403: 禁止访问
        404: 路径错误
    50X：服务器错误
        500: 服务器内部错误
        501: 服务器无法识别当前请求
        502: 错误网关
        503: 服务器当前维护或者过载，当前无法处理请求

3. 爬虫函数库：
    urllib
        urllib.require.urlopen()
    urllib2
        urllib2.urlopen()
    requires
        requires.requires.get()/post()

    beautifulSoup4


4. 解释一下robox协议
    robox是一个纯文本文件，他是网站管理者告诉网络程序可以访问那些内容, 里面的格式是一些约定俗成的
    当一个搜索引擎访问一个站点时，首先检查该站点的根目录下是否有roboxs.txt，如果该文件存在，则安照协议的内容确定访问的范围，
    如果不存在，则从起始页沿着链接爬去

    作用：提高访问的利率
        引导搜索引擎爬去指定内容
        屏蔽一些无效链接或者不存在的链接
        避免重复爬取

5. 介绍一下Scrapy 框架
    引擎：核心，控制整个数据爬取的过程
    调度器：接受引擎发过来的请求，加入队列，去重复，决定下一个爬去什么URL
    下载器：下载网页内容，并将网页内容返回给spiders
    spiders：处理返回的网页信息，即实体items，将实体返回给items管道，同时可以提取链接
    项目管道：接收实体，并保存
    调度中间件：引擎发送调度请求
    下载中间件：引擎和下载器之间的请求和响应
    spiders中间件：引擎和spiders之间的请求和响应

    大致流程：
        1. 引擎从调度器中取出一个URL
        2. 引擎把URL封装成一个Require发给下载器
        3. 下载器下载资源后封装成Response返回给引擎
        4. 引擎将数据传给spiders 解析，解析的URL通过引擎给调度器，items通过引擎给管道
        5. 管道进行数据持久化

    1. 为什么使用Scrapy框架：
        首先使用框架是为了使我们的爬虫更加高效，Scrapy就有这样的作用：
            1. 异步爬去，能够在短时间内完成大量的RUL请求
            2. 成熟的API，编写少量的代码就可以实现特定功能的爬虫
            3. 支持各种插件，功能比较强大

    2. 用过哪些scrapy插件：
        随机头
        管道
        headless

    3. setting设置过哪些参数：
        robox.txt
        最大的并发请求数
        cookies
        dont_filter
        DEFAULT_REQUEST_HEADERS  请求头参数
        插件声明和优先级设置
        DOWNLOAD_DELAY 请求延时
    4. scrapy 的去重原理：
        scrapy带有去冲的中间件duperfilter.py
        对于每个URL调度器会去请求获取指纹信息（可以理解为唯一的hash值），然后将指纹信息和set集合中的指纹信息对比进行去重
    

6. 爬虫有哪些反扒措施？如何应对？
    header：
        1. User-agent  设置浏览器头
        2. cookies 设置cookies
        其他字段：accept ref

    IP
        速率限制：降低访问频率
        次数限制：代理IP

    登陆：
        登陆查看： 设置cookies

    动态网页：
        selenium 模拟浏览器
        如果是RESTful 的网站，可以直接构造数据请求链接

    验证码：
        图片识别

    人机认证：
        selenium 模拟浏览器



7. 爬过那些网站
    安全信息网站：
        SecurityFocus：讨论不同产品的漏洞信息
        CoreSecurity：跟踪 CVE 安全漏洞信息的进展情况

8. TCP三次握手和四次挥手：
    三次握手：报文
        1. 客户 （SYN=1， ACK=0，seq=x） 服务器
        2. 服务器 （SYN=1，ACK=1， ack=x+1， seq=y） 客户
        3. 客户  （ACK=1，seq=x+1, ack=y+1) 服务器

    四次挥手：
        1. 客户   （FIN=1，seq=u） 服务器
        2. 服务器  （ACK=1，ack=u+1， seq=v）客户
        3. 服务器   （FIN=1， ACK=1，ack=u+1，seq=w） 客户
        4. 客户。  （ACK=1， ack=w+1，seq=u+1）    客户

9. HTTP 常见的头部字段
    accept-encoding
    Connection
    refer
    cookies
    User-agent

10. get和post的区别：
    在数据传输上：
        get通过拼接URL传递参数， 长度有限制
        post通过require中的body字段传递参数，长度没有限制
    参数可见性上：
        get参数可见
        post参数不可见
    安全性上：
        post比get传参数更安全些

11. OSI 7层模型 5层模型
    应用层：HTTP HTTPS DNS POP3 DHCP
        表示层 数据表示
        会话层 建立对话
    传输层：TCP UDP
    网络层：IP  ICMP IGMP
    链路层：建立逻辑链接
    物理层：建立物理链接 断开

12. 网络爬虫 - 反爬与反反爬
    1. robots.txt 协议

    2. ip层：
        ip限制 或者封杀 -----> ip 代理 - 降低爬取的频率 

    3. http层： -----> 设置好必要的字段信息
        X-Forwarded-for xff 保存原始IP
        referer
        User-Agent
        cookier


    4. 浏览器层：  
        ajax 动态请求数据 -------> 前端逆向分析 构造数据的请求链接
        接口加密 -- token参数 （用户id、cookied信息、ip信息）通过js加密（md5、sha256) 加密得到 --->   解析加密过程
        验证码 数字验证码、文字验证码、图片验证码 ---> 使用selenium 模拟浏览器 图片数字识别 打码平台


    5. 安全检测：
        异常行为检测 短时间内大量访问 用户操作轨迹和爬虫的操作轨迹不同 - 浏览商品
        拒绝cookies
        浏览器中 window.navigator 对象保持了很多的操作系统、浏览器信息 用于和ua对比
        js函数
        假链陷阱
        

13. js调试
    检查 - sources - 点击设置断点（右边出现调试信息）
        - network - 查看数据请求链接 （分析请求里面的header部分 response）

14. webkit --- 开源的浏览器内核

15. 数据筛选：
    正则表达式、Xpath、BeautifulSoup4等等 
    正则表达式：
        ^， $
        *， +， ?
        {n}， {n,}， {n,m}
        ? # 非贪婪匹配 例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”。
        . 匹配除“\n”之外的任何单个字符。要匹配包括“\n”在内的任何字符，请使用像“(.|\n)”的模式。
        x|y， [xyz]， [^xyz]， [a-z]， [^a-z]
        \b
        \d == [0-9], \D == [^0-9]
        \n, \r, \t
        \w == [A-Za-z0-9_]

        import re
        pattern = re.compile('正则表达式')
        pattern.match() # 头
        pattern.search() # 全文
        pattern.findall() # list

    xpath:
        / 
        //
        @  //td[@width='100']
        lxml etree

    beautifulsoup
        BeautifulSoup：文档对象
        Tag：标签对象
        NavigableString：字符内容操作对象
        Comment：特殊类型的NavigableString









