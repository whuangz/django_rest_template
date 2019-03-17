import json
import ast
import math
from datetime import datetime

class BaseSerializer():

    def __init__(self, transformer_class, item):
        self.transformer_class = transformer_class
        self.item = item
        self.__is_list = isinstance(item, list)

    def data(self):
        pass

    def list(self):
        if self.__is_list:
            return [self.transformer_class(an_item).data() for an_item in self.item]
        else:
            raise 'error : object is not a type of List'

    def to_json(self):
        if self.__is_list is True:
            return json.dumps(self.list())
        else:
            return json.dumps(self.data())

class ArticleSerializer(BaseSerializer):

    def __init__(self, article):
        super().__init__(ArticleSerializer, article)

    def data(self):
        article = self.item
        mapper = {
            "id": article.id,
            "title": article.title,
            "summary": article.summary,
        }
        return mapper
