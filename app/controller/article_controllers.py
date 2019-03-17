import core.api_controllers as base_controller
import json

from rest_framework.decorators import api_view
from core.models import Article
from core.base import session
from core.serializers import ArticleSerializer
from sqlalchemy import text

@api_view(['GET'])
def get_articles_controller(request):
    
    # if request.method == 'GET':
    # 	articles_query = text('''
    # 			select id, title, summary,
    # 			from articles
    # 		''')
    # 	articles = session.execute(articles_query).fetchall()
    # 	return base_controller.render_json(data=articles, serializer=ArticleSerializer, as_array=True)

    if request.method == 'GET':
    	articles = session.query(Article).all()
    	return base_controller.render_json(data=articles, serializer=ArticleSerializer, as_array=True)
