from google.appengine.ext import ndb

class post_model(ndb.Model):
    text = ndb.StringProperty()
    time_stamp = ndb.DateTimeProperty(auto_now_add = True)
    user = ndb.StringProperty()
    out = ndb.StringProperty()
