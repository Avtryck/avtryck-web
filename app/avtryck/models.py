from google.appengine.ext import db

class DictMixin(object):
    # this method stolen from 
    # http://stackoverflow.com/questions/1531501/json-serialization-of-google-app-engine-models
    # thank you, David Wilson
    def to_dict(self):
        model = self
        output = {}
        for key, prop in model.properties().iteritems():
            value = getattr(model, key)

            if value is None or isinstance(value, SIMPLE_TYPES):
                output[key] = value
            elif isinstance(value, date):
                # Convert date/datetime to ms-since-epoch ("new Date()").
                ms = time.mktime(value.utctimetuple()) * 1000
                ms += getattr(value, 'microseconds', 0) / 1000
                output[key] = int(ms)
            elif isinstance(value, db.Model):
                output[key] = to_dict(value)
            else:
                raise ValueError('cannot encode ' + repr(prop))
        output["id"] = model.key().id()
        return output

    def update_from_dict(self, dict_representation):
        for k, v in dict_representation.iteritems():
            if hasattr(self, k):
                logging.info("%s = %s" % (k,v))
                field_type = type(getattr(self, k))
                logging.info(field_type)
                if field_type == long:
                    v = int(v)
                if field_type == datetime:
                    logging.info(v)
                    v = datetime.fromtimestamp(v/1000) # microseconds in javascript
                    logging.info(v)
                setattr(self, k, v)


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

class Route(db.Model, DictMixin):
    title = db.StringProperty()
    desc = db.TextProperty()
    creator = db.ReferenceProperty(Profile)
    likes = db.IntegerProperty()
    duration = db.IntegerProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    places = db.ListProperty(db.Key)
