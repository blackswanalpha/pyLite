from database import db
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, String, Text, DateTime, func

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

def create_model(name, fields):
    attrs = {
        '__tablename__': name.lower(),
        'id': Column(Integer, primary_key=True, autoincrement=True)
    }
    attrs.update(fields)
    return type(name, (Base,), attrs)

def create_new_table(table_name, fields):
    model = create_model(table_name, fields)
    db.create_all()
    return model

# Example usage:
post_fields = {
    'title': db.Column(db.String(100), nullable=False),
    'content': db.Column(db.Text, nullable=False),
    'created_at': db.Column(db.DateTime, default=db.func.now())
}
Post = create_new_table('Post', post_fields)
