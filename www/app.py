# -*- coding:utf-8 -*-
from tornado.web import Application,RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


# 定义处理类型
class IndexHandler(RequestHandler):
    # 添加一个处理get请求方式的方法
    def get(self):
        # 向响应中，添加数据
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    http_server = HTTPServer(app)
    # 最原始的方式
    http_server.bind(8889)
    http_server.start(1)
    # 启动Ioloop轮循监听
    IOLoop.current().start()
