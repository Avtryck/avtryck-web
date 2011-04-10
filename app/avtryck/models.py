from google.appengine.ext import db

class Profile(db.Model):
    google_user = db.UserProperty()

class Provider(db.Model):
    name = db.StringProperty()

class Media(db.Model):
    mime = db.StringProperty()
    url = db.LinkProperty()
    preview = db.SelfReferenceProperty()

class Record(db.Model):
    title = db.StringProperty()
    desc = db.TextProperty()
    location = db.GeoPtProperty()
    provider = db.ReferenceProperty(Provider)
    media = db.ListProperty(db.Key)

class Place(db.Model):
    title = db.StringProperty()
    desc = db.TextProperty()
    location = db.GeoPtProperty()
    radius = db.FloatProperty()
    records = db.ListProperty(db.Key)

class Route(db.Model):
    title = db.StringProperty()
    desc = db.TextProperty()
    creator = db.ReferenceProperty(Profile)
    likes = db.IntegerProperty()
    duration = db.IntegerProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    places = db.ListProperty(db.Key)
