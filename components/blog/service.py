from components.blog.models import Post
from database import db

class CRUDService:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def get_by_id(self, item_id):
        return self.model.query.get(item_id)

    def create(self, data):
        new_item = self.model(**data)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def update(self, item_id, data):
        item = self.get_by_id(item_id)
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    def delete(self, item_id):
        item = self.get_by_id(item_id)
        db.session.delete(item)
        db.session.commit()
        return item


