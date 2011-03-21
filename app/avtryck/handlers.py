from avtryck.base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.redirect("/edit")


class EditHandler(BaseHandler):
    def get(self):
        self.response.out.write(self.render_template("edit/index.html"))