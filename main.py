#coding:utf-8
import tornado.options
from tornado.options import define, options
#import tornado.gen
import tornado.web
import tornado.httpserver
import tornado.ioloop

import os, time

#import common
from handler import *

define("port", default=8911, help="run on the given port", type=int)

# class SleepHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     @tornado.gen.coroutine
#     def get(self):
#         yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout,time.time()+5)
#         self.write("@1 after sleeping or 5s")
#         self.finish() # 四次握手关闭连接
 

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',index.IndexHandler),
            (r'/index/',index.IndexHandler),
            (r'/login/',login.LoginHandler),
            (r'/submit/',submit.SubmitHandler),
            (r'/index/submit/',submit.SubmitHandler),
            (r'/autocomplete/',autocomplete.AutocompleteHandler),
            (r'/index/autocomplete/',autocomplete.AutocompleteHandler),
            (r'/contact/',contact.ContactHandler),
            (r'/demo/ct/',index.IndexHandler),
            (r'/demo/ct/index/',index.IndexHandler),
            (r'/demo/ct/login/',login.LoginHandler),
            (r'/demo/ct/contact/',contact.ContactHandler),
            (r'/demo/ct/submit/',submit.SubmitHandler),
            (r'/demo/ct/index/submit/',submit.SubmitHandler),
            (r'/demo/ct/autocomplete/',autocomplete.AutocompleteHandler),
            (r'/demo/ct/index/autocomplete/',autocomplete.AutocompleteHandler),
        ]
        settings={
            'static_path':os.path.join(os.path.dirname(os.path.abspath(__file__)),'static'),
            'template_path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
            'login_url':'/login',
            'cookie_secret':'F/hsxF7kTIWGO1F6HrH78Rf4bMRe5EyFhjtReh6x+/E=',
            'xsrf_cookies':False,
            'debug':True,
            #'ui_modules':{'Hello': HelloModule}
        }
        super(Application,self).__init__(handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop().instance().start()

