import json
import ast
import math
from datetime import datetime
from core.serializer import BaseSerializer

class AccountSerializer(BaseSerializer):

    def __init__(self, account):
        super().__init__(AccountSerializer, account)

    def data(self):
        account = self.item
        mapper = {
            "id": account.id,
            "name": account.name,
            "email": account.email,
            "uuid" : account.uuid,
            # "created_at": account.created_at,
            # "updated_at": account.updated_at,  
        }

        if hasattr(account, "access_token"): 
            mapper["access_token"] = account.access_token
        if hasattr(account, "refresh_token"): 
            mapper["refresh_token"] = account.refresh_token
        if account.type == 'teacher':
            mapper["accountable"] = TeacherSerializer(account.teacher.first()).data()

        return mapper

class TeacherSerializer(BaseSerializer):
    def __init__(self, teacher):
        super().__init__(TeacherSerializer, teacher)

    def data(self):
        teacher = self.item
        mapper = {
            "teaching_field": teacher.teaching_field,
        }
        
        return mapper