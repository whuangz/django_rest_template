from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.ext.declarative import ConcreteBase
from sqlalchemy.ext.declarative import AbstractConcreteBase
from core.base import BaseModel

class SoftDeletionBase(AbstractConcreteBase):

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()

# TABLE
class Article(BaseModel, SoftDeletionBase):
    __tablename__ = 'articles'
    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    source_id = sa.Column(sa.Integer(), sa.ForeignKey("sources.id"))
    title = sa.Column(sa.String(255))
    summary = sa.Column(sa.String(1023))

    created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    deleted_at = sa.Column(sa.DateTime(), nullable=True)

    def as_dict(self):
        return dict(
            id=self.id,
        )

    def __repr__(self):
        return str(self.id)

class Source(BaseModel, SoftDeletionBase):
    __tablename__ = 'sources'

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(255))
    domain = sa.Column(sa.String(255))
    base_url = sa.Column(sa.String(255))
    logo = sa.Column(sa.String(1023))

    created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    deleted_at = sa.Column(sa.DateTime(), nullable=True)

    def as_dict(self):
        return dict(
            id=self.id
        )

    def __repr__(self):
        return str(self.id)


# from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean, ForeignKey, Table, Float
# from sqlalchemy.orm import relationship, column_property