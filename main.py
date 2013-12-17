import os
import tornado.ioloop
import tornado.web
import examples

langList = ['c','python','haskell','clisp']
langNames = {'c': 'C', 'python': 'Python', 'haskell': 'Haskell', 'clisp': 'Common Lisp'}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html", languages=langList, langNames=langNames)

class ExampleHandler(tornado.web.RequestHandler):
    def get(self, language, chapter):
        chapters = examples.getChapters(language)
        exs = examples.exercise(language, chapter)
        self.render("examples.html", language=language, languages=langList,
                langNames=langNames, chapters=chapters, exercises=exs)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "assets"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/assets/(.*)",tornado.web.StaticFileHandler, {"path": "./assets"},),
    (r"/examples/(.*)/(.*)", ExampleHandler),
    ], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
