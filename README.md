书香自动化测试

> 此测试完全依赖于 https://github.com/DoubleXm/book-scents 项目
> 
> 开始之前请确保，前后台项目已启动。


```
.
├── artifacts     # 测试结果目录
│   ├── allure
│   ├── logs
│   ├── reports
│   └── screenshorts
├── pytest.ini    # pytest 配置文件
├── README.md     # 项目说明文档
├── requirements.txt     # 项目依赖库
├── scripts     # 脚本目录（比如创建数据、小型爬虫等与公司业务有关，但是非测试型的代码）
└── src
    ├── api     # API 测试目录
    │   ├── client     # 接口请求
    │   │   ├── book_client.py
    │   │   ├── comment_client.py
    │   │   └── user_client.py
    │   ├── data     # 测试数据目录
    │   │   ├── book_failed_paramter.json
    │   │   ├── comment_failed_paramter.json
    │   │   └── create_data.py
    │   └── tests     # 测试用例目录
    │       ├── conftest.py
    │       ├── test_book.py
    │       └── test_comments.py
    ├── assets     # 测试资产目录（比如图片、文件等）
    │   └── album-cover.jpeg
    ├── main.py
    ├── ui     # UI 测试目录
    │   ├── data
    │   ├── pages
    │   └── tests
    └── utils     # 工具目录
        ├── config.py     # 配置文件
        ├── db_client.py     # 数据库客户端
        ├── helper.py     # 辅助函数
        ├── http_client.py     # HTTP 二次封装
        └── logger.py     # 日志模块
```