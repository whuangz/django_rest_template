# from datetime import datetime
# import sqlalchemy as sa
# import sqlalchemy.orm
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.declarative import ConcreteBase
# from sqlalchemy.ext.declarative import AbstractConcreteBase

# # Create your models here.
# BaseModel = declarative_base()

# class SoftDeletionBase(AbstractConcreteBase):

#     def soft_delete(self):
#         self.deleted_at = datetime.utcnow()

# # TABLE
# class Article(BaseModel, SoftDeletionBase):
#     __tablename__ = 'articles'
#     id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
#     source_id = sa.Column(sa.Integer(), sa.ForeignKey("sources.id"))
#     title = sa.Column(sa.String(255))
#     image_url = sa.Column(sa.String(1023))

#     created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
#     updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow,
#                         onupdate=datetime.utcnow)
#     deleted_at = sa.Column(sa.DateTime(), nullable=True)

#     def as_dict(self):
#         return dict(
#             id=self.id,
#         )

#     def __repr__(self):
#         return str(self.id)