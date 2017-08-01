#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class FrontPage(webapp2.RequestHandler):
    def get(self):
        front_template = jinja_environment.get_template("templates/front.html")
        self.response.write(front_template.render())
    def post(self):
        letter = self.request.get("message")

        self.response.write(letter)

class PastPostsPage(webapp2.RequestHandler):
    def get(self):
        past_template = jinja_environment.get_template("templates/past.html")
        self.response.write(past_template.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_environment.get_template("templates/about.html")
        self.response.write(about_template.render())

class WaysToHappyPage(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_environment.get_template("templates/ways_to_happy.html")
        self.response.write(about_template.render())

app = webapp2.WSGIApplication([
    ('/', FrontPage),
('/past_posts', PastPostsPage), ("/about", AboutPage), ("/waystohappy", WaysToHappyPage)], debug=True)
