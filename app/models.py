from . import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    mac_address = db.Column(db.String(20))
    ip_address = db.Column(db.String(15))
    current_location_id = (db.Integer, db.ForeignKey('maps.location_id'))


class Policy(db.Model):
    __tablename__ = 'policies'
    policy_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('maps.location_id'))
    text_id = db.Column(db.Integer, db.ForeignKey('texts.text_id'))
    video_id = db.Column(db.Integer, db.ForeignKey('videos.video_id'))
    starting_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    event_type = db.Column(db.String(20))


class UserPolicy(db.Model):
    __tablename__ = 'user_policies'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.policy_id'))


class Map(db.Model):
    __tablename__ = 'maps'
    location_id = db.Column(db.Integer, primary_key=True)
    campus = db.Column(db.String(20))
    building = db.Column(db.String(20))
    floor = db.Column(db.String(20))
    zone = db.Column(db.String(20))


class Text(db.Model):
    __tablename__ = 'texts'
    text_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)


class Video(db.Model):
    __tablename__ = 'videos'
    video_id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String)