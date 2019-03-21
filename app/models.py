from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean, ForeignKey, Table, Float
from sqlalchemy.ext.declarative import ConcreteBase
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import relationship, column_property
from core.base import BaseModel
from datetime import datetime

class SoftDeletionBase(AbstractConcreteBase):

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()

# TABLE
