import core.api_controller as base_controller
import json

from rest_framework.decorators import api_view
from core.models import Category
from core.base import session
#from core.serializers import 

@api_view(['GET'])