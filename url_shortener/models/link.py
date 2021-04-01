from url_shortener.extenstions import db
from datetime import datetime
import string
import random


class LinkModel(db.Model):
    __tablename__ = 'links'

    link_id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(80))
    short_url = db.Column(db.String(20))
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url

    def json(self):
        return {
            'id': self.id,
            'original_url': self.original_url,
            'short_url': self.short_url,
            'visits': self.visits,
            'date_created': self.date_created
        }

    @classmethod
    def find_by_original_url(cls, original_url):
        return cls.query.filter_by(original_url=original_url).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def commit_to_db(self):
        db.session.commit()

    @classmethod
    def find_by_link_id(cls, link_id):
        return cls.query.filter_by(link_id=link_id).first()

    @classmethod
    def find_by_short_url(cls, short_url):
        return cls.query.filter_by(short_url=short_url).first()

    @classmethod
    def get_short_url(cls):
        characters = string.digits + string.ascii_letters
        print(characters)
        short_url = ''.join(random.choices(characters, k=8))
        print(characters)
        link = cls.find_by_short_url(short_url)

        if link:
            return cls.get_short_url()

        return short_url

    @classmethod
    def get_all_links(cls):
        return cls.query.all()
