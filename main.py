import os
import tornado.ioloop
import tornado.web
import examples
from build import langList, langNames, hlName

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html", languages=langList, langNames=langNames)

class ExampleHandler(tornado.web.RequestHandler):
    def get(self, language, chapter=''):
        chapters = examples.getChapters(language)
        if chapter == "":
            chapter = chapters[0]
        exs = examples.exercise(language, chapter)
        self.render("examples.html", language=language, languages=langList,
                langNames=langNames, chapters=chapters, chapter=chapter,
                exercises=exs, hlName=hlName[language], title=langNames.get(language))

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("faq.html", languages=langList, langNames=langNames)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "assets"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/assets/(.*)",tornado.web.StaticFileHandler, {"path": "./assets"},),
    (r"/examples/(.*)/(.*)", ExampleHandler),
    (r"/examples/(.*)", ExampleHandler),
    (r"/faq.html", FaqHandler),
    ], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
