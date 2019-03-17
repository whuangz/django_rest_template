from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from user import views as UserView
from controller import article_controllers as ArticleController

# router = DefaultRouter()
# router.register('', CreateUserView, base_name='users')
# urlspatterns = router.urls

urlpatterns = {
	#path('user/create/', UserView.CreateUserView.as_view(), name="create"),

	#articles
	path('articles/', ArticleController.get_articles_controller, name="articles")
}

urlpatterns = format_suffix_patterns(urlpatterns)