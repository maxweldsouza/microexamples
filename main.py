import os
import tornado.ioloop
import tornado.web
import examples
from build import titles, folders, extensions, highlights

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html", folders=folders, titles=titles)

class ExampleHandler(tornado.web.RequestHandler):
    def get(self, language, chapter=''):
        chapters = examples.getChapters(language)
        if chapter == "":
            chapter = chapters[0]
        exs = examples.exercise(language, chapter)
        highlight = highlights[folders.index(language)]
        self.render("examples.html", folder=language, folders=folders,
                chapters=chapters, chapter=chapter,
                titles=titles, title=titles[folders.index(language)],
                exercises=exs, highlight=highlight)

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("faq.html", folders=folders, titles=titles)

class CourseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("course.html", folders=folders, titles=titles)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "assets"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/assets/(.*)",tornado.web.StaticFileHandler, {"path": "./assets"},),
    (r"/examples/(.*)/(.*)", ExampleHandler),
    (r"/examples/(.*)", ExampleHandler),
    (r"/faq.html", FaqHandler),
    (r"/course.html", CourseHandler),
    ], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
