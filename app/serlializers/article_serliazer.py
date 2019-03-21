import json
import ast
import math
from datetime import datetime
from core.serializer import BaseSerializer

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
