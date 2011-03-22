import os
from google.appengine.ext.webapp import template
import webapp2 as webapp

class BaseHandler(webapp.RequestHandler):
    def render_template(self, template_name, template_values={}):
        values = self.get_config("templates", "default_params", {})
        values.update(template_values)

        path = os.path.join(self.get_config("templates", "root"), template_name)
        return template.render(path, values)
        