书香自动化测试

> 此测试完全依赖于 https://github.com/DoubleXm/book-scents 项目
> 
> 开始之前请确保，前后台项目已启动。


```
.
├── artifacts     # 测试结果目录
│   ├── logs
│   ├── reports
│   └── screenshorts
├── pytest.ini    # pytest 配置文件
├── README.md     # 项目说明文档
├── requirements.txt     # 项目依赖库
├── scripts     # 脚本目录（比如创建数据、小型爬虫等与公司业务有关，但是非测试型的代码）
│   ├── common.py  # 通用函数
│   └── generate_database_data.py # 生成数据库数据脚本
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
    ├── main.py  # 主程序文件 入口文件
    ├── ui
    │   ├── data  # 测试数据目录
    │   │   ├── create_book_paramter.json
    │   │   └── login_paramter.json
    │   ├── pages # PO 模式页面对象目录
    │   │   ├── base_page.py  # 基础页面对象类
    │   │   ├── create_book_page.py
    │   │   ├── login_page.py
    │   │   ├── profile_page.py
    │   │   └── register_page.py
    │   └── tests  # 测试用例目录
    │       ├── conftest.py
    │       ├── test_create_book.py
    │       ├── test_login_page.py
    │       └── test_profile_page.py
    └── utils     # 工具目录
        ├── config.py     # 配置文件
        ├── db_client.py     # 数据库客户端
        ├── helper.py     # 辅助函数
        ├── http_client.py     # HTTP 二次封装
        └── logger.py     # 日志模块
```

# 执行测试

## 脚本文件执行

```bash
# 执行某个脚本，比如生成数据库数据
python scripts/generate_database_data.py
```

## 测试用例执行

### 主程序执行

`main.py` 提供了区分环境的执行方式，默认执行 `dev` 环境的测试用例。可以通过参数进行区分。

```bash
# 查看所有支持的参数
python src/main.py -h
```

核心做了如下事情：

- 让 `log` 文件的命名变得更加标准，规则为 `{env}_{timestamp}.log`
- 支持通过 `--env` 参数指定环境，默认是 dev
- 支持通过 `--ui-test` `--api-test` `--all-test` 参数指定执行的测试类型，默认是 `all-test`
- 支持 `--debug` 参数，UI 模式下进入调试模式，默认是 False

```bash
# 执行 production 环境的 UI 测试用例，进入调试模式
python src/main.py --env=production --ui-test --debug
```

### pytest 执行

其核心仍然使用 `pytest` 执行测试用例。也可以通过 `pytest src/ui/tests` 执行 `ui` 目录下的测试用例。或者执行所有测试 `pytest src`。

此种模式下，会走根目录下的 `pytest.ini` 配置。