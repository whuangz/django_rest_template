import core.api_controllers as base_controllers

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .model import Account, AccountOauth, Teacher, Student
from .service import TeacherService, AccountService
from .serializer import AccountSerializer

@api_view(['POST'])
@permission_classes((AllowAny, ))
def register_teacher(request):
	
	if request.method == 'POST':
		body = None

		#validate data request
		valid_data = {}
		data = request.data
		try:
			valid_data["email"] = data.get('email')
			valid_data["name"] = data.get("name")
			valid_data["type"] = data.get("type")
			if data.get("type") == 'password':
				valid_data["password"] = data.get("password")
			valid_data["teaching_field"] = data.get("teaching_field")
			body = valid_data
		except:
			body = None

		if not body:
			return base_controllers.render_json(status=400, data="Wrong Input Parameters", message="Wrong Input Parameters")

		teacher_service = TeacherService()
		body["account_type"] = "teacher"
		token, error = teacher_service.create_teacher(body)

		if not token:
			return base_controllers.render_json(status=error["status_code"], data=error["message"], message=error["message"])
		return base_controllers.render_json(data=token)
	else:
	    return base_controllers.render_json(status=400, data="Wrong Input Parameters", message="Wrong Input Parameters")

@api_view(['POST'])
@permission_classes((AllowAny, ))
def login_account(request):
	if request.method == 'POST':
		body = None
		valid_data = {}
		data = request.data
		try:
			valid_data["email"] = data.get("email")
			valid_data["password"] = data.get("password")
			valid_data["type"] = data.get("type")
			if data.get("type") == 'password':
				valid_data["password"] = data.get("password")
			body = valid_data
		except:
			body = None

		if not body:
			return base_controllers.render_json(status=400, data="Wrong Input Parameters", message="Wrong Input Parameters")

		account_service = AccountService()
		account,error = account_service.create_login(body)

		if not account:
			return base_controllers.render_json(status=error["status_code"], data=error["message"], message=error["message"])
		return base_controllers.render_json(data=account, serializer=AccountSerializer)


	return base_controllers.render_json(status=400, data="Wrong Input Parameters", message="Wrong Input Parameters")


