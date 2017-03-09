#coding:utf-8
import os

import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
from tornado.options import define, options

from controller import *

define("port", default=8911, help="run on the given port", type=int)


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
            (r'/contact/', contact.ContactHandler),
            (r'/sleep/', sleep.SleepHandler),
            (r'/demo/ct/',index.IndexHandler),
            (r'/demo/ct/index/',index.IndexHandler),
            (r'/demo/ct/login/',login.LoginHandler),
            (r'/demo/ct/contact/', contact.ContactHandler),
            (r'/demo/ct/submit/',submit.SubmitHandler),
            (r'/demo/ct/index/submit/',submit.SubmitHandler),
            (r'/demo/ct/autocomplete/',autocomplete.AutocompleteHandler),
            (r'/demo/ct/index/autocomplete/',autocomplete.AutocompleteHandler),
        ]
        settings={
            'static_path':os.path.join(os.path.dirname(os.path.abspath(__file__)),'static'),
            #'static_url_prefix':'static/',
            'template_path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template'),
            'login_url':'/login',
            'cookie_secret':'F/hsxF7kTIWGO1F6HrH78Rf4bMRe5EyFhjtReh6x+/E=',
            'xsrf_cookies':False,
            'debug':True,
            #'ui_modules':{'Hello': HelloModule}
        }
        super(Application,self).__init__(handlers,**settings)

def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop().instance().start()
