from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from controllers import article_controllers as ArticleController
from auth import controller as AccountController

urlpatterns = {
	#path('articles/', ArticleController.get_articles_controller, name="articles")
	path("register", AccountController.register_teacher, name="register"),
	path("login", AccountController.login_account, name="login")
	
}

urlpatterns = format_suffix_patterns(urlpatterns)