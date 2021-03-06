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
from models import post_model
import jinja2
import json
import os
import webapp2
from OGE import oge_response
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class FrontPage(webapp2.RequestHandler):
    def get(self):
        front_template = jinja_environment.get_template("templates/front.html")
        self.response.write(front_template.render())
    def post(self):
        letter = self.request.get("message")
        name = self.request.get("username")
        answer = oge_response(letter)
        front_template = jinja_environment.get_template("templates/front.html")
        self.response.write(front_template.render({'answer': answer, "text":letter, "user":name}))
        if answer != "NEUTRAL":
            input_post = post_model(text = letter, user = name, out = answer)
            input_post.put()


class PastPosts(ndb.Model):
    name = ndb.StringProperty()
    question = ndb.StringProperty()
    time = ndb.DateTimeProperty()
    answer = ndb.StringProperty()


class PastPostsPage(webapp2.RequestHandler):
    def get(self):
        query = post_model.query().order(-post_model.time_stamp)
        responses = query.fetch()
        past_template = jinja_environment.get_template("templates/past.html")
        self.response.write(past_template.render({'responses':responses}))
        #gonna have to use storing_in_DB.get.username() for getting name, time etc
        #do i wanna use

class neut_handler(webapp2.RequestHandler):
    def post(self):
        whole  = self.request.body
        better_whole = json.loads(whole)
        quote = better_whole["out"]
        letter = better_whole["text"]
        name = better_whole["user"]
        input_post = post_model(text = letter, user = name, out = quote)
        input_post.put()

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_environment.get_template("templates/about.html")
        self.response.write(about_template.render())

class WaysToHappyPage(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_environment.get_template("templates/ways_to_happy.html")
        self.response.write(about_template.render())

app = webapp2.WSGIApplication([
    ('/', FrontPage),("/neut", neut_handler),
    ('/past', PastPostsPage), ("/about", AboutPage), ("/waystohappy", WaysToHappyPage)], debug=True)
