from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean, ForeignKey, Table, Float
from sqlalchemy.ext.declarative import ConcreteBase
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import relationship, column_property
from core.base import BaseModel
from datetime import datetime
import uuid

class SoftDeletionBase(AbstractConcreteBase):

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()

# TABLE
class Account(BaseModel, SoftDeletionBase):
    __tablename__ = 'accounts'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    email= Column(String(255))
    type = Column(String(255))
    is_verified = Column(Integer)
    can_change_password = Column(Integer)
    is_skip_verification = Column(Integer)
    uuid = Column(String(255))

    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    deleted_at = Column(DateTime(), nullable=True)

    account_oauth = relationship("AccountOauth")
    teacher= relationship("Teacher",lazy="dynamic")



    def as_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            email=self.email,
        )

    def __init__(self, param):
        self.name = param["name"]
        self.email = param["email"]
        self.type = param["account_type"]
        self.is_verified = 0
        if param["type"] == 'password':
            self.can_change_password = 1
        self.is_skip_verification = 0
        self.uuid = uuid.uuid1()

    def __repr__(self):
        return self.email

class AccountOauth(BaseModel, SoftDeletionBase):
    __tablename__ = 'accounts_oauths'

    id = Column(Integer(), primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    oauth_user_id = Column(Integer)

    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    deleted_at = Column(DateTime(), nullable=True)

    account = relationship("Account", uselist=False)

    def as_dict(self):
        return dict(
            id=self.id
        )

    def __init__(self, param):
        self.account_id = param["account_id"]
        self.oauth_user_id = param["oauth_user_id"]

    def __repr__(self):
        return str(self.id)

class Teacher(BaseModel, SoftDeletionBase):
    __tablename__ = 'teachers'

    id = Column(Integer(), primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    teaching_field = Column(String(255))
    
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    deleted_at = Column(DateTime(), nullable=True)

    account = relationship("Account", uselist=False)

    def as_dict(self):
        return dict(
            id=self.id
        )

    def __init__(self, param):
        self.account_id = param["account_id"]
        self.teaching_field = param["teaching_field"]

    def __repr__(self):
        return str(self.id)

class Student(BaseModel, SoftDeletionBase):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    major = Column(String(255))

    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    deleted_at = Column(DateTime(), nullable=True)

    account = relationship("Account", uselist=False)

    def as_dict(self):
        return dict(
            id=self.id
        )

    def __repr__(self):
        return str(self.id)